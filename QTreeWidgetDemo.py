'''
树控件的基本用法

'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon,QBrush,QColor
from PyQt5.QtCore import Qt
class BasicTreeWidget(QMainWindow):
    def __init__(self,parent=None):
        super(BasicTreeWidget, self).__init__(parent)
        self.setWindowTitle('树控件的基本用法')
        self.tree=QTreeWidget()
        self.tree.setColumnCount(2)
        #制定列标签
        self.tree.setHeaderLabels(['Key','Value'])
        #根节点
        root=QTreeWidgetItem(self.tree)
        root.setText(0,'根节点')
        root.setIcon(0,QIcon('1.png'))
        self.tree.setColumnWidth(0,160)
        #添加子节点
        child1=QTreeWidgetItem(root)
        child1.setText(0,'子节点1')
        child1.setText(1,'子节点1的数据')
        child1.setIcon(0,QIcon('1.png'))
        child1.setCheckState(0,Qt.Checked)#复选框
        #添加子节点2
        child2=QTreeWidgetItem(root)
        child2.setText(0,'子节点2')
        child2.setIcon(0,QIcon('1.png'))
        child2.setText(1, '子节点2的数据')
        child2.setCheckState(0, Qt.Checked)  # 复选框
        #为child2添加一个子节点
        child3=QTreeWidgetItem(child2)
        child3.setText(0,'子节点2-1')
        child3.setIcon(0, QIcon('1.png'))
        child3.setText(1, '子节点2的数据')

        self.tree.expandAll()#展开所有节点

        #充满整个控件
        self.setCentralWidget(self.tree)


if __name__=='__main__':
    app=QApplication(sys.argv)
    tree=BasicTreeWidget()
    tree.show()
    sys.exit(app.exec_())


