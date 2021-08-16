# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         vqa
# Description:  BAN vqa [Bilinear attention + Bilinear residual network]
# Author:       Boliu.Kelvin
# Date:         2020/4/7
# -------------------------------------------------------------------------------
import torch
import torch.nn as nn
from language_model import WordEmbedding, QuestionEmbedding
from classifier import SimpleClassifier
from connect import FCNet
from connect import BCNet
from counting import Counter
from utils import tfidf_loading
from torch.nn.utils.weight_norm import weight_norm
from resnet import resnet8


# Bilinear Attention
class BiAttention(nn.Module):
    def __init__(self, x_dim, y_dim, z_dim, glimpse, dropout=[.2, .5]):  # 128, 1024, 1024,2
        super(BiAttention, self).__init__()

        self.glimpse = glimpse
        self.logits = weight_norm(BCNet(x_dim, y_dim, z_dim, glimpse, dropout=dropout, k=3),
                                  name='h_mat', dim=None)

    def forward(self, v, q, v_mask=True):  # v:32,1,128; q:32,12,1024
        """
        v: [batch, k, vdim]
        q: [batch, qdim]
        """
        v_num = v.size(1)
        q_num = q.size(1)
        logits = self.logits(v, q)  # b x g x v x q

        if v_mask:
            mask = (0 == v.abs().sum(2)).unsqueeze(1).unsqueeze(3).expand(logits.size())
            logits.data.masked_fill_(mask.data, -float('inf'))

        p = nn.functional.softmax(logits.view(-1, self.glimpse, v_num * q_num), 2)
        return p.view(-1, self.glimpse, v_num, q_num), logits


class BiResNet(nn.Module):
    def __init__(self, args, priotize_using_counter=False):
        super(BiResNet, self).__init__()
        # Optional module: counter
        use_counter = args.use_counter if priotize_using_counter is None else priotize_using_counter
        if use_counter or priotize_using_counter:
            objects = 10  # minimum number of boxes
        if use_counter or priotize_using_counter:
            counter = Counter(objects)
        else:
            counter = None
        # # init Bilinear residual network
        b_net = []  # bilinear connect :  (XTU)T A (YTV)
        q_prj = []  # output of bilinear connect + original question-> new question    Wq_ +q
        c_prj = []
        for i in range(args.glimpse):
            b_net.append(BCNet(args.v_dim, args.hid_dim, args.hid_dim, None, k=1))
            q_prj.append(FCNet([args.hid_dim, args.hid_dim], '', .2))
            if use_counter or priotize_using_counter:
                c_prj.append(FCNet([objects + 1, args.hid_dim], 'ReLU', .0))

        self.b_net = nn.ModuleList(b_net)
        self.q_prj = nn.ModuleList(q_prj)
        self.c_prj = nn.ModuleList(c_prj)
        self.args = args

    def forward(self, v_emb, q_emb, att_p):
        b_emb = [0] * self.args.glimpse
        for g in range(self.args.glimpse):
            b_emb[g] = self.b_net[g].forward_with_weights(v_emb, q_emb, att_p[:, g, :, :])  # b x l x h
            # atten, _ = logits[:,g,:,:].max(2)
            q_emb = self.q_prj[g](b_emb[g].unsqueeze(1)) + q_emb
        return q_emb.sum(1)


# Create BAN vqa
class BAN_Model(nn.Module):
    def __init__(self, dictionary, args,num_ans_candidates):
        super(BAN_Model, self).__init__()

        self.args = args
        # init word embedding module, question embedding module, biAttention network, bi_residual network, and classifier
        self.w_emb = WordEmbedding(dictionary.ntoken, 300, .0, args.cat)
        self.q_emb = QuestionEmbedding(600 if args.cat else 300, args.hid_dim, 1, False, .0, args.rnn)
        self.bi_att = BiAttention(args.v_dim, args.hid_dim, args.hid_dim, args.glimpse)
        self.bi_resnet = BiResNet(args)
        self.classifier = SimpleClassifier(args.hid_dim, args.hid_dim * 2, num_ans_candidates, args)

        # Loading tfidf weighted embedding
        if hasattr(args, 'tfidf'):
            self.w_emb = tfidf_loading(args.tfidf, self.w_emb, args)

        model = resnet8(num_classes=3)
        fc1 = nn.Linear(256,128)
        fc1.weight.data.normal_(mean=0.0, std=0.01)
        fc1.bias.data.zero_()
        bn = nn.BatchNorm1d(num_features=128, eps=1e-5, affine=True, momentum=0.05)
        self.fc = fc1
        self.bn = bn
        self.other = model


    def forward(self, v, q):
        """Forward
        v: [batch, num_objs, obj_dim]
        b: [batch, num_objs, b_dim]
        q: [batch_size, seq_length]
        return: logits, not probs
        """
        # get visual feature
        v_input = v.expand(-1, 3, -1, -1)
        output,_ = self.other(v_input,is_feat=True)
        fc = self.fc(output[-1])
        bn = self.bn(fc)
        v_emb = bn.unsqueeze(1)

        # get lextual feature
        w_emb = self.w_emb(q)
        # Attention

        q_emb = self.q_emb.forward_all(w_emb)  # [batch, q_len, q_dim]
        att_p, logits = self.bi_att(v_emb, q_emb)  # b x g x v x q
        # bilinear residual network
        last_output = self.bi_resnet(v_emb, q_emb, att_p)
        return last_output

    def classify(self, input_feats):
        return self.classifier(input_feats)

