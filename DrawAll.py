'''
绘制各种图形
弧
圆
椭圆
矩形  多边形
绘制图像
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class DrawAll(QWidget):
    def __init__(self):
        super(DrawAll, self).__init__()
        self.resize(300,600)
        self.setWindowTitle('绘制图形')
    def paintEvent(self, event):
        qp=QPainter()
        qp.begin(self)
        qp.setPen(Qt.blue)
        #绘制弧
        rect=QRect(0,10,100,100)
        #起始角度  结束角度alen:1个alen等于1/16度
        qp.drawArc(rect,0,50*16)

        qp.setPen(Qt.red)
        qp.drawArc(QRect(120,10,100,100),0,360*16)
        #绘制带弦的弧度
        qp.drawChord(rect,12,130*16)
        #绘制扇形
        qp.drawPie(rect,12,130*16)
        #椭圆
        qp.drawEllipse(QRect(120,120,150,100))
        #绘制多边形
        point1=QPoint(140,380)
        point2 = QPoint(270, 420)
        point3 = QPoint(290, 512)
        point4 = QPoint(290, 588)
        point5 = QPoint(200, 533)
        polygon=QPolygon([point1,point2,point3,point4,point5])
        qp.drawPolygon(polygon)

        #绘制图像
        image=QImage('1.png')
        rect=QRect(10,400,image.width(),image.height())
        qp.drawImage(rect,image)
        qp.end()

if __name__=='__main__':
    app=QApplication(sys.argv)
    main=DrawAll()
    main.show()
    sys.exit(app.exec_())