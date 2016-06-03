# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uiwindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from mplcanvas import MplCanvas

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(812, 597)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.mplwidget = MplCanvas(self.centralwidget)
        self.mplwidget.setGeometry(QtCore.QRect(0, 0, 812, 551))
        self.mplwidget.setObjectName(_fromUtf8("mplwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_file = QtGui.QMenu(self.menubar)
        self.menu_file.setObjectName(_fromUtf8("menu_file"))
        self.menu_proc = QtGui.QMenu(self.menubar)
        self.menu_proc.setObjectName(_fromUtf8("menu_proc"))
        self.menu_recog = QtGui.QMenu(self.menubar)
        self.menu_recog.setObjectName(_fromUtf8("menu_recog"))
        self.menu_help = QtGui.QMenu(self.menubar)
        self.menu_help.setObjectName(_fromUtf8("menu_help"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtGui.QAction(MainWindow)
        self.action_open.setObjectName(_fromUtf8("action_open"))
        self.action_saveas = QtGui.QAction(MainWindow)
        self.action_saveas.setObjectName(_fromUtf8("action_saveas"))
        self.action_reload = QtGui.QAction(MainWindow)
        self.action_reload.setObjectName(_fromUtf8("action_reload"))
        self.action_quit = QtGui.QAction(MainWindow)
        self.action_quit.setObjectName(_fromUtf8("action_quit"))
        self.action_set = QtGui.QAction(MainWindow)
        self.action_set.setObjectName(_fromUtf8("action_set"))
        self.action_proc = QtGui.QAction(MainWindow)
        self.action_proc.setObjectName(_fromUtf8("action_proc"))
        self.action_train = QtGui.QAction(MainWindow)
        self.action_train.setObjectName(_fromUtf8("action_train"))
        self.action_rec = QtGui.QAction(MainWindow)
        self.action_rec.setObjectName(_fromUtf8("action_rec"))
        self.action_about = QtGui.QAction(MainWindow)
        self.action_about.setObjectName(_fromUtf8("action_about"))
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_saveas)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_reload)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_quit)
        self.menu_proc.addAction(self.action_set)
        self.menu_proc.addSeparator()
        self.menu_proc.addAction(self.action_proc)
        self.menu_recog.addAction(self.action_train)
        self.menu_recog.addSeparator()
        self.menu_recog.addAction(self.action_rec)
        self.menu_help.addAction(self.action_about)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_proc.menuAction())
        self.menubar.addAction(self.menu_recog.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Python数字字符识别程序", None))
        self.menu_file.setTitle(_translate("MainWindow", "文件", None))
        self.menu_proc.setTitle(_translate("MainWindow", "图像预处理", None))
        self.menu_recog.setTitle(_translate("MainWindow", "神经网络识别", None))
        self.menu_help.setTitle(_translate("MainWindow", "帮助", None))
        self.action_open.setText(_translate("MainWindow", "打开", None))
        self.action_saveas.setText(_translate("MainWindow", "另存为", None))
        self.action_reload.setText(_translate("MainWindow", "重新加载", None))
        self.action_quit.setText(_translate("MainWindow", "退出", None))
        self.action_set.setText(_translate("MainWindow", "输入归一化宽度和高度", None))
        self.action_proc.setText(_translate("MainWindow", "一次性预处理", None))
        self.action_train.setText(_translate("MainWindow", "训练网络", None))
        self.action_rec.setText(_translate("MainWindow", "识别", None))
        self.action_about.setText(_translate("MainWindow", "关于", None))
