from PyQt5.QtWidgets import QMainWindow,QApplication
import sys
from PyQt5.QtGui import QIcon
'''
窗口的setWindowIcon用于设置窗口的图标
QApplication中的setWindowIcon用于设置主窗口的图标和应用程序图标    
'''
class IconForm(QMainWindow):
    def __init__(self):
        #继承父类
        super(IconForm,self).__init__()
        self.initUI()
    def initUI(self):
        self.setGeometry(300,300,250,250)
        self.setWindowTitle('设置窗口图标')
        #图标
        self.setWindowIcon(QIcon(r'1.png'))

if __name__=='__main__':
    app=QApplication(sys.argv)
    #app.setWindowIcon(QIcon(r'1.png'))#给path
    main=IconForm()
    main.show()
    sys.exit(app.exec_())

