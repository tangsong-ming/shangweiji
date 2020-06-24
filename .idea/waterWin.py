# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'waterWin.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowTitle('水域信息查询系统')
        Form.setWindowIcon(QtGui.QIcon('./images/fishicon.png'))
        window_pale = QtGui.QPalette()
        window_pale.setBrush(Form.backgroundRole(),
                             QtGui.QBrush(QtGui.QPixmap("./images/bgfish.jpg")))
        Form.setPalette(window_pale)

        Form.resize(945, 776)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(350, 40, 250, 51))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(73, 122, 260, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(550, 120, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(80, 190, 201, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(80, 280, 401, 371))
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(560, 280, 54, 12))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(80, 710, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 710, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.clicked.connect(Form.query)
        self.pushButton_2.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "水域信息查询系统"))
        self.label.setText(_translate("Form", "水域信息查询系统"))
        self.label_2.setText(_translate("Form", "请选择你想要查看的区域"))
        self.label_3.setText(_translate("Form", "水域分布区域图"))
        self.label_4.setText(_translate("Form", "水域图"))
        self.pushButton.setText(_translate("Form", "查询"))
        self.pushButton_2.setText(_translate("Form", "退出"))
        self.comboBox.setItemText(0, _translate("Form", "区域A"))
        self.comboBox.setItemText(1, _translate("Form", "区域B"))
        self.comboBox.setItemText(2, _translate("Form", "区域C"))
        self.comboBox.setItemText(3, _translate("Form", "区域D"))