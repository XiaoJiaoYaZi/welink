# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Descrip_Consumer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Descrip(object):
    def setupUi(self, Descrip):
        Descrip.setObjectName("Descrip")
        Descrip.resize(972, 340)
        self.gridLayout = QtWidgets.QGridLayout(Descrip)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.consumer_descrips = QtWidgets.QTableWidget(Descrip)
        self.consumer_descrips.setObjectName("consumer_descrips")
        self.consumer_descrips.setColumnCount(8)
        self.consumer_descrips.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.consumer_descrips.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.consumer_descrips.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.consumer_descrips.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.consumer_descrips.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.consumer_descrips.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.consumer_descrips.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.consumer_descrips.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.consumer_descrips.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.consumer_descrips.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.consumer_descrips.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.consumer_descrips.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.consumer_descrips.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.consumer_descrips.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.consumer_descrips.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.consumer_descrips.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.consumer_descrips.setHorizontalHeaderItem(7, item)
        self.consumer_descrips.horizontalHeader().setCascadingSectionResizes(True)
        self.consumer_descrips.horizontalHeader().setDefaultSectionSize(120)
        self.consumer_descrips.verticalHeader().setVisible(False)
        self.gridLayout.addWidget(self.consumer_descrips, 0, 0, 1, 1)

        self.retranslateUi(Descrip)
        QtCore.QMetaObject.connectSlotsByName(Descrip)

    def retranslateUi(self, Descrip):
        _translate = QtCore.QCoreApplication.translate
        Descrip.setWindowTitle(_translate("Descrip", "Form"))
        item = self.consumer_descrips.verticalHeaderItem(0)
        item.setText(_translate("Descrip", "新建行"))
        item = self.consumer_descrips.verticalHeaderItem(1)
        item.setText(_translate("Descrip", "新建行"))
        item = self.consumer_descrips.verticalHeaderItem(2)
        item.setText(_translate("Descrip", "新建行"))
        item = self.consumer_descrips.verticalHeaderItem(3)
        item.setText(_translate("Descrip", "新建行"))
        item = self.consumer_descrips.verticalHeaderItem(4)
        item.setText(_translate("Descrip", "新建行"))
        item = self.consumer_descrips.verticalHeaderItem(5)
        item.setText(_translate("Descrip", "新建行"))
        item = self.consumer_descrips.verticalHeaderItem(6)
        item.setText(_translate("Descrip", "新建行"))
        item = self.consumer_descrips.verticalHeaderItem(7)
        item.setText(_translate("Descrip", "新建行"))
        item = self.consumer_descrips.horizontalHeaderItem(0)
        item.setText(_translate("Descrip", "Partition"))
        item = self.consumer_descrips.horizontalHeaderItem(1)
        item.setText(_translate("Descrip", "LogSize"))
        item = self.consumer_descrips.horizontalHeaderItem(2)
        item.setText(_translate("Descrip", "Offset"))
        item = self.consumer_descrips.horizontalHeaderItem(3)
        item.setText(_translate("Descrip", "Lag"))
        item = self.consumer_descrips.horizontalHeaderItem(4)
        item.setText(_translate("Descrip", "group_id"))
        item = self.consumer_descrips.horizontalHeaderItem(5)
        item.setText(_translate("Descrip", "member_id"))
        item = self.consumer_descrips.horizontalHeaderItem(6)
        item.setText(_translate("Descrip", "client_id"))
        item = self.consumer_descrips.horizontalHeaderItem(7)
        item.setText(_translate("Descrip", "client_host"))
