'''
按钮控件
QPushButton
父类：QAbstractButton
QPushButton
AToolButton
QRadioButton
QCheckBox

'''
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class QPushButtonDemo(QDialog):
    def __init__(self):
        super(QPushButtonDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('按钮的使用')
        self.resize(400,300)
        layout=QVBoxLayout()
        self.button1=QPushButton('第一个按钮')
        self.button1.setText('first Button')
        #设置按钮被按下
        self.button1.setCheckable(True)
        self.button1.toggle()
        self.button1.clicked.connect(self.ButtonState)
        #传入lambda表达式  为了第二个布尔值参数btn
        self.button1.clicked.connect(lambda: self.WhichButton(self.button1))

        self.button2=QPushButton('图像按钮')
        self.button2.setIcon(QIcon(QPixmap('./images/1.png')))
        self.button2.clicked.connect(lambda: self.WhichButton(self.button2))

        self.button3=QPushButton('不可用按钮')
        self.button3.setEnabled(False)

        self.button4=QPushButton('&MyButton')
        self.button4.setDefault(True)#默认按钮  快捷键alt M
        self.button4.clicked.connect(lambda: self.WhichButton(self.button4))

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        self.setLayout(layout)
    def WhichButton(self,btn):#self.sender() 之前有
        print('被单击的按钮是<'+btn.text()+'>')
    def ButtonState(self):
        if self.button1.isChecked():
            print('按钮1被选中')
        else:
            print('按钮1未被选中')
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QPushButtonDemo()

    main.show()
    sys.exit(app.exec_())



