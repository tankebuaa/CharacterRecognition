# -*- coding : utf-8 -*-

import cv2
import matplotlib.pyplot as plt
from PyQt4 import QtGui, QtCore
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolBar
import recfunc

class MplData(object):
    """存放和处理图片数据的类"""
    def __init__(self):
        self.img = None
        self.WD = 12
        self.HG = 18
    
    def read_img(self, name):
        self.filename = name
        self.img = cv2.imread(name)
    
    def save_img(self, name):
        cv2.imwrite(name, self.img)
        
    def set(self,para):
        self.WD, self.HG = para
        
    def process_img(self):
        self.img, self.cha, self.features = recfunc.process(self.img, self.WD, self.HG)
    
class MplCanvas(QtGui.QWidget):
    """主窗体小部件，利用matplotlib"""
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.data = MplData()
        self.create_canvas()
        
    def create_canvas(self):
        """创建figure画布"""
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.canvas.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.toolbar = NavigationToolBar(self.canvas, self)
        
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.canvas)
        layout.addWidget(self.toolbar)
        
        self.setLayout(layout)
        self.ax = plt.subplot(111)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        
    def show_img(self):
        """显示图像"""
        if self.data.img.ndim == 3:
            b, g, r = cv2.split(self.data.img)
            image = cv2.merge([r,g,b])
            self.ax.imshow(image)
        else:
            image = self.data.img
            self.ax.imshow(image, cmap = "gray")
        self.canvas.draw()
        
    def open(self, filename):
        """读入图像，并显示"""
        # 读入图片
        self.data.read_img(filename)
        # 显示
        self.ax.cla()
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.show_img()
        
    def save_as(self, filename):
        """将显示的图像另存为"""
        self.data.save_img(filename)
        
    def reload(self):
        """重新加载原图像并显示"""
        self.data.read_img(self.data.filename)
        self.ax.cla()
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        self.show_img()
        
    def set_para(self, para):
        """设置归一化宽度和高度"""
        self.data.set(para)
        
    def process(self):
        """一次性预处理"""
        self.data.process_img()
        self.show_img()
        # 画出字符外框
        for everyCha in self.data.cha:
            L = everyCha[1]
            self.ax.plot([L[2], L[3], L[3], L[2], L[2]], [L[0], L[0], L[1], L[1], L[0]], 'r-', linewidth=2)
        self.canvas.draw()