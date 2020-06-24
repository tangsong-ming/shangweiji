from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator#第三个正则表达式
from PyQt5.QtCore import QRegExp#引用正则表达式
import sys
'''
限制QLineEdit控件的输入   校验器
如只能输入整数 浮点数  满足一定条件的字符串
'''
class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('校验器')

        formLayout=QFormLayout()
        IntLineEdit=QLineEdit()
        DoubleLineEdit=QLineEdit()
        validatorLineEdit=QLineEdit()

        formLayout.addRow('int',IntLineEdit)
        formLayout.addRow('double', DoubleLineEdit)
        formLayout.addRow('数字和字母',validatorLineEdit)

        IntLineEdit.setPlaceholderText('整型')

        #整数校验器1-99
        intValidator=QIntValidator(self)
        intValidator.setRange(1,99)
        #浮点
        doubleValidator=QDoubleValidator(self)
        doubleValidator.setRange(-360,360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)#小数点2位

        #字符和数字
        reg=QRegExp('[a-zA-Z0-9]+$')
        validator=QRegExpValidator(self)
        validator.setRegExp(reg)

        #设置校验器
        IntLineEdit.setValidator(intValidator)
        DoubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLineEditValidator()

    main.show()
    sys.exit(app.exec_())






