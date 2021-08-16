# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         vqa
# Description:
# Author:       Boliu.Kelvin
# Date:         2021/5/26
# -------------------------------------------------------------------------------


import torch
import torch.nn as nn

import torch
import numpy as np
import random
from dataset_RAD import Dictionary
from model import BAN_Model
import argparse
import _pickle as cPickle
from vqa import utils
import json
import torch.nn.functional as F

def parse_args():
    parser = argparse.ArgumentParser(description="Med VQA")
    # seed config
    parser.add_argument('--seed', type=int, default=88
                        , help='random seed for gpu.default:5')
    # # Train with RAD
    parser.add_argument('--use_data', action='store_true', default=True,
                         help='Using TDIUC dataset to train')
    parser.add_argument('--data_dir', type=str,
                         help='RAD dir')
    # Activation function + dropout for classification module
    parser.add_argument('--activation', type=str, default='relu', choices=['relu', 'sigmoid'],
                        help='the activation to use for final classifier')
    parser.add_argument('--dropout', default=0.5, type=float, metavar='dropout',
                        help='dropout of rate of final classifier')

    # BAN - Bilinear Attention Networks
    parser.add_argument('--glimpse', type=int, default=2,
                        help='glimpse in Bilinear Attention Networks')
    parser.add_argument('--use_counter', action='store_true', default=False,
                        help='use counter module')

    # Question ---------------------------------------------------------------------------------------------------------
    # Choices of RNN models
    parser.add_argument('--rnn', type=str, default='GRU', choices=['LSTM', 'GRU'],
                        help='the RNN we use')
    # Question embedding
    parser.add_argument('--question_len', default=12, type=int, metavar='N',
                        help='maximum length of input question')
    parser.add_argument('--tfidf', type=bool, default=True,
                        help='tfidf word embedding?')
    parser.add_argument('--cat', type=bool, default=True,
                        help='concatenated 600-D word embedding')
    parser.add_argument('--hid_dim', type=int, default=1024,
                        help='dim of joint semantic features')

    # Vision -----------------------------------------------------------------------------------------------------------
    # Input visual feature dimension
    parser.add_argument('--v_dim', default=128, type=int,
                        help='visual feature dim')

    # details
    parser.add_argument('--details', type=str, default='original ')

    args = parser.parse_args()
    return args

args = parse_args()
args.data_dir = 'vqa/data/rad/'
torch.manual_seed(args.seed)
torch.cuda.manual_seed(args.seed)
torch.cuda.manual_seed_all(args.seed)
np.random.seed(args.seed)  # Numpy module.
random.seed(args.seed)  # Python random module.
torch.backends.cudnn.benchmark = False
torch.backends.cudnn.deterministic = True
# create word dictionary from train+val dataset
d = Dictionary.load_from_file('./vqa/data/rad/dictionary.pkl')
ans2label = cPickle.load(open('./vqa/data/rad/cache/trainval_ans2label.pkl', 'rb'))
label2ans = cPickle.load(open('./vqa/data/rad/cache/trainval_label2ans.pkl', 'rb'))
vqa_model = BAN_Model(d,args,len(ans2label))

ckpt = torch.load('./vqa/model.pth',map_location='cpu')
vqa_model.load_state_dict(ckpt,strict=True)
vqa_model.eval()



imgs = cPickle.load(open('./vqa/data/rad/images128x128.pkl', 'rb'))
imgs = torch.from_numpy(imgs).type('torch.FloatTensor')
img_id = json.load(open('./vqa/data/rad/imgid2idx.json','r'))


def tokenize(question, max_length=12):
    """
    Tokenizes the questions.
    This will add q_token in each entry of the dataset.
    -1 represent nil, and should be treated as padding_idx in embedding
    """
    tokens = d.tokenize(question, False)
    tokens = tokens[:max_length]
    if len(tokens) < max_length:
        # Note here we pad in front of the sentence
        padding = [d.padding_idx] * (max_length - len(tokens))
        tokens = tokens + padding
    utils.assert_eq(len(tokens), max_length)
    return tokens




def process_img(image):
    name = image.split('/')[-1]
    return imgs[img_id[name]]

def getResult(question,image):
    answer = {}
    with torch.no_grad():
        # tokenize q
        q = torch.from_numpy(np.array(tokenize(question))).type('torch.LongTensor').unsqueeze(0)
        # get image
        v = process_img(image).reshape(128*128)
        v = v.reshape(-1, 128, 128).unsqueeze(1)
        output = vqa_model(v,q)
        preds = vqa_model.classifier(output)
        acc,index = torch.topk(preds,5)
        acc = F.softmax(acc,1)
        acc = np.array(acc)[0]
        index = np.array(index)[0]
        for i in range(5):
            answer[label2ans[index[i]].title()]=acc[i]



    return answer
