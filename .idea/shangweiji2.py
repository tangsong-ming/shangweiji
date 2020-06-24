from PyQt5.QtWidgets import QLabel,QTextEdit,QDialog,QPushButton,QTableView,QVBoxLayout
from PyQt5.QtCore import Qt,QRect
from PyQt5.QtGui import QIcon,QMovie,QFont,QStandardItemModel,QStandardItem
from PyQt5 import QtWidgets
import pypyodbc
class theSecond(QDialog):
    def __init__(self):
        super(theSecond, self).__init__()
        self.setWindowTitle('欢迎使用本软件来预测自己的心情数据')
        self.setWindowIcon(QIcon(':/images/29.jpg'))
        self.resize(600,600)
        # self.label1=QLabel(self)
        # self.label1.setAlignment(Qt.AlignCenter)
        # self.label1.setToolTip('要开心呀')
        # self.movie = QMovie(':/images/3.gif')
        # self.label1.setMovie(self.movie)
        # self.movie.start()
        # self.textEdit=QTextEdit(self)
        # self.textEdit.move(120,310)
        # self.textEdit.setFont(QFont('SanSerif',20))
        # with open('D:/mood/src/1.txt', 'r') as f:
        #     answer=f.read()
        # answer=int(answer)
        # if answer==0:
        #     self.textEdit.setPlainText('别不开心了，笑一个嘛，人生总是不堪与顺遂交错，这样才会坚信自己是被上帝选中的人，每一次触底反弹的前提往往是谷底几日的昏暗。')
        # elif answer==1:
        #     self.textEdit.setPlainText('软件预测你的心情还不错，所以还是要多笑笑嘛!')
        self.layout = QVBoxLayout()
        self.button_read = QPushButton(self)
        self.button_read.setText('load')
        self.button_read.clicked.connect(self.onClickedButtonRead)
        self.button_delete = QPushButton(self)
        self.button_delete.setText('load')
        self.button_delete.clicked.connect(self.onClickedButtonDelete)
        self.tableWidget=QTableView(self)
        # self.tableWidget.setGeometry(QRect(30, 80, 550, 500))
        self.layout.addWidget(self.button_read)
        self.layout.addWidget(self.tableWidget)
        self.setLayout(self.layout)
    def onClickedButtonRead(self):
        path = r'C:\Users\VULCAN\Desktop\ten\acc1.accdb'  # 数据库文件
        strr = 'Driver={Microsoft Access Driver (*.mdb,*.accdb)};DBQ=' + (path)
        db = pypyodbc.win_connect_mdb(strr)
        curser = db.cursor()
        # curser.execute("select * from MSysAccessStorage order by id desc")
        # 查询的sql语句
        sql = "SELECT * FROM sensors"
        curser.execute(sql)
        # 获取查询到的数据, 是以二维元组的形式存储的, 所以读取需要使用 data[i][j] 下标定位
        ndata = curser.fetchall()
        # 打印测试
        # print(ndata)
        model = QStandardItemModel()

        title = ['温度', 'ph值', '浊度', '电导率', '采集时间']

        model.setHorizontalHeaderLabels(title)
        for row, linedata in enumerate(ndata):

            for col, itemdata in enumerate(linedata):

                item = QStandardItem(str(itemdata)) if itemdata != None else QStandardItem('')

                model.setItem(row, col, item)

        # tableView.setModel(model)
        self.tableWidget.setModel(model)

        curser.close()
        db.close()
    def onClickedButtonDelete(self):
        pass



