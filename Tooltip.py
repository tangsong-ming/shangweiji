#显示控件提示信息
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QToolTip,QPushButton,QWidget
from PyQt5.QtGui import QFont
import sys
class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        QToolTip.setFont(QFont('SanSerif',12))
        self.setToolTip('今天<b>星期一</b>')
        self.setGeometry(300,300,200,300)
        self.setWindowTitle('设置控件提示消息')
        
        self.button1=QPushButton('按钮')
        self.button1.setToolTip('这是一个按钮a a a ')
        #self.button1.clicked.connect(self.onClick_Button)

        #一层层放上去
        layout=QHBoxLayout()
        layout.addWidget(self.button1)

        mainframe=QWidget()
        mainframe.setLayout(layout)
        #Frame充满整个屏幕
        self.setCentralWidget(mainframe)
if __name__=='__main__':
    app=QApplication(sys.argv)
    #app.setWindowIcon(QIcon(r'1.png'))#给path
    main=TooltipForm()
    main.show()
    sys.exit(app.exec_())


