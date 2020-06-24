import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
class StackedDemo(QTabWidget):
    def __init__(self,parent=None):
        super(StackedDemo, self).__init__(parent)
        self.setGeometry(300,50,10,10)
        self.setWindowTitle('堆栈窗口控件（QStackedWidget）')
        self.list=QListWidget()
        self.list.insertItem(0,'联系方式')
        self.list.insertItem(1, '个人信息')
        self.list.insertItem(2, '教育程度')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

        self.stack=QStackedWidget()
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
        hbox=QHBoxLayout()
        hbox.addWidget(self.list)
        hbox.addWidget(self.stack)
        self.setLayout(hbox)
        #信号  发生改变时
        self.list.currentRowChanged.connect(self.display)
    def tab1UI(self):
        #表单布局
        layout=QFormLayout()
        #添加姓名，地址的单行文本输入框
        layout.addRow('姓名',QLineEdit())
        layout.addRow('地址',QLineEdit())
        #设置选项卡的小标题与布局方式
        self.stack1.setLayout(layout)

    def tab2UI(self):
        #zhu表单布局，次水平布局
        layout=QFormLayout()
        sex=QHBoxLayout()

        #水平布局添加单选按钮
        sex.addWidget(QRadioButton('男'))
        sex.addWidget(QRadioButton('女'))

        #表单布局添加控件
        layout.addRow(QLabel('性别'),sex)
        layout.addRow('生日',QLineEdit())

        #设置标题与布局

        self.stack2.setLayout(layout)

    def tab3UI(self):
        #水平布局
        layout=QHBoxLayout()

        #添加控件到布局中
        layout.addWidget(QLabel('科目'))
        layout.addWidget(QCheckBox('物理'))
        layout.addWidget(QCheckBox('高数'))

        #设置小标题与布局方式

        self.stack3.setLayout(layout)
    def display(self,index):
        self.stack.setCurrentIndex(index)
if __name__ == '__main__':
    app=QApplication(sys.argv)
    demo=StackedDemo()
    demo.show()
    sys.exit(app.exec_())
