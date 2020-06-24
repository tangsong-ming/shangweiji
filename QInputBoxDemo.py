import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
'''
输入对话框：
QInput
'''
class QInputBoxDemo(QWidget):
    def __init__(self):
        super(QInputBoxDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QInputBox案例')

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QInputBoxDemo()

    main.show()
    sys.exit(app.exec_())
