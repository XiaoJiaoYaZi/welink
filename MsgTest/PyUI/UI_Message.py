# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Message.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Message(object):
    def setupUi(self, Message):
        Message.setObjectName("Message")
        Message.resize(830, 409)
        self.gridLayout = QtWidgets.QGridLayout(Message)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_save = QtWidgets.QPushButton(Message)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout.addWidget(self.pushButton_save)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(Message)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.ContiguousSelection)
        self.treeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setDefaultSectionSize(50)
        self.treeWidget.header().setMinimumSectionSize(10)
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 1)

        self.retranslateUi(Message)
        QtCore.QMetaObject.connectSlotsByName(Message)

    def retranslateUi(self, Message):
        _translate = QtCore.QCoreApplication.translate
        Message.setWindowTitle(_translate("Message", "消息内容"))
        self.pushButton_save.setText(_translate("Message", "save"))

