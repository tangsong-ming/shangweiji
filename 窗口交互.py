'''
多窗口交互
不使用信号与槽
win1
win2
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from DateDialog import DateDialog

class MultiWindow1(QWidget):
    def __init__(self):
        super(MultiWindow1, self).__init__()
        self.setWindowTitle('多窗口交互 不适用信号与曹')
        self.lineEdit=QLineEdit(self)
        self.button1=QPushButton('弹出对话框1')
        self.button1.clicked.connect(self.onButton1Click)
        self.button2 = QPushButton('弹出对话框2')
        self.button2.clicked.connect(self.onButton2Click)

        gridlayout=QGridLayout()
        gridlayout.addWidget(self.lineEdit)
        gridlayout.addWidget(self.button1)
        gridlayout.addWidget(self.button2)
        self.setLayout(gridlayout)
    def onButton1Click(self):
        dialog=DateDialog(self)
        result=dialog.exec()
        date=dialog.dateTime()
        self.lineEdit.setText(date.date().toString())
        dialog.destroy()
    def onButton2Click(self):
        date,time,result=DateDialog.getDateTime()
        self.lineEdit.setText(date.toString())
        if result==QDialog.Accepted:
            print('点击确定按钮')
        else:
            print('点击取消按钮')
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=MultiWindow1()

    main.show()
    sys.exit(app.exec_())

