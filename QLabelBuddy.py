'''
QLabel与伙伴控件
先界面  然后编写槽函数
'''
from PyQt5.QtWidgets import *
import sys
class QLabelBuddy(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控件')

        nameLabel=QLabel('&Name',self)
        nameLineEdit=QLineEdit(self)
        #设置伙伴控件
        nameLabel.setBuddy(nameLineEdit)

        passwordLabel=QLabel('&Password',self)
        passwordLineEdit=QLineEdit(self)
        #设置伙伴控件
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK=QPushButton('&OK')
        btnCancel=QPushButton('&Cancel')

        mainlayout=QGridLayout(self)
        mainlayout.addWidget(nameLabel,0,0)
        mainlayout.addWidget(nameLineEdit,0,1,1,2)

        mainlayout.addWidget(passwordLabel,1,0)
        mainlayout.addWidget(passwordLineEdit, 1, 1, 1, 2)

        mainlayout.addWidget(btnOK,2,1)
        mainlayout.addWidget(btnCancel,2,2)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLabelBuddy()

    main.show()
    sys.exit(app.exec_())

