# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_SMsgSendData.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SMsgSendData(object):
    def setupUi(self, SMsgSendData):
        SMsgSendData.setObjectName("SMsgSendData")
        SMsgSendData.resize(786, 695)
        self.gridLayout = QtWidgets.QGridLayout(SMsgSendData)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(SMsgSendData)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lineEdit_productExtendId = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_productExtendId.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_productExtendId.setObjectName("lineEdit_productExtendId")
        self.horizontalLayout.addWidget(self.lineEdit_productExtendId)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(SMsgSendData)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.lineEdit_msgId = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_msgId.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_msgId.setObjectName("lineEdit_msgId")
        self.horizontalLayout_2.addWidget(self.lineEdit_msgId)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_16 = QtWidgets.QLabel(SMsgSendData)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_16.addWidget(self.label_16)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem2)
        self.dateTimeEdit_sendedTime = QtWidgets.QDateTimeEdit(SMsgSendData)
        self.dateTimeEdit_sendedTime.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dateTimeEdit_sendedTime.setObjectName("dateTimeEdit_sendedTime")
        self.horizontalLayout_16.addWidget(self.dateTimeEdit_sendedTime)
        self.verticalLayout_4.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_17 = QtWidgets.QLabel(SMsgSendData)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_17.addWidget(self.label_17)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem3)
        self.dateTimeEdit_submitTime = QtWidgets.QDateTimeEdit(SMsgSendData)
        self.dateTimeEdit_submitTime.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.dateTimeEdit_submitTime.setObjectName("dateTimeEdit_submitTime")
        self.horizontalLayout_17.addWidget(self.dateTimeEdit_submitTime)
        self.verticalLayout_4.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(SMsgSendData)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.lineEdit_mobilePhone = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_mobilePhone.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_mobilePhone.setObjectName("lineEdit_mobilePhone")
        self.horizontalLayout_6.addWidget(self.lineEdit_mobilePhone)
        self.verticalLayout_4.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(SMsgSendData)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_7.addWidget(self.label_7)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.lineEdit_matchId = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_matchId.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_matchId.setObjectName("lineEdit_matchId")
        self.horizontalLayout_7.addWidget(self.lineEdit_matchId)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(SMsgSendData)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.lineEdit_realProductExtendId = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_realProductExtendId.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_realProductExtendId.setObjectName("lineEdit_realProductExtendId")
        self.horizontalLayout_8.addWidget(self.lineEdit_realProductExtendId)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(SMsgSendData)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.lineEdit_chargeQuantity = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_chargeQuantity.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_chargeQuantity.setObjectName("lineEdit_chargeQuantity")
        self.horizontalLayout_9.addWidget(self.lineEdit_chargeQuantity)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_28 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_28.setObjectName("horizontalLayout_28")
        self.label_31 = QtWidgets.QLabel(SMsgSendData)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_28.addWidget(self.label_31)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_28.addItem(spacerItem8)
        self.lineEdit_resourceId = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_resourceId.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_resourceId.setObjectName("lineEdit_resourceId")
        self.horizontalLayout_28.addWidget(self.lineEdit_resourceId)
        self.verticalLayout_4.addLayout(self.horizontalLayout_28)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(SMsgSendData)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem9)
        self.lineEdit_propertyComponent = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_propertyComponent.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_propertyComponent.setObjectName("lineEdit_propertyComponent")
        self.horizontalLayout_10.addWidget(self.lineEdit_propertyComponent)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_11 = QtWidgets.QLabel(SMsgSendData)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_11.addWidget(self.label_11)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem10)
        self.lineEdit_sendTimes = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_sendTimes.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_sendTimes.setObjectName("lineEdit_sendTimes")
        self.horizontalLayout_11.addWidget(self.lineEdit_sendTimes)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_12 = QtWidgets.QLabel(SMsgSendData)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_12.addWidget(self.label_12)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem11)
        self.lineEdit_msgType = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_msgType.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_msgType.setObjectName("lineEdit_msgType")
        self.horizontalLayout_12.addWidget(self.lineEdit_msgType)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_13 = QtWidgets.QLabel(SMsgSendData)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem12)
        self.lineEdit_accountId = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_accountId.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_accountId.setObjectName("lineEdit_accountId")
        self.horizontalLayout_13.addWidget(self.lineEdit_accountId)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_15 = QtWidgets.QLabel(SMsgSendData)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_15.addWidget(self.label_15)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem13)
        self.lineEdit_SPNo = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_SPNo.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_SPNo.setObjectName("lineEdit_SPNo")
        self.horizontalLayout_15.addWidget(self.lineEdit_SPNo)
        self.verticalLayout_4.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_14 = QtWidgets.QLabel(SMsgSendData)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_14.addWidget(self.label_14)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem14)
        self.lineEdit_clientMsgId = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_clientMsgId.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_clientMsgId.setObjectName("lineEdit_clientMsgId")
        self.horizontalLayout_14.addWidget(self.lineEdit_clientMsgId)
        self.verticalLayout_4.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(SMsgSendData)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem15)
        self.lineEdit_sendState = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_sendState.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_sendState.setObjectName("lineEdit_sendState")
        self.horizontalLayout_4.addWidget(self.lineEdit_sendState)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(SMsgSendData)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem16)
        self.lineEdit_msgLen = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_msgLen.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_msgLen.setObjectName("lineEdit_msgLen")
        self.horizontalLayout_5.addWidget(self.lineEdit_msgLen)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(SMsgSendData)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem17)
        self.lineEdit_SendResultLen = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_SendResultLen.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_SendResultLen.setObjectName("lineEdit_SendResultLen")
        self.horizontalLayout_3.addWidget(self.lineEdit_SendResultLen)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_18 = QtWidgets.QLabel(SMsgSendData)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout_18.addWidget(self.label_18)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem18)
        self.lineEdit_TitleLen = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_TitleLen.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_TitleLen.setObjectName("lineEdit_TitleLen")
        self.horizontalLayout_18.addWidget(self.lineEdit_TitleLen)
        self.verticalLayout_4.addLayout(self.horizontalLayout_18)
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_19 = QtWidgets.QLabel(SMsgSendData)
        self.label_19.setObjectName("label_19")
        self.horizontalLayout_19.addWidget(self.label_19)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem19)
        self.lineEdit_cycletimes = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_cycletimes.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_cycletimes.setObjectName("lineEdit_cycletimes")
        self.horizontalLayout_19.addWidget(self.lineEdit_cycletimes)
        self.verticalLayout_4.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.label_20 = QtWidgets.QLabel(SMsgSendData)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_20.addWidget(self.label_20)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem20)
        self.lineEdit_Priority = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_Priority.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_Priority.setObjectName("lineEdit_Priority")
        self.horizontalLayout_20.addWidget(self.lineEdit_Priority)
        self.verticalLayout_4.addLayout(self.horizontalLayout_20)
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.label_21 = QtWidgets.QLabel(SMsgSendData)
        self.label_21.setObjectName("label_21")
        self.horizontalLayout_21.addWidget(self.label_21)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem21)
        self.lineEdit_typeComponentParam = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_typeComponentParam.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_typeComponentParam.setObjectName("lineEdit_typeComponentParam")
        self.horizontalLayout_21.addWidget(self.lineEdit_typeComponentParam)
        self.verticalLayout_4.addLayout(self.horizontalLayout_21)
        self.horizontalLayout_22 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_22.setObjectName("horizontalLayout_22")
        self.label_22 = QtWidgets.QLabel(SMsgSendData)
        self.label_22.setObjectName("label_22")
        self.horizontalLayout_22.addWidget(self.label_22)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_22.addItem(spacerItem22)
        self.lineEdit_rmReSendTimes = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_rmReSendTimes.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_rmReSendTimes.setObjectName("lineEdit_rmReSendTimes")
        self.horizontalLayout_22.addWidget(self.lineEdit_rmReSendTimes)
        self.verticalLayout_4.addLayout(self.horizontalLayout_22)
        self.horizontalLayout_23 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_23.setObjectName("horizontalLayout_23")
        self.label_23 = QtWidgets.QLabel(SMsgSendData)
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_23.addWidget(self.label_23)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_23.addItem(spacerItem23)
        self.lineEdit_repResendTimeOut = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_repResendTimeOut.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_repResendTimeOut.setObjectName("lineEdit_repResendTimeOut")
        self.horizontalLayout_23.addWidget(self.lineEdit_repResendTimeOut)
        self.verticalLayout_4.addLayout(self.horizontalLayout_23)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_25 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_25.setObjectName("horizontalLayout_25")
        self.label_27 = QtWidgets.QLabel(SMsgSendData)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_25.addWidget(self.label_27)
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_25.addItem(spacerItem24)
        self.lineEdit_userDefineId = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_userDefineId.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_userDefineId.setObjectName("lineEdit_userDefineId")
        self.horizontalLayout_25.addWidget(self.lineEdit_userDefineId)
        self.verticalLayout_5.addLayout(self.horizontalLayout_25)
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.label_26 = QtWidgets.QLabel(SMsgSendData)
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_24.addWidget(self.label_26)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem25)
        self.lineEdit_title = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_title.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.horizontalLayout_24.addWidget(self.lineEdit_title)
        self.verticalLayout_5.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_27 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_27.setObjectName("horizontalLayout_27")
        self.label_30 = QtWidgets.QLabel(SMsgSendData)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_27.addWidget(self.label_30)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_27.addItem(spacerItem26)
        self.lineEdit_sign = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_sign.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_sign.setObjectName("lineEdit_sign")
        self.horizontalLayout_27.addWidget(self.lineEdit_sign)
        self.verticalLayout_5.addLayout(self.horizontalLayout_27)
        self.horizontalLayout_26 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_26.setObjectName("horizontalLayout_26")
        self.label_28 = QtWidgets.QLabel(SMsgSendData)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_26.addWidget(self.label_28)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_26.addItem(spacerItem27)
        self.lineEdit_totalMsgLen = QtWidgets.QLineEdit(SMsgSendData)
        self.lineEdit_totalMsgLen.setMaximumSize(QtCore.QSize(180, 16777215))
        self.lineEdit_totalMsgLen.setObjectName("lineEdit_totalMsgLen")
        self.horizontalLayout_26.addWidget(self.lineEdit_totalMsgLen)
        self.verticalLayout_5.addLayout(self.horizontalLayout_26)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_29 = QtWidgets.QLabel(SMsgSendData)
        self.label_29.setObjectName("label_29")
        self.verticalLayout_3.addWidget(self.label_29)
        self.textEdit_totalMsg = QtWidgets.QTextEdit(SMsgSendData)
        self.textEdit_totalMsg.setObjectName("textEdit_totalMsg")
        self.verticalLayout_3.addWidget(self.textEdit_totalMsg)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_25 = QtWidgets.QLabel(SMsgSendData)
        self.label_25.setObjectName("label_25")
        self.verticalLayout_2.addWidget(self.label_25)
        self.textEdit_sendResultInfo = QtWidgets.QTextEdit(SMsgSendData)
        self.textEdit_sendResultInfo.setObjectName("textEdit_sendResultInfo")
        self.verticalLayout_2.addWidget(self.textEdit_sendResultInfo)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_24 = QtWidgets.QLabel(SMsgSendData)
        self.label_24.setObjectName("label_24")
        self.verticalLayout.addWidget(self.label_24)
        self.textEdit_msgContent = QtWidgets.QTextEdit(SMsgSendData)
        self.textEdit_msgContent.setObjectName("textEdit_msgContent")
        self.verticalLayout.addWidget(self.textEdit_msgContent)
        self.verticalLayout_5.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 2, 1, 1)
        self.line = QtWidgets.QFrame(SMsgSendData)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 0, 1, 1, 1)

        self.retranslateUi(SMsgSendData)
        QtCore.QMetaObject.connectSlotsByName(SMsgSendData)

    def retranslateUi(self, SMsgSendData):
        _translate = QtCore.QCoreApplication.translate
        SMsgSendData.setWindowTitle(_translate("SMsgSendData", "Form"))
        self.label.setText(_translate("SMsgSendData", "扩展产品"))
        self.lineEdit_productExtendId.setText(_translate("SMsgSendData", "0"))
        self.label_2.setText(_translate("SMsgSendData", "信息编号"))
        self.lineEdit_msgId.setText(_translate("SMsgSendData", "0"))
        self.label_16.setText(_translate("SMsgSendData", "发送时间"))
        self.dateTimeEdit_sendedTime.setDisplayFormat(_translate("SMsgSendData", "yyyy/M/d H:mm:ss"))
        self.label_17.setText(_translate("SMsgSendData", "提交时间"))
        self.dateTimeEdit_submitTime.setDisplayFormat(_translate("SMsgSendData", "yyyy/M/d H:mm:ss"))
        self.label_6.setText(_translate("SMsgSendData", "手机号码"))
        self.lineEdit_mobilePhone.setText(_translate("SMsgSendData", "0"))
        self.label_7.setText(_translate("SMsgSendData", "匹配编号"))
        self.lineEdit_matchId.setText(_translate("SMsgSendData", "0"))
        self.label_8.setText(_translate("SMsgSendData", "真实扩展产品编号"))
        self.lineEdit_realProductExtendId.setText(_translate("SMsgSendData", "0"))
        self.label_9.setText(_translate("SMsgSendData", "计费数"))
        self.lineEdit_chargeQuantity.setText(_translate("SMsgSendData", "0"))
        self.label_31.setText(_translate("SMsgSendData", "资源编号"))
        self.lineEdit_resourceId.setText(_translate("SMsgSendData", "0"))
        self.label_10.setText(_translate("SMsgSendData", "组合属性"))
        self.lineEdit_propertyComponent.setText(_translate("SMsgSendData", "0"))
        self.label_11.setText(_translate("SMsgSendData", "发送次数"))
        self.lineEdit_sendTimes.setText(_translate("SMsgSendData", "0"))
        self.label_12.setText(_translate("SMsgSendData", "消息类型"))
        self.lineEdit_msgType.setText(_translate("SMsgSendData", "0"))
        self.label_13.setText(_translate("SMsgSendData", "账号编号"))
        self.lineEdit_accountId.setText(_translate("SMsgSendData", "0"))
        self.label_15.setText(_translate("SMsgSendData", "企业扩展码"))
        self.lineEdit_SPNo.setText(_translate("SMsgSendData", "0"))
        self.label_14.setText(_translate("SMsgSendData", "客户自定义id"))
        self.lineEdit_clientMsgId.setText(_translate("SMsgSendData", "0"))
        self.label_4.setText(_translate("SMsgSendData", "发送状态"))
        self.lineEdit_sendState.setText(_translate("SMsgSendData", "0"))
        self.label_5.setText(_translate("SMsgSendData", "消息长度"))
        self.lineEdit_msgLen.setText(_translate("SMsgSendData", "0"))
        self.label_3.setText(_translate("SMsgSendData", "发送结果长度"))
        self.lineEdit_SendResultLen.setText(_translate("SMsgSendData", "0"))
        self.label_18.setText(_translate("SMsgSendData", "标题长度"))
        self.lineEdit_TitleLen.setText(_translate("SMsgSendData", "0"))
        self.label_19.setText(_translate("SMsgSendData", "循环次数"))
        self.lineEdit_cycletimes.setText(_translate("SMsgSendData", "0"))
        self.label_20.setText(_translate("SMsgSendData", "消息级别"))
        self.lineEdit_Priority.setText(_translate("SMsgSendData", "0"))
        self.label_21.setText(_translate("SMsgSendData", "综合状态"))
        self.lineEdit_typeComponentParam.setText(_translate("SMsgSendData", "0"))
        self.label_22.setText(_translate("SMsgSendData", "剩余重发次数"))
        self.lineEdit_rmReSendTimes.setText(_translate("SMsgSendData", "0"))
        self.label_23.setText(_translate("SMsgSendData", "回执超时时长"))
        self.lineEdit_repResendTimeOut.setText(_translate("SMsgSendData", "0"))
        self.label_27.setText(_translate("SMsgSendData", "用户定义id"))
        self.lineEdit_userDefineId.setText(_translate("SMsgSendData", "userid"))
        self.label_26.setText(_translate("SMsgSendData", "标题"))
        self.lineEdit_title.setText(_translate("SMsgSendData", "这是标题"))
        self.label_30.setText(_translate("SMsgSendData", "签名"))
        self.lineEdit_sign.setText(_translate("SMsgSendData", "【微网通联】"))
        self.label_28.setText(_translate("SMsgSendData", "整包长度"))
        self.lineEdit_totalMsgLen.setText(_translate("SMsgSendData", "7"))
        self.label_29.setText(_translate("SMsgSendData", "整包内容"))
        self.textEdit_totalMsg.setHtml(_translate("SMsgSendData", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">你好，微网通联</p></body></html>"))
        self.label_25.setText(_translate("SMsgSendData", "发送结果内容"))
        self.textEdit_sendResultInfo.setHtml(_translate("SMsgSendData", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">fail</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.label_24.setText(_translate("SMsgSendData", "短信内容"))
        self.textEdit_msgContent.setHtml(_translate("SMsgSendData", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">你好</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
