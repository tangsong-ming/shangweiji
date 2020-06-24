import sys
from PyQt5.QtWidgets import QApplication , QMainWindow
from waterWin import Ui_Form

class MainWindow(QMainWindow ):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    def query(self):
        if self.ui.comboBox.currentText() == '区域A':
            self.ui.textEdit.setPlainText('a:xxxxxx')
            self.ui.textEdit.append('b:xxxxxx')
            self.ui.textEdit.append('c:xxxxxx')
            self.ui.textEdit.append('建议:xxxxxx')
if __name__=="__main__":
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())




