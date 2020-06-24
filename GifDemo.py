import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie

class LoadingGif(QWidget):
    def __init__(self):
        super(LoadingGif, self).__init__()
        self.resize(450,300)
        self.label=QLabel('',self)
        #self.setFixedSize(128,128)
        #self.setWindowFlags(Qt.Dialog|Qt.CustomizeWindowHint)
        self.movie=QMovie('./images/3.gif')
        self.label.setMovie(self.movie)
        self.movie.start()

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=LoadingGif()

    main.show()
    sys.exit(app.exec_())