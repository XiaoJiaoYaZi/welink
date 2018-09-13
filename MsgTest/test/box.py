# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'box.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 200)
        Form.setMinimumSize(QtCore.QSize(300, 200))
        Form.setMaximumSize(QtCore.QSize(300, 200))
        Form.setStyleSheet("QWidget{\n"
"background-color: rgb(255, 255, 147);\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(5, 0, 5, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setStyleSheet("background-color: rgb(255, 239, 181);")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet("background-color: qconicalgradient(cx:0, cy:0, angle:135, stop:0.374384 rgba(241, 129, 0, 255), stop:0.375 rgba(255, 255, 0, 69), stop:0.423533 rgba(255, 99, 0, 145), stop:0.44335 rgba(255, 190, 0, 208), stop:0.477581 rgba(237, 255, 71, 130), stop:0.518717 rgba(184, 255, 71, 130), stop:0.55 rgba(39, 255, 0, 255), stop:0.57754 rgba(0, 115, 255, 130), stop:0.625 rgba(30, 0, 255, 69), stop:1 rgba(255, 255, 0, 69));")
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setMidLineWidth(7)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.toolButton = QtWidgets.QToolButton(Form)
        self.toolButton.setStyleSheet("background-color: rgb(255, 231, 47);\n"
"QPushButton{\n"
"border:rgb(255, 255, 255);\n"
"border-radius:0px;\n"
"border-style:solid;\n"
"border-width:0px;\n"
"margin:0px;\n"
"padding:0px;\n"
"padding-left: 0px;\n"
"padding-right: 0px;\n"
"\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/button_cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 7)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "niha"))
        self.label.setText(_translate("Form", "TextLabel"))
        self.toolButton.setText(_translate("Form", "..."))

import main_rc
