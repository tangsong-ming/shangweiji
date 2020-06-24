import  sys
import mood_prediction#这个是由ui转为py的文件名
#导入由ui编出来的那个py
from PyQt5.QtWidgets import QApplication,QMainWindow
#基础的导入
if __name__=='__main__':
    app=QApplication(sys.argv)
    mainWindow=QMainWindow()
    #实例化两个对象
    #对自动生成的py实例化 然后用其中的方法
    ui=mood_prediction.Ui_MainWindow()
    #添加控件的方法
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

