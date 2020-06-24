import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

'''
复选框
0没选中
1半选中
2选中
再起一样的名字  就是狗 好吧
'''
class QCheckBoxDemo(QWidget):
    def __init__(self):
        super(QCheckBoxDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('复选框')
        layout=QHBoxLayout()
        self.checkBox1=QCheckBox('复选框控件1')
        self.checkBox1.setChecked(True)
        self.checkBox2 = QCheckBox('复选框控件2')
        self.checkBox3 = QCheckBox('半选中')
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)

        self.checkBox1.stateChanged.connect(lambda:self.checkState(self.checkBox1))
        self.checkBox2.stateChanged.connect(lambda: self.checkState(self.checkBox2))
        self.checkBox3.stateChanged.connect(lambda: self.checkState(self.checkBox3))
        layout.addWidget(self.checkBox1)
        layout.addWidget(self.checkBox2)
        layout.addWidget(self.checkBox3)
        self.setLayout(layout)

    def checkState(self,cb):
        check1Status=self.checkBox1.text()+',isChecked='+str(
            self.checkBox1.isChecked())+',checkState='+str(self.checkBox1.checkState())+'\n'
        check2Status = self.checkBox2.text() + ',isChecked=' + str(
            self.checkBox2.isChecked()) + ',checkState=' + str(self.checkBox2.checkState()) + '\n'
        check3Status = self.checkBox3.text() + ',isChecked=' + str(
            self.checkBox3.isChecked()) + ',checkState=' + str(self.checkBox3.checkState()) + '\n'
        print(check1Status+check2Status+check3Status)



if __name__=='__main__':
    app=QApplication(sys.argv)
    main=QCheckBoxDemo()

    main.show()
    sys.exit(app.exec_())

