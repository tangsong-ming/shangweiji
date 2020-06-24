'''
创建和使用工具栏
工具栏默认按钮是  只显示图标  将文本作为悬停提示来展示
一个QAction就是一个按钮
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class ToolBar(QMainWindow):
    def __init__(self):
        super(ToolBar, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('工具栏例子')
        self.resize(300,200)

        tb1=self.addToolBar('File')
        #一个QAction就是一个按钮
        new=QAction(QIcon('1.png'),'new',self)
        tb1.addAction(new)
        open=QAction(QIcon('1.png'),'open',self)
        tb1.addAction(open)
        save=QAction(QIcon('1.png'),'save',self)
        tb1.addAction(save)
        #设置文字在图片边上
        tb1.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        tb2=self.addToolBar('File1')
        new1=QAction(QIcon('1.png'),'新建',self)
        tb2.addAction(new1)
        tb2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        tb1.actionTriggered.connect(self.toolbtnpressed)
        tb2.actionTriggered.connect(self.toolbtnpressed)
    def toolbtnpressed(self,a):
        print('按下工具栏按钮时',a.text())
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=ToolBar()
    main.show()
    sys.exit(app.exec_())


