# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DispatchNofify.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DispatchNofify(object):
    def setupUi(self, DispatchNofify):
        DispatchNofify.setObjectName("DispatchNofify")
        DispatchNofify.resize(640, 480)
        self.layoutWidget = QtWidgets.QWidget(DispatchNofify)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 260, 247, 23))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_flag = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_flag.setObjectName("lineEdit_flag")
        self.horizontalLayout_2.addWidget(self.lineEdit_flag)
        self.layoutWidget_2 = QtWidgets.QWidget(DispatchNofify)
        self.layoutWidget_2.setGeometry(QtCore.QRect(140, 320, 247, 23))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(self.layoutWidget_2)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_3.addWidget(self.dateTimeEdit)
        self.widget = QtWidgets.QWidget(DispatchNofify)
        self.widget.setGeometry(QtCore.QRect(140, 210, 247, 23))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit_msgid = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_msgid.setObjectName("lineEdit_msgid")
        self.horizontalLayout.addWidget(self.lineEdit_msgid)

        self.retranslateUi(DispatchNofify)
        QtCore.QMetaObject.connectSlotsByName(DispatchNofify)

    def retranslateUi(self, DispatchNofify):
        _translate = QtCore.QCoreApplication.translate
        DispatchNofify.setWindowTitle(_translate("DispatchNofify", "Form"))
        self.label_2.setText(_translate("DispatchNofify", "flag"))
        self.label_3.setText(_translate("DispatchNofify", "time"))
        self.dateTimeEdit.setDisplayFormat(_translate("DispatchNofify", "yyyy/M/d H:mm:ss"))
        self.label.setText(_translate("DispatchNofify", "msgid"))

