from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sys
'''
校验器
掩码
回显模式
'''
class QLineEditDemo(QWidget):
    def __init__(self):
        super(QLineEditDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('综合案例')
        edit1=QLineEdit()
        #使用校验器
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)#9999
        edit1.setAlignment(Qt.AlignRight)
        edit1.setFont(QFont('Arial',20))
        edit2=QLineEdit()
        edit2.setValidator(QDoubleValidator(0.99,99.99,2))
        edit3=QLineEdit()
        edit3.setInputMask('99_9999_999999;#')
        edit4=QLineEdit()
        edit4.textChanged.connect(self.TextChanged)
        edit5=QLineEdit()
        edit5.setEchoMode(QLineEdit.Password)
        edit5.editingFinished.connect(self.enterPress)
        edit6=QLineEdit('hallo')
        edit6.setReadOnly(True)
        formLayout=QFormLayout()
        formLayout.addRow('整数校验',edit1)
        formLayout.addRow('浮点数校验', edit2)
        formLayout.addRow('掩码',edit3)
        formLayout.addRow('文本变化', edit4)
        formLayout.addRow('密码模式', edit5)
        formLayout.addRow('只读模式', edit6)


        self.setLayout(formLayout)
    def TextChanged(self,text):
        print('输入内容：'+text)
    def enterPress(self):
        print('已输入值')
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLineEditDemo()

    main.show()
    sys.exit(app.exec_())



