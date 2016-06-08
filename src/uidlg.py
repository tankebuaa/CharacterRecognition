# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'uidlg.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_SetDialog(QtGui.QDialog):
    def setupUi(self, SetDialog):
        SetDialog.setObjectName(_fromUtf8("SetDialog"))
        SetDialog.resize(400, 182)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SetDialog.sizePolicy().hasHeightForWidth())
        SetDialog.setSizePolicy(sizePolicy)
        self.buttonBox = QtGui.QDialogButtonBox(SetDialog)
        self.buttonBox.setGeometry(QtCore.QRect(120, 130, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.label_w = QtGui.QLabel(SetDialog)
        self.label_w.setGeometry(QtCore.QRect(30, 50, 181, 16))
        self.label_w.setObjectName(_fromUtf8("label_w"))
        self.label_h = QtGui.QLabel(SetDialog)
        self.label_h.setGeometry(QtCore.QRect(30, 90, 181, 16))
        self.label_h.setObjectName(_fromUtf8("label_h"))
        self.lineEdit_w = QtGui.QLineEdit(SetDialog)
        self.lineEdit_w.setGeometry(QtCore.QRect(250, 50, 113, 20))
        self.lineEdit_w.setObjectName(_fromUtf8("lineEdit_w"))
        self.lineEdit_h = QtGui.QLineEdit(SetDialog)
        self.lineEdit_h.setGeometry(QtCore.QRect(250, 90, 113, 20))
        self.lineEdit_h.setObjectName(_fromUtf8("lineEdit_h"))

        self.retranslateUi(SetDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SetDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SetDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(SetDialog)

    def retranslateUi(self, SetDialog):
        SetDialog.setWindowTitle(_translate("SetDialog", "设置归一化图像尺寸", None))
        self.label_w.setText(_translate("SetDialog", "请输入归一化后每个字符的宽度", None))
        self.label_h.setText(_translate("SetDialog", "请输入归一化后每个字符的高度", None))
        self.lineEdit_w.setText(_translate("SetDialog", "12", None))
        self.lineEdit_h.setText(_translate("SetDialog", "18", None))

