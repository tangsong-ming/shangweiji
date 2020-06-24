'''
绘制不同类型的直线

'''
'''
用像素点绘制正弦曲线
-2pi---2pi
drawPoint（x,y）
'''
import math,sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class DrawMultLine(QWidget):
    def __init__(self):
        super(DrawMultLine, self).__init__()
        self.resize(300,300)
        self.setWindowTitle('设置Pen的样式')

    def paintEvent(self, event):
        painter=QPainter()
        painter.begin(self)
        pen=QPen(Qt.red,3,Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(20,40,250,40)

        pen.setStyle(Qt.DashDotLine)#换各种各样的线
        painter.setPen(pen)
        painter.drawLine(20,80,250,80)
        #自定义线
        pen.setStyle(Qt.CustomDashLine)
        pen.setDashPattern([1,4,5,4])
        painter.setPen(pen)
        painter.drawLine(20,200,250,200)
        size=self.size()


        painter.end()
if __name__=='__main__':
    app=QApplication(sys.argv)
    main=DrawMultLine()
    main.show()
    sys.exit(app.exec_())


