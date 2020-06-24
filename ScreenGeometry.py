from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QWidget,QPushButton
import sys
def onClick_Button():
    print('1')
    print('widget.x()=%d' % widget.x())
    print('widget.y()=%d' % widget.y())
    print('widget.width()=%d' % widget.width())
    print('widget.height()=%d' % widget.height())
    print('2')
    print('widget.geometry().x()=%d' % widget.geometry().x())
    print('widget.geometry().y()=%d' % widget.geometry().y())
    print('3')
    print('widget.frameGeometry().x()=%d' % widget.frameGeometry().x())
    print('widget.frameGeometry().y()=%d' % widget.frameGeometry().y())
app=QApplication(sys.argv)

widget=QWidget()
btn=QPushButton(widget)
btn.setText('按钮')
btn.clicked.connect(onClick_Button)

btn.move(24,52)
widget.resize(300,240)  #工作区的尺寸
widget.move(250,200)
widget.setWindowTitle('屏幕坐标系')
widget.show()
sys.exit(app.exec_())

