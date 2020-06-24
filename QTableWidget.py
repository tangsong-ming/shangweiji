import sys
from PyQt5.QtWidgets import *
'''
每一个cell是一个QTableWidgetItem
用一种方式能完成，这种方式可能是好的
'''
class TableWidgetDemo(QWidget):
    def __init__(self):
        super(TableWidgetDemo, self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('- -!QTableWidget演示！')
        self.resize(500,800)
        layout=QHBoxLayout()
        tablewidget=QTableWidget()
        #设置行列数
        tablewidget.setRowCount(4)
        tablewidget.setColumnCount(3)
        layout.addWidget(tablewidget)
        tablewidget.setHorizontalHeaderLabels(['姓名','年龄','身份'])
        nameItem=QTableWidgetItem('dell')
        tablewidget.setItem(0,0,nameItem)
        ageItem = QTableWidgetItem('10')
        tablewidget.setItem(0, 1, ageItem)
        shenfenItem=QTableWidgetItem('好事者')
        tablewidget.setItem(0, 2, shenfenItem)

        #禁止编辑
        #tablewidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #整行选择
        tablewidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        #调整行列大小
        #tablewidget.resizeRowsToContents()
        #tablewidget.resizeColumnsToContents()

        #表格头显示隐藏
        #tablewidget.horizontalHeader().setVisible(False)
        #tablewidget.verticalHeader().setVisible(False)

        #隐藏表格线
        tablewidget.setShowGrid(False)
        self.setLayout(layout)
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=TableWidgetDemo()
    main.show()
    sys.exit(app.exec_())


