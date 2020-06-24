'''
让控件支持拖拽操作
A.setDragEnabled(True)
B.setAcceptDrops(True)
B需要两个事件
1.dragEnterEvent   A拖到B触发
2.dropEvent         在B的区域放下A时触发
'''
#效果拔群
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MyComboxBox(QComboBox):
    def __init__(self):
        super(MyComboxBox, self).__init__()
        self.setAcceptDrops(True)
    def dragEnterEvent(self, e):
        print(e)
        #如果有文本的话选择接收
        if e.mimeData().hasText():
            e.accept()
        else:
            e.ignore()
    def dropEvent(self,e):
        self.addItem(e.mimeData().text())

class DrapDropDemoe(QWidget):
    def __init__(self):
        super(DrapDropDemoe, self).__init__()

        formLayout=QFormLayout()
        formLayout.addRow(QLabel('请将左边的文本拖拽到右边的下来列表中'))
        lineEdit=QLineEdit()
        lineEdit.setDragEnabled(True)
        combo=MyComboxBox()
        formLayout.addRow(lineEdit,combo)
        self.setLayout(formLayout)
        self.setWindowTitle('拖拽案例')

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=DrapDropDemoe()
    main.show()
    sys.exit(app.exec_())