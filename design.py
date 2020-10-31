# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(488, 535)
        self.Port = QtWidgets.QComboBox(Form)
        self.Port.setGeometry(QtCore.QRect(100, 30, 211, 31))
        self.Port.setObjectName("Port")
        self.Speed = QtWidgets.QComboBox(Form)
        self.Speed.setGeometry(QtCore.QRect(100, 70, 211, 31))
        self.Speed.setObjectName("Speed")
#        self.label = QtWidgets.QLabel(Form)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 40, 61, 16))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 61, 16))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.ConnectButton = QtWidgets.QPushButton(Form)
        self.ConnectButton.setGeometry(QtCore.QRect(320, 30, 151, 31))
        self.ConnectButton.setObjectName("ConnectButton")
        self.OnBtn = QtWidgets.QPushButton(Form)
        self.OnBtn.setGeometry(QtCore.QRect(30, 120, 211, 31))
        self.OnBtn.setObjectName("OnBtn")
        self.blinkBtn = QtWidgets.QPushButton(Form)
        self.blinkBtn.setGeometry(QtCore.QRect(260, 120, 211, 31))
        self.blinkBtn.setObjectName("blinkBtn")
        self.label_Vtext = QtWidgets.QLabel(Form)
        self.label_Vtext.setGeometry(QtCore.QRect(170, 180, 301, 16))
        self.label_Vtext.setMaximumSize(QtCore.QSize(16777215, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_Vtext.setFont(font)
        self.label_Vtext.setObjectName("label_Vtext")
        self.GetVBtn = QtWidgets.QPushButton(Form)
        self.GetVBtn.setGeometry(QtCore.QRect(30, 170, 121, 31))
        self.GetVBtn.setObjectName("GetVBtn")
        self.BaudDetectButton = QtWidgets.QPushButton(Form)
        self.BaudDetectButton.setGeometry(QtCore.QRect(320, 70, 151, 31))
        self.BaudDetectButton.setObjectName("BaudDetectButton")
        self.GetVcontBtn = QtWidgets.QPushButton(Form)
        self.GetVcontBtn.setGeometry(QtCore.QRect(30, 210, 441, 31))
        self.GetVcontBtn.setObjectName("GetVcontBtn")
        self.graphWidget = PlotWidget(Form)
        self.graphWidget.setGeometry(QtCore.QRect(30, 250, 441, 271))
        self.graphWidget.setObjectName("graphWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ARDUINO control via USB"))
        self.label.setText(_translate("Form", "Port"))
        self.label_2.setText(_translate("Form", "Speed"))
        self.ConnectButton.setText(_translate("Form", "Connect"))
        self.OnBtn.setText(_translate("Form", "LED on"))
        self.blinkBtn.setText(_translate("Form", "LED blinking"))
        self.label_Vtext.setText(_translate("Form", "Voltage"))
        self.GetVBtn.setText(_translate("Form", "Get Voltage"))
        self.BaudDetectButton.setText(_translate("Form", "Baud autodetect"))
        self.GetVcontBtn.setText(_translate("Form", "Get Voltage every 1s"))
from pyqtgraph import PlotWidget
