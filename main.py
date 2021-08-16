import json

from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import mainwindow

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
import os
from interface import VQAsignal



class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_layout.setSpacing(0)
        self.main_widget.setLayout(self.main_layout)

        self.left_widget = QtWidgets.QWidget()
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()
        self.left_widget.setLayout(self.left_layout)
        self.left_widget.setStyleSheet('''
            QWidget#left_widget{
                background:gray;
                border-top:1px solid white;
                border-bottom:1px solid white;
                border-left:1px solid white;
                border-top-left-radius:10px;
                border-bottom-left-radius:10px;
            }
            QLabel#left_label{
                color: white;
                border:none;
                font-size:14px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
            QRadioButton{
                color: white;
            }
        ''')
        self.right_widget = QtWidgets.QWidget()
        self.right_widget.setObjectName('right_widget')
        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)
        self.setCentralWidget(self.main_widget)

        #left pannel
        self.left_close = QtWidgets.QPushButton("")
        self.left_visit = QtWidgets.QPushButton("")
        self.left_mini = QtWidgets.QPushButton("")
        self.left_close.setFixedSize(15, 15)
        self.left_visit.setFixedSize(15, 15)
        self.left_mini.setFixedSize(15, 15)
        self.left_close.clicked.connect(self.close)
        self.left_close.setStyleSheet(
            '''QPushButton{background:red;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#f0f0f0;border-radius:5px;}QPushButton:hover{background:#f0f0f0;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#f0f0f0;border-radius:5px;}QPushButton:hover{background:#f0f0f0;}''')

        self.left_label_1 = QtWidgets.QPushButton("Med - VQA")
        self.left_label_1.setObjectName('left_label')
        #Med-VQA can answer questions you ask about an image
        self.left_text_1 = QtWidgets.QLabel('    This system can \nanswer questions you \n       ask about a \n   radiology image!')
        self.left_text_1.setObjectName('left_label')



        self.left_label_2 = QtWidgets.QPushButton("Dataset Choice")
        self.left_label_2.setObjectName('left_label')
        self.radio_button1 = QtWidgets.QRadioButton("VQA-RAD (2018)")
        self.radio_button1.setChecked(True)
        # self.radio_button2 = QtWidgets.QRadioButton("SLAKE (Ours)")
        self.radio_button1.toggled.connect(self.dataset_choice)
        # self.radio_button2.toggled.connect(self.dataset_choice)

        self.radio_button_group = QtWidgets.QButtonGroup(self)
        self.radio_button_group.addButton(self.radio_button1)
        # self.radio_button_group.addButton(self.radio_button2)

        self.left_label_3 = QtWidgets.QPushButton("Model Choice")
        self.left_label_3.setObjectName('left_label')
        # self.radio_button3 = QtWidgets.QRadioButton("MEVF (2019)")
        self.radio_button4 = QtWidgets.QRadioButton("CPRD (Ours)")
        self.radio_button4.setChecked(True)
        # self.radio_button3.toggled.connect(self.model_choice)
        self.radio_button4.toggled.connect(self.model_choice)
        self.radio_button_group2 = QtWidgets.QButtonGroup(self)
        # self.radio_button_group2.addButton(self.radio_button3)
        self.radio_button_group2.addButton(self.radio_button4)

        self.left_team = QtWidgets.QPushButton("Team")
        self.left_team.setObjectName('left_label')
        #XMLab
        # Copyright ©2020 All Rights Reserved The Department of Computing
        # The Hong Kong Polytechnic University
        self.left_team_1 = QtWidgets.QPushButton(qtawesome.icon('fa.television', color='white'),"XMLAB@Comp")
        self.left_team_1.setObjectName('left_button')
        self.left_team_2 = QtWidgets.QPushButton(qtawesome.icon('fa.map-marker', color='white'),"PolyU,HK")
        self.left_team_2.setObjectName('left_button')
        self.left_team_3 = QtWidgets.QPushButton(qtawesome.icon('fa.copyright', color='white'),"Copyright©2020")
        self.left_team_3.setObjectName('left_button')

        self.left_team_4 = QtWidgets.QPushButton("")
        self.left_team_4.setObjectName('left_button')
        self.left_team_5 = QtWidgets.QPushButton("")
        self.left_team_5.setObjectName('left_button')
        self.left_team_6 = QtWidgets.QPushButton("")
        self.left_team_6.setObjectName('left_button')
        self.left_team_7 = QtWidgets.QPushButton("")
        self.left_team_7.setObjectName('left_button')
        self.left_team_8 = QtWidgets.QPushButton("")
        self.left_team_8.setObjectName('left_button')

        self.left_question = QtWidgets.QPushButton("Feedback")
        self.left_question.setObjectName('left_label')
        self.left_problem_1 = QtWidgets.QPushButton(qtawesome.icon('fa.envelope', color='white'), "Email")
        self.left_problem_1.setObjectName('left_button')
        self.left_problem_2 = QtWidgets.QPushButton(qtawesome.icon('fa.mobile', color='white'), "Telephone")
        self.left_problem_2.setObjectName('left_button')


        self.left_layout.addWidget(self.left_close, 0, 0, 1, 1)
        # self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        # self.left_layout.addWidget(self.left_mini, 0, 2, 1, 1)



        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_text_1 , 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 4, 0, 1, 3)

        self.left_layout.addWidget(self.radio_button1, 5, 0, 1, 3)
        # self.left_layout.addWidget(self.radio_button2, 6, 0, 1, 3)

        self.left_layout.addWidget(self.left_label_3, 7, 0, 1, 3)
        # self.left_layout.addWidget(self.radio_button3, 8, 0, 1, 3)
        self.left_layout.addWidget(self.radio_button4, 9, 0, 1, 3)

        self.left_layout.addWidget(self.left_team, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_team_1, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_team_2, 12, 0, 1, 3)
        self.left_layout.addWidget(self.left_team_3, 13, 0, 1, 3)

        self.left_layout.addWidget(self.left_question,14,0,1,3)
        self.left_layout.addWidget(self.left_problem_1, 15, 0, 1, 3)
        self.left_layout.addWidget(self.left_problem_2, 16, 0, 1, 3)

        self.left_layout.addWidget(self.left_team_4, 17, 0, 1, 3)
        self.left_layout.addWidget(self.left_team_5, 18, 0, 1, 3)
        self.left_layout.addWidget(self.left_team_6, 19, 0, 1, 3)
        self.left_layout.addWidget(self.left_team_7, 20, 0, 1, 3)


        # right panel
        self.right_gallery_label = QtWidgets.QLabel("Dataset Visual Gallery")
        self.right_gallery_label.setObjectName('right_lable')
        self.right_gallery_widght = QtWidgets.QWidget()
        self.right_gallery_widght.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
                QPushButton{border:none;}
            ''')
        self.right_gallery_layout = QtWidgets.QGridLayout()
        self.right_gallery_widght.setLayout(self.right_gallery_layout)

        self.gallery_pic_1 = QtWidgets.QToolButton()
        # self.gallery_pic_1.setIcon(QtGui.QIcon('./images/synpic676.jpg'))
        self.gallery_pic_1.setIconSize(QtCore.QSize(100, 100))
        self.gallery_pic_1.clicked.connect(lambda: self.tb_action_slot(1))


        self.gallery_pic_2 = QtWidgets.QToolButton()
        # self.gallery_pic_2.setIcon(QtGui.QIcon('./images/synpic676.jpg'))
        self.gallery_pic_2.setIconSize(QtCore.QSize(100, 100))
        self.gallery_pic_2.clicked.connect(lambda: self.tb_action_slot(2))
        # self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.gallery_pic_3 = QtWidgets.QToolButton()
        # self.gallery_pic_3.setIcon(QtGui.QIcon('./images/synpic676.jpg'))
        self.gallery_pic_3.setIconSize(QtCore.QSize(100, 100))
        self.gallery_pic_3.clicked.connect(lambda: self.tb_action_slot(3))
        # self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.gallery_pic_4 = QtWidgets.QToolButton()
        # self.gallery_pic_4.setIcon(QtGui.QIcon('./images/synpic676.jpg'))
        self.gallery_pic_4.setIconSize(QtCore.QSize(100, 100))
        self.gallery_pic_4.clicked.connect(lambda: self.tb_action_slot(4))
        # self.recommend_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.gallery_pic_5 = QtWidgets.QToolButton()
        # self.gallery_pic_5.setIcon(QtGui.QIcon('./images/synpic676.jpg'))
        self.gallery_pic_5.setIconSize(QtCore.QSize(100, 100))
        self.gallery_pic_5.clicked.connect(lambda: self.tb_action_slot(5))
        # self.recommend_button_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.gallery_pic_6 = QtWidgets.QToolButton()
        # self.gallery_pic_6.setIcon(QtGui.QIcon('./images/synpic676.jpg'))  # 设置按钮图标
        self.gallery_pic_6.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
        self.gallery_pic_6.clicked.connect(lambda: self.tb_action_slot(6))
        # self.recommend_button_6.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文

        self.gallery_pic_7 = QtWidgets.QToolButton()
        # self.gallery_pic_7.setIcon(QtGui.QIcon('./images/synpic676.jpg'))
        self.gallery_pic_7.setIconSize(QtCore.QSize(100, 100))
        self.gallery_pic_7.clicked.connect(lambda: self.tb_action_slot(7))
        # self.recommend_button_7.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.gallery_pic_8 = QtWidgets.QToolButton()
        # self.gallery_pic_8.setIcon(QtGui.QIcon('./images/synpic676.jpg'))
        self.gallery_pic_8.setIconSize(QtCore.QSize(100, 100))
        self.gallery_pic_8.clicked.connect(lambda: self.tb_action_slot(8))


        self.gallery_pic_9 = QtWidgets.QToolButton()
        # self.gallery_pic_9.setIcon(QtGui.QIcon('./images/synpic676.jpg'))
        self.gallery_pic_9.setIconSize(QtCore.QSize(100, 100))
        self.gallery_pic_9.clicked.connect(lambda: self.tb_action_slot(9))
        # self.recommend_button_9.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)

        self.gallery_pic_10 = QtWidgets.QToolButton()
        # self.gallery_pic_10.setIcon(QtGui.QIcon('./images/synpic676.jpg'))
        self.gallery_pic_10.setIconSize(QtCore.QSize(100, 100))
        self.gallery_pic_10.clicked.connect(lambda: self.tb_action_slot(10))
        self.gallery = [self.gallery_pic_1,self.gallery_pic_2,self.gallery_pic_3,self.gallery_pic_4,
                        self.gallery_pic_5,self.gallery_pic_6,self.gallery_pic_7,self.gallery_pic_8,
                        self.gallery_pic_9,self.gallery_pic_10]
        self.gallery_path = []
        self.ptr = 0

        # self.recommend_button_10.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.backward', color='#F76677'), "")
        self.button_1.clicked.connect(lambda: self.bt_action_slot(1))
        self.button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.forward', color='#F76677'), "")
        self.button_2.clicked.connect(lambda: self.bt_action_slot(2))

        self.right_gallery_layout.addWidget(self.button_1,0,0,2,1)
        self.button_1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.right_gallery_layout.addWidget(self.gallery_pic_1, 0, 1)
        self.right_gallery_layout.addWidget(self.gallery_pic_2, 0, 2)
        self.right_gallery_layout.addWidget(self.gallery_pic_3, 0, 3)
        self.right_gallery_layout.addWidget(self.gallery_pic_4, 0, 4)
        self.right_gallery_layout.addWidget(self.gallery_pic_5, 0, 5)

        self.right_gallery_layout.addWidget(self.gallery_pic_6, 1, 1)
        self.right_gallery_layout.addWidget(self.gallery_pic_7, 1, 2)
        self.right_gallery_layout.addWidget(self.gallery_pic_8, 1, 3)
        self.right_gallery_layout.addWidget(self.gallery_pic_9, 1, 4)
        self.right_gallery_layout.addWidget(self.gallery_pic_10, 1, 5)

        self.right_gallery_layout.addWidget(self.button_2, 0, 6, 2, 1)
        self.button_2.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

        self.right_layout.addWidget(self.right_gallery_label, 0, 0, 1, 9)
        self.right_layout.addWidget(self.right_gallery_widght, 1, 0, 2, 9)

        #Selected Radiology Images
        self.right_selected_lable = QtWidgets.QLabel("Selected Radiology Images")
        self.right_selected_lable.setObjectName('right_lable')

        self.right_selected_widget = QtWidgets.QWidget()
        self.right_selected_widget.setStyleSheet('''
            QPushButton{
                border:none;
                color:gray;
                font-size:12px;
                height:40px;
                padding-left:5px;
                padding-right:10px;
                text-align:left;
            }
            QPushButton:hover{
                color:black;
                border:1px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
            }
        ''')
        self.right_selected_layout = QtWidgets.QGridLayout()
        self.right_selected_widget.setLayout(self.right_selected_layout)

        self.select_image = QtWidgets.QLabel("")
        self.select_image_path = None
        pic = QtGui.QPixmap('./images/blank.jpg')
        self.select_image.setPixmap(pic)
        self.select_image.setScaledContents(True)  # 图片自适应LABEL大小
        self.right_selected_layout.addWidget(self.select_image, 0, 1)

        # select questions
        self.right_question_lable = QtWidgets.QLabel("Input Questions")
        self.right_question_lable.setObjectName('right_lable')
        self.right_question_widget = QtWidgets.QWidget()
        self.right_question_layout = QtWidgets.QGridLayout()
        self.right_question_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
                QProgressBar {   border: 1px  solid grey;   border-radius: 5px;   background-color: #FFFFFF;text-align: center;}
                QProgressBar::chunk {   background-color: #F76677;   width: 10px;}
            ''')
        self.right_question_widget.setLayout(self.right_question_layout)

        self.input_edit =QtWidgets.QComboBox()
        self.input_edit.currentIndexChanged.connect(self.comboChange)
        self.input_edit.currentTextChanged.connect(self.comboTextChange)
        # self.input_edit.setPlaceholderText("Enter the question ")
        self.input_edit.setEditable(True)
        # self.input_edit.currentIndexChanged.connect(self.selectionchange)


        self.submit = QtWidgets.QPushButton('Submit')
        self.submit.clicked.connect(self.submit_slot)
        self.question_id = 0


        # self.pushButton_3.setGraphicsEffect(op)

        self.answer1 = QtWidgets.QLabel('')
        self.right_process_bar1 = QtWidgets.QProgressBar()
        self.right_process_bar1.setVisible(False)
        # self.op1 = QtWidgets.QGraphicsOpacityEffect()
        # self.op1.setOpacity(0)
        # self.right_process_bar1.setGraphicsEffect(self.op1)


        self.answer2 = QtWidgets.QLabel('')
        self.right_process_bar2 = QtWidgets.QProgressBar()
        self.right_process_bar2.setValue(10)
        self.right_process_bar2.setVisible(False)
        # op2 = QtWidgets.QGraphicsOpacityEffect()
        # op2.setOpacity(0)
        # self.right_process_bar2.setGraphicsEffect(op2)

        self.answer3 = QtWidgets.QLabel('')
        self.right_process_bar3 = QtWidgets.QProgressBar()
        self.right_process_bar3.setValue(40)
        self.right_process_bar3.setVisible(False)
        # op3 = QtWidgets.QGraphicsOpacityEffect()
        # op3.setOpacity(0)
        # self.right_process_bar3.setGraphicsEffect(op3)

        self.answer4 = QtWidgets.QLabel('')
        self.right_process_bar4 = QtWidgets.QProgressBar()
        self.right_process_bar4.setValue(30)
        self.right_process_bar4.setVisible(False)
        # op4 = QtWidgets.QGraphicsOpacityEffect()
        # op4.setOpacity(0)
        # self.right_process_bar4.setGraphicsEffect(op4)

        self.answer5 = QtWidgets.QLabel('')
        self.right_process_bar5 = QtWidgets.QProgressBar()
        self.right_process_bar5.setValue(20)
        self.right_process_bar5.setVisible(False)
        # op5 = QtWidgets.QGraphicsOpacityEffect()
        # op5.setOpacity(0)
        # self.right_process_bar5.setGraphicsEffect(op5)

        # self.answer6 = QtWidgets.QLabel('Ground Truth:')
        self.answer7 = QtWidgets.QLabel('')


        # self.right_question_layout.addWidget(self.answer6, 0, 0, 1, 1)
        # self.right_question_layout.addWidget(self.answer7, 0, 2, 1, 1)

        self.right_question_layout.addWidget(self.input_edit,1,0,1,5)
        self.right_question_layout.addWidget(self.answer7,1,5,1,2)
        self.right_question_layout.addWidget(self.submit, 1, 7, 1, 1)

        # self.right_question_layout.addWidget(self.answer6, 1, 0, 1, 1)
        # self.right_question_layout.addWidget(self.answer7, 1, 2, 1, 5)

        self.right_question_layout.addWidget(self.answer1, 2, 0, 1, 2)
        self.right_question_layout.addWidget(self.right_process_bar1, 2, 2, 1, 6)

        self.right_question_layout.addWidget(self.answer2, 3, 0, 1, 2)
        self.right_question_layout.addWidget(self.right_process_bar2, 3, 2, 1, 6)

        self.right_question_layout.addWidget(self.answer3, 4, 0, 1, 2)
        self.right_question_layout.addWidget(self.right_process_bar3, 4, 2, 1, 6)

        self.right_question_layout.addWidget(self.answer4, 5, 0, 1, 2)
        self.right_question_layout.addWidget(self.right_process_bar4, 5, 2, 1, 6)

        self.right_question_layout.addWidget(self.answer5, 6, 0, 1, 2)
        self.right_question_layout.addWidget(self.right_process_bar5, 6, 2, 1, 6)




        self.right_layout.addWidget(self.right_selected_lable, 4, 0, 1, 3)
        self.right_layout.addWidget(self.right_selected_widget, 5, 0, 1, 3)

        self.right_layout.addWidget(self.right_question_lable, 4, 3, 1, 7)
        self.right_layout.addWidget(self.right_question_widget, 5, 3, 1, 7)


        self.setWindowOpacity(1)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        # initial images
        self.combo_idx = 0
        self.comboTextlabel = 0
        self.img_ques_ans = {}
        self.show_gallery(0)


    def tb_action_slot(self,id):
        if id > len(self.gallery_path):
            return
        # show selected img
        pic = QtGui.QPixmap(self.gallery_path[id-1])
        self.select_image_path = self.gallery_path[id-1]
        self.select_image.setPixmap(pic)

        # shown combo questions
        img_name = self.select_image_path.split('/')[-1]
        self.input_edit.clear()
        self.input_edit.addItems(self.img_ques_ans[img_name][0])


    def comboChange(self,id):
        self.combo_idx = id
        self.comboTextlabel = 0

    def set_icon(self,images):
        for id,image in enumerate(images):
            self.gallery[id].setIcon(QtGui.QIcon(image))

    def show_gallery(self,n):
        # n 0: vqa_rad 1: slake
        image_set = './images/slake' if n else './images/vqa_rad'
        questions = json.load(open('./vqa/data/rad/testset.json', 'r')) + json.load(open('./vqa/data/rad/testset.json', 'r'))[:400]

        for i in questions:
            name = i['image_name']
            question = i['question']
            answer = i['answer']


            if name not in self.img_ques_ans:
                self.img_ques_ans[name] = [[],[]]
            self.img_ques_ans[name][0].append(question)
            self.img_ques_ans[name][1].append(answer)

        sorted(self.img_ques_ans.items(), key=lambda d: len(d[1]))

        images = [os.path.join(image_set,i) for i in self.img_ques_ans.keys()]
        interval = 10
        self.gallery_path = images[:interval]
        self.set_icon(images[:interval])
        self.images = images

    def dataset_choice(self):
        if self.radio_button1.isChecked():
            self.show_gallery(0)
        # if self.radio_button2.isChecked():
        #     self.show_gallery(1)

    def model_choice(self):
        if self.radio_button4.isChecked():
            print('b')

    def bt_action_slot(self,n):
        self.ptr += -1 if n==1 else 1
        start = self.ptr*10
        end = start+10 if start < len(self.images)-10 else len(self.images)
        self.gallery_path = self.images[start:end]
        self.set_icon(self.gallery_path)

    def comboTextChange(self):
        self.comboTextlabel = 1

    def submit_slot(self):
        question = self.input_edit.currentText()
        if len(question)==0 or question.isspace():
            return
        if self.select_image_path == None:
            return

        # set gt
        name = self.select_image_path.split('/')[-1]
        if self.comboTextlabel:
            show = ''
        else:
            show = self.img_ques_ans[name][1][self.combo_idx]

        if len(show)>12:
            show = show[:12]+'..'

        self.answer7.setText(show)
        self.answer7.repaint()

        # signal register
        thread = VQAsignal(self,question=question,image=self.select_image_path)
        # return signal, and show results
        thread.breakSignal.connect(self.show_result)
        # signal start
        thread.start()

    def show_result(self,answer):

        name = list(answer.keys())
        for i in range(5):
            if len(name[i])>23:
                name[i] = name[i][:23]+"..."
        acc = list(answer.values())

        self.answer1.setText(name[0])
        self.right_process_bar1.setMaximum(100 * 100)
        value = round(acc[0],2)*100
        self.right_process_bar1.setValue(value*100)
        self.right_process_bar1.setVisible(True)
        self.right_process_bar1.setFormat("%.02f %%" % value)


        self.answer2.setText(name[1])
        self.right_process_bar2.setMaximum(100 * 100)
        value = round(acc[1], 2) * 100
        self.right_process_bar2.setValue(value * 100)
        self.right_process_bar2.setVisible(True)
        self.right_process_bar2.setFormat("%.02f %%" % value)


        self.answer3.setText(name[2])
        self.right_process_bar3.setMaximum(100 * 100)
        value = round(acc[2], 2) * 100
        self.right_process_bar3.setValue(value * 100)
        self.right_process_bar3.setVisible(True)
        self.right_process_bar3.setFormat("%.02f %%" % value)


        self.answer4.setText(name[3])
        self.right_process_bar4.setMaximum(100 * 100)
        value = round(acc[3],2)*100
        self.right_process_bar4.setValue(value*100)
        self.right_process_bar4.setVisible(True)
        self.right_process_bar4.setFormat("%.02f %%" % value)


        self.answer5.setText(name[4])
        self.right_process_bar5.setMaximum(100 * 100)
        value = round(acc[4],2)*100
        self.right_process_bar5.setValue(value*100)
        self.right_process_bar5.setVisible(True)
        self.right_process_bar5.setFormat("%.02f %%" % value)








class blankDialogue(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setGeometry(300,260,840,420)
        self.main_widget = QtWidgets.QWidget()
        self.main_layout = QtWidgets.QGridLayout()
        self.main_layout.setSpacing(0)
        self.main_widget.setLayout(self.main_layout)
        palette1 = QtGui.QPalette()
        palette1.setColor(self.backgroundRole(), QtGui.QColor(255, 255, 255))
        self.setPalette(palette1)
        self.setWindowOpacity(1)
        label = QtWidgets.QLabel('xxx')
        self.main_layout.addWidget(label,0,0)




def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    # dialogue = blankDialogue()
    # gui.radio_button2.toggled.connect(dialogue.show)
    gui.show()
    app.exec_()
    sys.exit()


if __name__ == '__main__':
    main()
