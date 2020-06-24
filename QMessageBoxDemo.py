'''
消息对话框
1.关于对话框
2.错误对话框
3.警告对话框
4.提问对话框
5.消息对话框
两点差异：
    对话框图标可能不一样
    显示的按钮是不一样的

'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
class QMessageBoxDemo(QWidget):
    def __init__(self):
        super(QMessageBoxDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Qmessagebox案例')
        self.resize(300,400)
        layout=QVBoxLayout()
        self.setLayout(layout)
        self.button1=QPushButton('显示关于对话框')
        self.button1.clicked.connect(self.showDialog)
        self.button2 = QPushButton('显示消息对话框')
        self.button2.clicked.connect(self.showDialog)
        self.button3 = QPushButton('显示警告对话框')
        self.button3.clicked.connect(self.showDialog)
        self.button4 = QPushButton('显示错误对话框')
        self.button4.clicked.connect(self.showDialog)
        self.button5 = QPushButton('显示提问对话框')
        self.button5.clicked.connect(self.showDialog)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        layout.addWidget(self.button5)
        self.setLayout(layout)
    def showDialog(self):
        text=self.sender().text()
        if text=='显示关于对话框':
            QMessageBox.about(self,'关于','这是一个关于对话框')
        elif text=='显示消息对话框':
            reply=QMessageBox.information(self,'消息','本预测结果仅供参考，请加以自己的分析来判断，对方是否心情不好',
                                          QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
        elif text=='显示警告对话框':
            QMessageBox.warning(self,'警告','警告，快去哄了')
        elif text=='显示错误对话框':
            QMessageBox.critical(self,'错误','你的这个行为是错的哟')
        elif text=='显示提问对话框':
            QMessageBox.question(self,'提问','你是猪嘛',QMessageBox.Yes|QMessageBox.No)

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QMessageBoxDemo()

    main.show()
    sys.exit(app.exec_())




