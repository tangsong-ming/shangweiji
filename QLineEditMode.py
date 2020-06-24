from PyQt5.QtWidgets import *
import sys

'''
QLineEdit控件与回显模式
基本：
EchoMode  回显模式
4种
1.normal
2.NoEcho 不回显模式
3.Password  ****
4.PasswordEchoOnEdit 先显后不显示
'''
class QLineEditEchoMode(QWidget):
    def __init__(self):
        super(QLineEditEchoMode, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('文本输入框回显模式')
        formLayout=QFormLayout()

        normalLineEdit=QLineEdit()
        noEchoLineEdit=QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow('Normal',normalLineEdit)
        formLayout.addRow('NoEcho',noEchoLineEdit)
        formLayout.addRow('password',passwordLineEdit)
        formLayout.addRow('passwordEchoOnEdit',passwordEchoOnEditLineEdit)

        #palceholdertext  提示信息
        normalLineEdit.setPlaceholderText('Normal')
        noEchoLineEdit.setPlaceholderText('NoEcho')
        passwordLineEdit.setPlaceholderText('password')
        passwordEchoOnEditLineEdit.setPlaceholderText('passwordEchoOnEdit')

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QLineEditEchoMode()

    main.show()
    sys.exit(app.exec_())

