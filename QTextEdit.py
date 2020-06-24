from PyQt5.QtWidgets import *
import sys

class QTextEditDemo(QWidget):
    def __init__(self):
        super(QTextEditDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QText控件演示')
        self.resize(300,320)
        #全局变量  在槽函数里面要用
        self.textEdit=QTextEdit()
        self.buttonText=QPushButton('显示文本')
        self.buttonHTML=QPushButton('显示html')
        self.buttonToText = QPushButton('获取文本')
        self.buttonToHTML = QPushButton('获取html')
        layout=QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.buttonText)
        layout.addWidget(self.buttonHTML)
        layout.addWidget(self.buttonToText)
        layout.addWidget(self.buttonToHTML)
        self.setLayout(layout)
        self.buttonText.clicked.connect(self.OnClicked_ButtonText)
        self.buttonHTML.clicked.connect(self.OnClicked_ButtonHTML)
        self.buttonToText.clicked.connect(self.OnClicked_ButtonToText)
        self.buttonToHTML.clicked.connect(self.OnClicked_ButtonToHTML)

    def OnClicked_ButtonText(self):
        self.textEdit.setPlainText('hallo world')
    def OnClicked_ButtonHTML(self):
        self.textEdit.setHtml("<font color='blue' size='5'>hallo world</font>")
    def OnClicked_ButtonToText(self):
        print(self.textEdit.toPlainText())
    def OnClicked_ButtonToHTML(self):
        print(self.textEdit.toHtml())
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QTextEditDemo()

    main.show()
    sys.exit(app.exec_())
