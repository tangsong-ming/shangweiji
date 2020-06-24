import sys
from PyQt5.QtWidgets import QApplication , QMainWindow,QFileDialog,QMessageBox
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
import numpy as np
from ImageProcess import Ui_Form

class MainWindow(QMainWindow ):
    def __init__(self, parent=None):
        super(MainWindow,self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
    def loading(self):
        try:
            self.fname,_=QFileDialog.getOpenFileName(self,'打开文件','.','图像文件(*.jpg *.png *.gif)')
            self.ui.label_2.setPixmap(QPixmap(self.fname))
            self.im = Image.open(self.fname)
            #print(self.fname,_)
        except:
            QMessageBox.warning(self, '警告', '请先读取路径')
    def jiazai(self):
        try:
            self.ui.label_2.setPixmap(QPixmap(self.fname))
        except:
            QMessageBox.warning(self, '警告', '请先读取路径')
    def form_icon(self):
        try:
            self.im=Image.open(self.fname)
            self.im.thumbnail(size=(128, 128))
            #self.im.show()
            #print(self.fname)
            self.im.save(self.fname)
        except:
            QMessageBox.warning(self, '警告', '请先读取路径')
    def hand_writing(self):
        try:
            vec_el = np.pi / 2.4  # 光源俯视角度  弧度制    为3 的话 类似浮雕效果
            vec_az = np.pi / 4  # 光源方位角度
            depth = 10  # 0-100
            self.im = Image.open(self.fname).convert('L')
            a = np.asarray(self.im).astype('float')
            grad = np.gradient(a)  # 图像灰度的梯度值
            grad_x, grad_y = grad
            grad_x = grad_x * depth / 100
            grad_y = grad_y * depth / 100
            dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x轴的影响
            dy = np.cos(vec_az) * np.cos(vec_el)
            dz = np.sin(vec_el)
            A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
            uni_x = grad_x / A
            uni_y = grad_y / A
            uni_z = 1. / A
            a2 = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化
            a2 = a2.clip(0, 255)  # clip这个函数将将数组中的元素限制在a_min, a_max之间，
            # 大于a_max的就使得它等于 a_max，小于a_min,的就使得它等于a_min
            self.im = Image.fromarray(a2.astype('uint8'))  # 转换数据类型 重构图像
            #self.im.show()
            self.im.save(self.fname)
        except:
            QMessageBox.warning(self, '警告', '请先读取路径')
    def fudiao(self):
        try:
            self.im=self.im.filter(ImageFilter.EMBOSS)
            self.im.save(self.fname)
        except:
            QMessageBox.warning(self, '警告', '请先读取路径')
    def lvjing(self):
        try:
            im0 = np.array(Image.open(self.fname).convert('L'))
            im1 = 255 - im0
            im2 = (100 / 255) * im0 + 150  # 灰白滤镜
            im3 = 255 * (im1 / 255) ** 2
            self.im = Image.fromarray(np.uint(im2))
            if self.im.mode=='I':
                self.im=self.im.convert('RGB')
            self.im.save(self.fname)
        except:
            QMessageBox.warning(self, '警告', '请先读取路径')
    def duibidu(self):
        try:
            self.im = ImageEnhance.Contrast(self.im)  # 对比度
            self.im=self.im.enhance(2)
            self.im.save(self.fname)
        except:
            QMessageBox.warning(self, '警告', '请先读取路径')
    def balance(self):
        try:
            self.im = ImageEnhance.Color(self.im)  # 颜色平衡
            self.im = self.im.enhance(2)
            self.im.save(self.fname)
        except:
            QMessageBox.warning(self, '警告', '请先读取路径')
    def brightness(self):
        try:
            self.im = ImageEnhance.Brightness(self.im)  # 亮度
            self.im = self.im.enhance(2)
            self.im.save(self.fname)
        except:
            QMessageBox.warning(self, '警告', '请先读取路径')
    def sharpness(self):
        try:
            self.im = ImageEnhance.Sharpness(self.im)  # 锐度
            self.im = self.im.enhance(2)
            self.im.save(self.fname)
        except:
            QMessageBox.warning(self, '警告', '请先读取路径')
    def pic_save(self):
        try:
            if '.jpg' in self.fname:
                self.im.save(self.fname)
            if '.png' in self.fname:
                self.im.save(self.fname)
                print(self.fname)
            if '.gif' in self.fname:
                self.im.save(self.fname)
            if '.pdf' in self.fname:
                self.im.save(self.fname)
        except:
            QMessageBox.warning(self, '警告', '请先读取路径')
    def pic_trans(self):
        try:
            if self.ui.comboBox.currentText()=='.jpg':
                self.fname=((self.fname.split('.')[0])+'new.jpg')
                #print((self.fname.split('.')[0])+'new.jpg')
            if self.ui.comboBox.currentText()=='.png':
                self.fname=((self.fname.split('.')[0])+'new.png')
            if self.ui.comboBox.currentText()=='.gif':
                self.fname=((self.fname.split('.')[0])+'new.gif')
            if self.ui.comboBox.currentText()=='.pdf':
                self.fname=((self.fname.split('.')[0])+'new.pdf')
        except:
            QMessageBox.warning(self, '警告', '请先读取路径')
if __name__=="__main__":
	app = QApplication(sys.argv)
	win = MainWindow()
	win.show()
	sys.exit(app.exec_())