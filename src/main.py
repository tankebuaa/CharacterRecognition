# -*- coding : utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from uiwindow import Ui_MainWindow
from uidlg import Ui_SetDialog

class RecWindow(Ui_MainWindow):
    """UI"""
    def __init__(self):
        super(RecWindow, self).__init__()
        # 建立主窗口
        self.setupUi(self)
        # 连接action信号与槽
        self.connect(self.action_open, QtCore.SIGNAL("triggered()"), self.open_file)
        self.connect(self.action_saveas, QtCore.SIGNAL("triggered()"), self.save_file)
        self.connect(self.action_reload, QtCore.SIGNAL("triggered()"), self.reload)
        self.connect(self.action_quit, QtCore.SIGNAL("triggered()"), self.quit)
        self.connect(self.action_set, QtCore.SIGNAL("triggered()"), self.set)
        self.connect(self.action_proc, QtCore.SIGNAL("triggered()"), self.process)
        self.connect(self.action_train, QtCore.SIGNAL("triggered()"), self.train)
        self.connect(self.action_rec, QtCore.SIGNAL("triggered()"), self.recognize)
        self.connect(self.action_about, QtCore.SIGNAL("triggered()"), self.about)
        
    def open_file(self):
        """打开文件"""
        filename = QtGui.QFileDialog.getOpenFileName(self, caption='打开文件', directory='../images/', filter='')
        self.mplwidget.open(filename)
    
    def save_file(self):
        """另存为"""
        filename = QtGui.QFileDialog.getSaveFileName(self, '保存图像', '../images/')
        self.mplwidget.save_as(filename)
    
    def reload(self):
        """重新加载"""
        self.mplwidget.reload()
    
    def quit(self):
        """强制退出"""
        exit()
        
    def set(self):
        """设置归一化宽度和高度"""
        self.dlg = Ui_SetDialog()
        self.dlg.setupUi(self.dlg)
        if self.dlg.exec_():
            para = (int(self.dlg.lineEdit_w.text()), int(self.dlg.lineEdit_h.text()))
        self.mplwidget.set_para(para)
    
    def process(self):
        """一次性预处理"""
        self.mplwidget.process()
    
    def train(self):
        """训练网络"""
        self.mplwidget.train()
    
    def recognize(self):
        """字符识别"""
        pass
    
    def about(self):
        """关于"""
        QtGui.QMessageBox.about(self, "关于", "author@TANKE\n version 0.0")
    
    def closeEvent(self, event):
        """重载关闭窗口事件"""
        msg = QtGui.QMessageBox.question(self, "Warning", "Are you sure to quit?", QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        if msg == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
def main():
    """主函数"""
    sys.setrecursionlimit(10000)
    app = QtGui.QApplication(sys.argv)
    calib = RecWindow()
    calib.show()
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()