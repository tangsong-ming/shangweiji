# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mood_prediction.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import QPainter,QPixmap
from PyQt5.QtCore import Qt
import pygame
import time
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report,confusion_matrix
import numpy as np
import pandas as pd

data = pd.read_csv('./src/trying.csv', sep=',')
x_data = data.iloc[:, :-2]
y_data = data.iloc[:, -2]
scaler = StandardScaler()
x_data = scaler.fit_transform(x_data)
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data,random_state=40)  # 分割数据1/4为测试数据，3/4为训练数据
mlp = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=500)
mlp.fit(x_train, y_train)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1051, 700)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 10, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        # self.label_8 = QtWidgets.QLabel(self.centralwidget)
        # self.label_8.setGeometry(QtCore.QRect(390, 10, 400, 400))
        #self.label_8.setObjectName("label_8")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 590, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 590, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 590, 131, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(660, 590, 131, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(60, 90, 161, 411))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_3.addWidget(self.lineEdit_4)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_3.addWidget(self.lineEdit_5)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_3.addWidget(self.lineEdit_6)

        intValidator1 = QIntValidator()
        intValidator1.setRange(0, 1)
        intValidator2 = QIntValidator()
        intValidator2.setRange(0, 10)
        self.lineEdit.setValidator(intValidator1)
        self.lineEdit.setMaxLength(2)
        self.lineEdit.setToolTip('请输入0或者1')
        self.lineEdit_2.setValidator(intValidator1)
        self.lineEdit_2.setMaxLength(2)
        self.lineEdit_2.setToolTip('请输入0或者1')
        self.lineEdit_3.setValidator(intValidator1)
        self.lineEdit_3.setMaxLength(2)
        self.lineEdit_3.setToolTip('请输入0或者1')
        self.lineEdit_4.setValidator(intValidator1)
        self.lineEdit_4.setMaxLength(2)
        self.lineEdit_4.setToolTip('请输入0或者1')
        self.lineEdit_5.setValidator(intValidator1)
        self.lineEdit_5.setMaxLength(2)
        self.lineEdit_5.setToolTip('请输入0或者1')
        self.lineEdit_6.setValidator(intValidator2)
        self.lineEdit_6.setToolTip('请输入0-10,此处并非为具体次数')
        # self.movie = QMovie('./images/1.gif')
        # self.label_8.setMovie(self.movie)
        # self.movie.start()
        ######我日
        MainWindow.setWindowIcon(QtGui.QIcon('./images/77.jpg'))

        window_pale = QtGui.QPalette()
        window_pale.setBrush(MainWindow.backgroundRole(),
                                 QtGui.QBrush(QtGui.QPixmap("./images/1212.jpg")))
        MainWindow.setPalette(window_pale)
        self.pushButton.clicked.connect(self.onClickedButton1)
        self.pushButton_2.clicked.connect(self.onClickedButton2)
        self.pushButton_4.clicked.connect(self.onClickedButton4)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.verticalLayout_3.addWidget(self.lineEdit_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1051, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def onClickedButton1(self):
        pygame.init()
        print("播放音乐1")
        track = pygame.mixer.music.load(r"./src/1.mp3")
        pygame.mixer.music.play()
        time.sleep(40)
        pygame.mixer.music.stop()
    def onClickedButton2(self):
        strrrr=str(self.a1)+','+str(self.a2)+','+str(self.a3)+','+\
               str(self.a4)+','+str(self.a5)+','+str(self.a6)+','+str(self.predictions[0])+','+'\n'
        with open('./src/trying.csv', 'a') as f:
            f.writelines(strrrr)
    def onClickedButton4(self):
        self.a1=int(self.lineEdit.text())
        self.a2 = int(self.lineEdit_2.text())
        self.a3 = int(self.lineEdit_3.text())
        self.a4 = int(self.lineEdit_4.text())
        self.a5 = int(self.lineEdit_5.text())
        self.a6 = int(self.lineEdit_6.text())
        self.aaa=[self.a1,self.a2,self.a3,self.a4,self.a5,self.a6]
        self.bbb=[self.aaa]
        self.predictions = mlp.predict(self.bbb)
        if self.predictions[0]==0:
            self.lineEdit_7.setText('她心情不好快去哄哄她吧')
            aaa=[]
        elif self.predictions[0]==1:
            self.lineEdit_7.setText('她心情还行，但是可能会生气')
            aaa=[]
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "要相信科学"))
        self.label.setText(_translate("MainWindow", "小张心情好坏预测软件"))
        #self.label_8.setText(_translate("MainWindow", "图片标签"))

        self.pushButton.setText(_translate("MainWindow", "BGM"))
        self.pushButton_2.setText(_translate("MainWindow", "提交数据到本地"))
        self.pushButton_3.setText(_translate("MainWindow", "本人使用该软件"))
        self.pushButton_4.setText(_translate("MainWindow", "他人使用该软件"))
        self.label_2.setText(_translate("MainWindow", "是否放下头发（0/1）"))
        self.label_3.setText(_translate("MainWindow", "是否主动与人交流"))
        self.label_4.setText(_translate("MainWindow", "是否长时间观看综艺"))
        self.label_5.setText(_translate("MainWindow", "是否外表看起来很down"))
        self.label_6.setText(_translate("MainWindow", "是否长时间观看论文"))
        self.label_7.setText(_translate("MainWindow", "微笑的次数（0-10）"))
        self.label_8.setText(_translate("MainWindow", "判断结果，请谨慎参考"))
        self.menu.setTitle(_translate("MainWindow", "彩蛋"))


