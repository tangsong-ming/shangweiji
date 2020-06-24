from PyQt5.QtWidgets import *
'''
文件对话框
QfileDialog
1.打开图像文件显示
2.打开文本文件显示
'''
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('文本对话框')
        self.resize(500,500)
        layout=QVBoxLayout()
        self.button1=QPushButton('加载图片')
        self.button1.clicked.connect(self.loadImage)
        layout.addWidget(self.button1)
        self.imagelabel=QLabel()
        layout.addWidget(self.imagelabel)
        self.button2=QPushButton('加载文本文件')
        self.button2.clicked.connect(self.loadText)
        layout.addWidget(self.button2)

        self.contents=QTextEdit()
        layout.addWidget(self.contents)
        self.setLayout(layout)
    def loadImage(self):
        fname,_=QFileDialog.getOpenFileName(self,'打开文件','.','图像文件(*.jpg *.png)')
        self.imagelabel.setPixmap(QPixmap(fname))
        #跳出本地的图片文件
        #可以加个图片居中显示
    def loadText(self):
        dialog=QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        #选择文件
        dialog.setFilter(QDir.Files)
        if dialog.exec():
            filenames=dialog.selectedFiles()
            f=open(filenames[0],'r',encoding='gbk')
            #编码格式
            with f:
                data=f.read()
                self.contents.setText(data)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QFileDialogDemo()
    main.show()
    sys.exit(app.exec_())





