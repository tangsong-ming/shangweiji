'''
在单元格中放置控件
setCellWidget:在单元格中放置控件
setItem:文本
QSS：setStyleSheet('QPushButton{margin:3px};')设置控件样式

'''
import sys
from PyQt5.QtWidgets import *
class PlaceControlInCell(QWidget):
    def __init__(self):
        super(PlaceControlInCell, self).__init__()
        self.initUI()
    def initUI(self):
        self.resize(430,300)
        layout=QHBoxLayout()
        tableWidget=QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)
        tableWidget.setHorizontalHeaderLabels(['姓名','体重','性别'])
        textItem=QTableWidgetItem('光明')
        tableWidget.setItem(0,0,textItem)

        self.combox=QComboBox()
        self.combox.addItem('0')
        self.combox.addItem('1')
        #QSS  设置所有QComboBox  边距为3
        self.combox.setStyleSheet('QComboBox{margin:3px};')
        tableWidget.setCellWidget(0,1,self.combox)

        #添加一个按钮 默认按下的状态
        modifyButton=QPushButton('修改')
        modifyButton.setDown(True)
        modifyButton.setStyleSheet('QPushButton{margin:3px};')
        #完成combox当前选中的值得获取  用来进行模型预测
        modifyButton.clicked.connect(self.onClicked)
        tableWidget.setCellWidget(0, 2, modifyButton)

        self.setLayout(layout)
    def onClicked(self):
        print(self.combox.currentText())
        print(type(int(self.combox.currentText())))
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=PlaceControlInCell()
    main.show()
    sys.exit(app.exec_())


