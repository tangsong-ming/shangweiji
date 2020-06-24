from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QWidget,QPushButton
import sys

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(300,120)
        self.setWindowTitle('退出应用程序')
        #添加按钮
        self.button1=QPushButton('退出应用程序')
        self.button1.clicked.connect(self.onClick_Button)

        #一层层放上去
        layout=QHBoxLayout()
        layout.addWidget(self.button1)

        mainframe=QWidget()
        mainframe.setLayout(layout)
        #Frame充满整个屏幕
        self.setCentralWidget(mainframe)
    #按钮单击事件方法(自定义了一个槽
    def onClick_Button(self):
        sender=self.sender()
        print(sender.text()+'按钮被按下')
        app=QApplication.instance()
        #退出
        app.quit()
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QuitApplication()

    main.show()
    sys.exit(app.exec_())

