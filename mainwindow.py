from PyQt5.QtWidgets import QMainWindow,QApplication
import sys
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self):
        #继承父类
        super(FirstMainWin,self).__init__()
        #设置主窗口标题
        self.setWindowTitle('第一个主窗口')
        self.resize(400,300)
        self.status=self.statusBar()
        self.status.showMessage('只存在5s的消息',5000)
if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon(r'1.png'))#给path
    main=FirstMainWin()
    main.show()
    sys.exit(app.exec_())


