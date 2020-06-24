from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class theSecond(QDialog):
    def __init__(self):
        super(theSecond, self).__init__()
        self.setWindowTitle('欢迎使用本软件来预测自己的心情数据')
        self.setWindowIcon(QIcon('./images/29.jpg'))
        self.resize(500,503)
        self.label1=QLabel(self)
        self.label1.setAlignment(Qt.AlignCenter)
        self.label1.setToolTip('要开心呀')
        self.movie = QMovie('./images/3.gif')
        self.label1.setMovie(self.movie)
        self.movie.start()
        self.textEdit=QTextEdit(self)
        self.textEdit.move(120,310)
        self.textEdit.setFont(QFont('SanSerif',20))
        with open('./src/1.txt', 'r') as f:
            answer=f.read()
        answer=int(answer)
        if answer==0:
            self.textEdit.setPlainText('别不开心了，笑一个嘛，打开综艺，屏蔽王老师，烦恼全消!')
        elif answer==1:
            self.textEdit.setPlainText('软件预测你的心情还不错，所以还是要多笑笑嘛!')


