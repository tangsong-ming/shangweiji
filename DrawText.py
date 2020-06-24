'''
绘图api：绘制文本
1.文本
2.图形（直线 点 椭圆 多边形）
3.图像
QPainter
painter=QPainter（）
painter.begin（）
painter.drawText（...）
painter.end（）

在paintEvent事件方法中绘制各种元素
'''
import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QPainter,QColor,QFont
from PyQt5.QtCore import Qt
class DrawText(QWidget):
    def __init__(self):
        super(DrawText, self).__init__()
        self.setWindowTitle('在窗口上绘制文本')
        self.resize(300,200)
        self.text='白洞白色的明天在等着你们'
    def paintEvent(self, event):
        painter=QPainter(self)
        painter.begin(self)
        painter.setPen(QColor(200,43,5))
        painter.setFont(QFont('SimSun',25))
        painter.drawText(event.rect(),Qt.AlignCenter,self.text)
        painter.end()
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=DrawText()
    main.show()
    sys.exit(app.exec_())


