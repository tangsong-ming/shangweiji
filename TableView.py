'''
显示二维表数据（QTableView控件）
数据源
Model
需创建QTableView实例和数据源，然后关联两者
MVC：Model  Viewer  Controller
目的是将后端的数据和前端页面的耦合度降低
'''
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
class TableView(QWidget):
    def __init__(self,arg=None):
        super(TableView, self).__init__(arg)
        self.setWindowTitle('表格视图控件演示')
        self.resize(500,300)
        self.model=QStandardItemModel(4,3)
        self.model.setHorizontalHeaderLabels(['id','姓名','年龄'])
        self.tableview=QTableView()
        #将两者关联
        self.tableview.setModel(self.model)
        #添加数据
        item11=QStandardItem('10')
        item12 = QStandardItem('cgod')
        item13 = QStandardItem('2000')
        self.model.setItem(0,0, item11)
        self.model.setItem(0,1, item12)
        self.model.setItem(0,2, item13)
        item31=QStandardItem('90')
        item32 = QStandardItem('ca')
        item33 = QStandardItem('20')
        self.model.setItem(2,0, item31)
        self.model.setItem(2,1, item32)
        self.model.setItem(2,2, item33)
        layout=QVBoxLayout()
        layout.addWidget(self.tableview)
        self.setLayout(layout)
        #######获取某一个单元格的值得方法
        print(self.model.data(self.model.index(0,0)))
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=TableView()
    main.show()
    sys.exit(app.exec_())

