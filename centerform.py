#窗口居中  通过一个类实现
#QDesktopWidget
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget
import sys
from PyQt5.QtGui import QIcon

class CenterForm(QMainWindow):
    def __init__(self):
        #继承父类
        super(CenterForm,self).__init__()
        #设置主窗口标题
        self.setWindowTitle('让窗口居中')
        self.resize(400,300)
    def center(self):
        #获取屏幕坐标系  和窗口坐标系
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        newleft=(screen.width()-size.width())/2
        newtop = (screen.height() - size.height()) / 2
        self.move(newleft,newtop)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=CenterForm()
    main.center()
    main.show()
    sys.exit(app.exec_())
