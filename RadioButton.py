import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class RadioButton(QWidget):
    def __init__(self):
        super(RadioButton, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('radiobutton')
        #放在一个容器
        layout=QHBoxLayout()
        self.button1=QRadioButton('单1')
        self.button1.setChecked(True)
        self.button2=QRadioButton('单2')
        #状态切换toggle
        self.button1.toggled.connect(self.buttonState)
        self.button2.toggled.connect(self.buttonState)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        self.setLayout(layout)

    def buttonState(self):
        radioButton=self.sender()

        if radioButton.text()=='单1':
            if radioButton.isChecked()==True:
                print('<'+radioButton.text()+'>被选中')
            else:
                print('<'+radioButton.text()+'>被取消选中状态')
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=RadioButton()

    main.show()
    sys.exit(app.exec_())
