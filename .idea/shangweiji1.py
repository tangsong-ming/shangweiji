# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shangweiji1.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from shangweiji2 import theSecond
import serial
import serial.tools.list_ports
import pypyodbc
import pyqtgraph as pg
from datetime import datetime as dt
def access_insert(temp,ph,zhuodu,ddl,real_time):
    path = r'C:\Users\VULCAN\Desktop\ten\acc1.accdb'  # 数据库文件
    strr = 'Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ=' + (path)
    db = pypyodbc.win_connect_mdb(strr)
    curser = db.cursor()
    try:
        curser.execute("CREATE TABLE [sensors] (temp varchar(50) , ph varchar(50) , zhuodu varchar(50),ddl varchar(50),real_time varchar(50)  )")
    except:
        pass
    curser.execute('''INSERT INTO [sensors] VALUES('{} ','{}','{}','{}','{}')'''.format(temp,ph,zhuodu,ddl,real_time))

    curser.commit()
    # 关闭句柄
    curser.close()
    db.close()

class Ui_Form(object):
    def __init__(self):
        super().__init__()
        self.flag = 1
        plist = list(serial.tools.list_ports.comports())

        if len(plist) <= 0:
            print("The Serial port can't find!")
        else:
            # print(plist)
            plist_0 = list(plist[0])
            plist_1 = list(plist[1])
            self.serialName = plist_0[0]
            self.serialName_1 = plist_1[0]
            # serialFd = serial.Serial(serialName, 115200)
            # print("check which port was really used >", serialFd.name)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1712, 906)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 81, 41))
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(30, 80, 291, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.onClickedButton1)
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 81, 41))
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(30, 170, 291, 111))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 2, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 2, 3, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(110, 130, 91, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(40, 300, 91, 31))
        self.label_7.setObjectName("label_7")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(30, 350, 440, 201))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 1, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 3, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 0, 4, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 0, 2, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 1, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.gridLayout_2.addWidget(self.label_11, 1, 3, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 0, 5, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 1, 4, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.gridLayoutWidget_2)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 1, 5, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(Form)
        self.pushButton_11.setGeometry(QtCore.QRect(40, 590, 75, 31))
        self.pushButton_11.setObjectName("pushButton_11")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(500, 40, 581, 821))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(1129, 39, 531, 821))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QVBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_12 = QtWidgets.QPushButton(Form)
        self.pushButton_12.setGeometry(QtCore.QRect(350, 590, 75, 31))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_2.clicked.connect(self.onClickedButton2)
        self.pushButton_3.clicked.connect(self.onClickedButton3)
        self.pushButton_4.clicked.connect(self.onClickedButton4)
        self.pushButton_5.clicked.connect(self.onClickedButton5)
        self.pushButton_6.clicked.connect(self.onClickedButton6)
        self.pushButton_7.clicked.connect(self.onClickedButton7)
        self.pushButton_8.clicked.connect(self.onClickedButton8)
        self.pushButton_9.clicked.connect(self.onClickedButton9)
        self.pushButton_10.clicked.connect(self.onClickedButton10)
        self.pushButton_11.clicked.connect(self.onClickedButton11)
        self.pushButton_12.clicked.connect(self.onClickedButton12)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "串口通信"))
        self.pushButton.setText(_translate("Form", "打开串口"))
        self.pushButton_2.setText(_translate("Form", "关闭串口"))
        self.label_2.setText(_translate("Form", "选择节点"))
        self.label_3.setText(_translate("Form", "温度"))
        self.label_4.setText(_translate("Form", "PH值"))
        self.label_5.setText(_translate("Form", "浊度"))
        self.label_6.setText(_translate("Form", "导电率"))
        self.label_7.setText(_translate("Form", "设备控制模块"))
        self.label_9.setText(_translate("Form", "设备3"))
        self.label_10.setText(_translate("Form", "设备一"))
        self.label_8.setText(_translate("Form", "设备二"))
        self.pushButton_7.setText(_translate("Form", "开"))
        self.pushButton_3.setText(_translate("Form", "开"))
        self.pushButton_4.setText(_translate("Form", "关"))
        self.pushButton_5.setText(_translate("Form", "开"))
        self.pushButton_6.setText(_translate("Form", "关"))
        self.label_11.setText(_translate("Form", "设备四"))
        self.pushButton_8.setText(_translate("Form", "关"))
        self.pushButton_9.setText(_translate("Form", "开"))
        self.pushButton_10.setText(_translate("Form", "关"))
        self.pushButton_11.setText(_translate("Form", "数据库查询"))
        self.pushButton_12.setText(_translate("Form", "图表显示"))
        self.comboBox.setItemText(0, _translate("Form", "{}".format(self.serialName)))
        self.comboBox.setItemText(1, _translate("Form", "{}").format(self.serialName_1))
        self.comboBox_2.setItemText(0, _translate("Form", "节点1"))
        self.comboBox_2.setItemText(1, _translate("Form", "节点2"))
        self.comboBox_2.setItemText(2, _translate("Form", "节点3"))
        self.comboBox_2.setItemText(3, _translate("Form", "节点4"))
        self.comboBox_2.setItemText(4, _translate("Form", "节点5"))
        self.comboBox_2.setItemText(5, _translate("Form", "节点6"))
        self.comboBox_2.setItemText(6, _translate("Form", "节点7"))
        self.comboBox_2.setItemText(7, _translate("Form", "节点8"))
    def onClickedButton1(self):
        if self.comboBox.currentText==self.serialName:
            self.serialFd = serial.Serial(self.serialName, 115200)
            print("check which port was really used >", self.serialFd.name)
        elif self.comboBox.currentText==self.serialName_1:
            self.serialFd = serial.Serial(self.serialName_1, 115200)
            print("check which port was really used >", self.serialFd.name)
        else:
            print('error')
        try:
            while True:
                real_time = dt.now()
                y1 = self.serialFd.read(9)
                if self.serialFd.is_open:
                    if (len(y1) == 9) & (y1[0] == 0x9a) & (y1[8] == 0xff):
                        temp0 = y1[5]
                        temp = str(temp0) + '度'  ######
                        phadc = y1[3] + (y1[4] << 8)
                        phvol = phadc * (3.3 / 4096)
                        ph = 22.255 - 5.9647 * phvol
                        fph = float(ph)
                        if (phadc != 0):
                            fph = str(fph)  #######
                        RES2 = 820.0
                        ECREF = 200.0
                        kValue = 1.0
                        kValue_Low = 1.0
                        kValue_High = 1.0
                        EC_value = 0.0
                        compensationCoefficient = 1.0
                        ddl = y1[1] + (y1[2] << 8)
                        EC_voltage = ddl / 4096 * 3300
                        rawEC = 1000 * EC_voltage / RES2 / ECREF
                        EC_valueTemp = rawEC * kValue
                        if (EC_valueTemp > 2.0):
                            kValue = kValue_High
                        elif (EC_valueTemp <= 2.0):
                            kValue = kValue_Low
                        EC_value = rawEC * kValue
                        compensationCoefficient = 1.0 + 0.0185 * ((temp0 / 10) - 25.0)
                        EC_value = EC_value / compensationCoefficient
                        if EC_value <= 0:
                            EC_value = 0
                        if EC_value > 20:
                            EC_value = 20
                        EC_value = float(EC_value)
                        if (ddl != 0):
                            EC_value = str(EC_value) + "mS/cm"  ####
                        K_Value = 3047.19
                        zhuodu = y1[6] + (y1[7] << 8)
                        TU = zhuodu * 3.3 / 4096
                        TU_calibration = -0.0192 * (temp0 / 10 - 25) + TU
                        TU_value = (-865.68 * TU_calibration + K_Value)
                        if (TU_value <= 175):
                            TU_value = 0
                        if (TU_value >= 3000):
                            TU_value = 3000
                        if zhuodu != 0:
                            zhuodu = str(zhuodu) + 'NTU'
                        if (phadc != 0) | (ddl != 0) | (zhuodu != 0):
                            access_insert(temp, ph, zhuodu, ddl, real_time)
                        print(temp, ddl, ph, zhuodu)
                        self.lineEdit.setText(''.format(temp))
                        self.lineEdit_2.setText(''.format(ph))
                        self.lineEdit_2.setText(''.format(zhuodu))
                        self.lineEdit_2.setText(''.format(ddl))
        except:
            pass
    def onClickedButton2(self):
        try:
            if self.serialFd.is_open:
                self.serialFd.close()
        except:
            pass
    def onClickedButton3(self):
        try:
            serialFd.write(b'\x01\x00\x01\xff')  # green
        except:
            pass
    def onClickedButton5(self):
        try:
            serialFd.write(b'\x01\x01\x00\xff')  # yellow
        except:
            pass
    def onClickedButton7(self):
        try:
            serialFd.write(b'\x02\x00\x01\xff')  # red
        except:
            pass
    def onClickedButton9(self):
        try:
            serialFd.write(b'\x02\x01\x00\xff')  # blue
        except:
            pass
    def onClickedButton4(self):
        try:
            serialFd.write(b'\x01\x01\x01\xff')  # green
        except:
            pass
    def onClickedButton6(self):
        try:
            serialFd.write(b'\x01\x01\x01\xff')  # yellow
        except:
            pass
    def onClickedButton8(self):
        try:
            serialFd.write(b'\x02\x01\x01\xff')  # red
        except:
            pass
    def onClickedButton10(self):
        try:
            serialFd.write(b'\x02\x01\x01\xff')  # blue
        except:
            pass
    def onClickedButton11(self):

        thesecond = theSecond()
        result = thesecond.exec()

    def onClickedButton12(self):
        # self.flag=1

        if self.flag==1:
            import pandas as pd
            data=[25,25,27,32,33,25,17,26,28,30]
            data=pd.read_csv(r'C:\Users\VULCAN\Desktop\hia\datas.csv').iloc[:,0]



            #第一张图   一个vertical画两图
            self.pw = pg.PlotWidget()  # 实例化一个绘图部件
            self.pw.plot(data)  # 在绘图部件中绘制折线图
            self.pw1=pg.PlotWidget()
            self.pw1.plot(data,)
            self.verticalLayout.addWidget(self.pw)  # 添加绘图部件到网格布局层
            self.verticalLayout.addWidget(self.pw1)  # 添加绘图部件到网格布局层
            #第二张图
            self.pw2 = pg.PlotWidget()  # 实例化一个绘图部件
            self.pw2.plot(data, )  # 在绘图部件中绘制折线图
            self.pw3 = pg.PlotWidget()
            self.pw3.plot(data, )
            self.horizontalLayout_2.addWidget(self.pw2)  # 添加绘图部件到网格布局层
            self.horizontalLayout_2.addWidget(self.pw3)  # 添加绘图部件到网格布局层
            self.flag=0