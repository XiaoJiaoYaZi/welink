# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_SRepNotifyData.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SRepNotifyData(object):
    def setupUi(self, SRepNotifyData):
        SRepNotifyData.setObjectName("SRepNotifyData")
        SRepNotifyData.resize(690, 494)
        self.gridLayout = QtWidgets.QGridLayout(SRepNotifyData)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(SRepNotifyData)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_msgId = QtWidgets.QLineEdit(SRepNotifyData)
        self.lineEdit_msgId.setObjectName("lineEdit_msgId")
        self.horizontalLayout.addWidget(self.lineEdit_msgId)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(SRepNotifyData)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lineEdit_accId = QtWidgets.QLineEdit(SRepNotifyData)
        self.lineEdit_accId.setObjectName("lineEdit_accId")
        self.horizontalLayout_2.addWidget(self.lineEdit_accId)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(SRepNotifyData)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.lineEdit_mobile = QtWidgets.QLineEdit(SRepNotifyData)
        self.lineEdit_mobile.setObjectName("lineEdit_mobile")
        self.horizontalLayout_3.addWidget(self.lineEdit_mobile)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(SRepNotifyData)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.lineEdit_sendState = QtWidgets.QLineEdit(SRepNotifyData)
        self.lineEdit_sendState.setObjectName("lineEdit_sendState")
        self.horizontalLayout_4.addWidget(self.lineEdit_sendState)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(SRepNotifyData)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.lineEdit_reportState = QtWidgets.QLineEdit(SRepNotifyData)
        self.lineEdit_reportState.setObjectName("lineEdit_reportState")
        self.horizontalLayout_5.addWidget(self.lineEdit_reportState)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(SRepNotifyData)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem5)
        self.dateTimeEdit_sendDateTime = QtWidgets.QDateTimeEdit(SRepNotifyData)
        self.dateTimeEdit_sendDateTime.setObjectName("dateTimeEdit_sendDateTime")
        self.horizontalLayout_6.addWidget(self.dateTimeEdit_sendDateTime)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(SRepNotifyData)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.dateTimeEdit_reportDateTime = QtWidgets.QDateTimeEdit(SRepNotifyData)
        self.dateTimeEdit_reportDateTime.setObjectName("dateTimeEdit_reportDateTime")
        self.horizontalLayout_7.addWidget(self.dateTimeEdit_reportDateTime)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(SRepNotifyData)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem7)
        self.dateTimeEdit_recvReportDateTime = QtWidgets.QDateTimeEdit(SRepNotifyData)
        self.dateTimeEdit_recvReportDateTime.setObjectName("dateTimeEdit_recvReportDateTime")
        self.horizontalLayout_8.addWidget(self.dateTimeEdit_recvReportDateTime)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(SRepNotifyData)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem8)
        self.lineEdit_pk_total = QtWidgets.QLineEdit(SRepNotifyData)
        self.lineEdit_pk_total.setObjectName("lineEdit_pk_total")
        self.horizontalLayout_9.addWidget(self.lineEdit_pk_total)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(SRepNotifyData)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.lineEdit_pk_num = QtWidgets.QLineEdit(SRepNotifyData)
        self.lineEdit_pk_num.setObjectName("lineEdit_pk_num")
        self.horizontalLayout_10.addWidget(self.lineEdit_pk_num)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(SRepNotifyData)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.lineEdit_flagBits = QtWidgets.QLineEdit(SRepNotifyData)
        self.lineEdit_flagBits.setObjectName("lineEdit_flagBits")
        self.horizontalLayout_11.addWidget(self.lineEdit_flagBits)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(SRepNotifyData)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.lineEdit_spno = QtWidgets.QLineEdit(SRepNotifyData)
        self.lineEdit_spno.setObjectName("lineEdit_spno")
        self.horizontalLayout_12.addWidget(self.lineEdit_spno)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_13 = QtWidgets.QLabel(SRepNotifyData)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem12)
        self.lineEdit_acc_msgid = QtWidgets.QLineEdit(SRepNotifyData)
        self.lineEdit_acc_msgid.setObjectName("lineEdit_acc_msgid")
        self.horizontalLayout_13.addWidget(self.lineEdit_acc_msgid)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_15 = QtWidgets.QLabel(SRepNotifyData)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_15.addWidget(self.label_15)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem13)
        self.lineEdit_extnumber = QtWidgets.QLineEdit(SRepNotifyData)
        self.lineEdit_extnumber.setObjectName("lineEdit_extnumber")
        self.horizontalLayout_15.addWidget(self.lineEdit_extnumber)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_17 = QtWidgets.QLabel(SRepNotifyData)
        self.label_17.setObjectName("label_17")
        self.verticalLayout.addWidget(self.label_17)
        self.textEdit_sendResultInfo = QtWidgets.QTextEdit(SRepNotifyData)
        self.textEdit_sendResultInfo.setObjectName("textEdit_sendResultInfo")
        self.verticalLayout.addWidget(self.textEdit_sendResultInfo)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_18 = QtWidgets.QLabel(SRepNotifyData)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_2.addWidget(self.label_18)
        self.textEdit_repResultInfo = QtWidgets.QTextEdit(SRepNotifyData)
        self.textEdit_repResultInfo.setObjectName("textEdit_repResultInfo")
        self.verticalLayout_2.addWidget(self.textEdit_repResultInfo)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 1)

        self.retranslateUi(SRepNotifyData)
        QtCore.QMetaObject.connectSlotsByName(SRepNotifyData)

    def retranslateUi(self, SRepNotifyData):
        _translate = QtCore.QCoreApplication.translate
        SRepNotifyData.setWindowTitle(_translate("SRepNotifyData", "Form"))
        self.label.setText(_translate("SRepNotifyData", "消息ID       "))
        self.lineEdit_msgId.setText(_translate("SRepNotifyData", "0"))
        self.label_2.setText(_translate("SRepNotifyData", "用户ID       "))
        self.lineEdit_accId.setText(_translate("SRepNotifyData", "0"))
        self.label_3.setText(_translate("SRepNotifyData", "电话号码     "))
        self.lineEdit_mobile.setText(_translate("SRepNotifyData", "13000000000"))
        self.label_4.setText(_translate("SRepNotifyData", "发送状态     "))
        self.lineEdit_sendState.setText(_translate("SRepNotifyData", "0"))
        self.label_5.setText(_translate("SRepNotifyData", "回执状态     "))
        self.lineEdit_reportState.setText(_translate("SRepNotifyData", "0"))
        self.label_6.setText(_translate("SRepNotifyData", "发送时间"))
        self.dateTimeEdit_sendDateTime.setDisplayFormat(_translate("SRepNotifyData", "yyyy/M/d H:mm:ss"))
        self.label_7.setText(_translate("SRepNotifyData", "回执时间"))
        self.dateTimeEdit_reportDateTime.setDisplayFormat(_translate("SRepNotifyData", "yyyy/M/d H:mm:ss"))
        self.label_8.setText(_translate("SRepNotifyData", "回执本地时间 "))
        self.dateTimeEdit_recvReportDateTime.setDisplayFormat(_translate("SRepNotifyData", "yyyy/M/d H:mm:ss"))
        self.label_9.setText(_translate("SRepNotifyData", "信息总页数  "))
        self.lineEdit_pk_total.setText(_translate("SRepNotifyData", "0"))
        self.label_10.setText(_translate("SRepNotifyData", "信息当前页数"))
        self.lineEdit_pk_num.setText(_translate("SRepNotifyData", "0"))
        self.label_11.setText(_translate("SRepNotifyData", "flagbits    "))
        self.lineEdit_flagBits.setText(_translate("SRepNotifyData", "0"))
        self.label_12.setText(_translate("SRepNotifyData", "服务商号    "))
        self.lineEdit_spno.setText(_translate("SRepNotifyData", "0"))
        self.label_13.setText(_translate("SRepNotifyData", "客户自定义id"))
        self.lineEdit_acc_msgid.setText(_translate("SRepNotifyData", "0"))
        self.label_15.setText(_translate("SRepNotifyData", "扩展号码    "))
        self.lineEdit_extnumber.setText(_translate("SRepNotifyData", "0"))
        self.label_17.setText(_translate("SRepNotifyData", "发送结果内容"))
        self.textEdit_sendResultInfo.setHtml(_translate("SRepNotifyData", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hello</p></body></html>"))
        self.label_18.setText(_translate("SRepNotifyData", "状态报告结果内容"))
        self.textEdit_repResultInfo.setHtml(_translate("SRepNotifyData", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">hello</p></body></html>"))

