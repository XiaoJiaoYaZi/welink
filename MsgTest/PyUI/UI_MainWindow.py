# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1264, 754)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/101.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTipDuration(11)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBox_msgtype = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_msgtype.setMaxVisibleItems(20)
        self.comboBox_msgtype.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBox_msgtype.setObjectName("comboBox_msgtype")
        self.comboBox_msgtype.addItem("")
        self.comboBox_msgtype.addItem("")
        self.comboBox_msgtype.addItem("")
        self.comboBox_msgtype.addItem("")
        self.comboBox_msgtype.addItem("")
        self.comboBox_msgtype.addItem("")
        self.comboBox_msgtype.addItem("")
        self.comboBox_msgtype.addItem("")
        self.comboBox_msgtype.addItem("")
        self.comboBox_msgtype.addItem("")
        self.comboBox_msgtype.addItem("")
        self.comboBox_msgtype.addItem("")
        self.comboBox_msgtype.addItem("")
        self.comboBox_msgtype.addItem("")
        self.comboBox_msgtype.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_msgtype)
        self.horizontalLayout_18.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem1)
        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setObjectName("pushButton_save")
        self.horizontalLayout_18.addWidget(self.pushButton_save)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem2)
        self.pushButton_load = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_load.setObjectName("pushButton_load")
        self.horizontalLayout_18.addWidget(self.pushButton_load)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_18)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_7.addWidget(self.checkBox)
        self.checkBox_Play = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_Play.setObjectName("checkBox_Play")
        self.horizontalLayout_7.addWidget(self.checkBox_Play)
        self.gridLayout_2.addLayout(self.horizontalLayout_7, 0, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 1, 0, 1, 2)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_2.addWidget(self.stackedWidget, 2, 0, 3, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 2, 1, 3, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_pausesend = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_pausesend.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_pausesend.setObjectName("pushButton_pausesend")
        self.gridLayout.addWidget(self.pushButton_pausesend, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.label_num_recv = QtWidgets.QLabel(self.centralwidget)
        self.label_num_recv.setObjectName("label_num_recv")
        self.horizontalLayout_4.addWidget(self.label_num_recv)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 1, 1, 1)
        self.pushButton_stoprecv_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stoprecv_2.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_stoprecv_2.setObjectName("pushButton_stoprecv_2")
        self.gridLayout.addWidget(self.pushButton_stoprecv_2, 6, 0, 1, 1)
        self.pushButton_stopsend = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stopsend.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_stopsend.setObjectName("pushButton_stopsend")
        self.gridLayout.addWidget(self.pushButton_stopsend, 2, 0, 1, 1)
        self.pushButton_startrecv = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_startrecv.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_startrecv.setObjectName("pushButton_startrecv")
        self.gridLayout.addWidget(self.pushButton_startrecv, 4, 0, 1, 1)
        self.pushButton_threadsend = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_threadsend.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_threadsend.setObjectName("pushButton_threadsend")
        self.gridLayout.addWidget(self.pushButton_threadsend, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEdit_topick_recv = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_topick_recv.sizePolicy().hasHeightForWidth())
        self.lineEdit_topick_recv.setSizePolicy(sizePolicy)
        self.lineEdit_topick_recv.setObjectName("lineEdit_topick_recv")
        self.verticalLayout_2.addWidget(self.lineEdit_topick_recv)
        self.gridLayout.addLayout(self.verticalLayout_2, 5, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_5.addWidget(self.label_11)
        self.label_recv_speed = QtWidgets.QLabel(self.centralwidget)
        self.label_recv_speed.setObjectName("label_recv_speed")
        self.horizontalLayout_5.addWidget(self.label_recv_speed)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.lineEdit_group = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_group.setObjectName("lineEdit_group")
        self.verticalLayout_3.addWidget(self.lineEdit_group)
        self.gridLayout.addLayout(self.verticalLayout_3, 6, 1, 1, 1)
        self.pushButton_send = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_send.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_send.setObjectName("pushButton_send")
        self.gridLayout.addWidget(self.pushButton_send, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        self.comboBoxpartition = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxpartition.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.comboBoxpartition.setObjectName("comboBoxpartition")
        self.comboBoxpartition.addItem("")
        self.comboBoxpartition.addItem("")
        self.comboBoxpartition.addItem("")
        self.comboBoxpartition.addItem("")
        self.comboBoxpartition.addItem("")
        self.comboBoxpartition.addItem("")
        self.comboBoxpartition.addItem("")
        self.comboBoxpartition.addItem("")
        self.comboBoxpartition.addItem("")
        self.horizontalLayout_13.addWidget(self.comboBoxpartition)
        self.verticalLayout.addLayout(self.horizontalLayout_13)
        self.lineEdit_topick_send = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_topick_send.sizePolicy().hasHeightForWidth())
        self.lineEdit_topick_send.setSizePolicy(sizePolicy)
        self.lineEdit_topick_send.setObjectName("lineEdit_topick_send")
        self.verticalLayout.addWidget(self.lineEdit_topick_send)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.pushButton_stoprecv = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_stoprecv.setMinimumSize(QtCore.QSize(0, 50))
        self.pushButton_stoprecv.setObjectName("pushButton_stoprecv")
        self.gridLayout.addWidget(self.pushButton_stoprecv, 5, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.label_send_speed = QtWidgets.QLabel(self.centralwidget)
        self.label_send_speed.setObjectName("label_send_speed")
        self.horizontalLayout_3.addWidget(self.label_send_speed)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_num_send = QtWidgets.QLabel(self.centralwidget)
        self.label_num_send.setObjectName("label_num_send")
        self.horizontalLayout_2.addWidget(self.label_num_send)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 1, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_8.addWidget(self.label_8)
        self.lineEdit_topic_trans = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_topic_trans.setObjectName("lineEdit_topic_trans")
        self.horizontalLayout_8.addWidget(self.lineEdit_topic_trans)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.checkBox_trans_kafk = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_trans_kafk.setObjectName("checkBox_trans_kafk")
        self.horizontalLayout_11.addWidget(self.checkBox_trans_kafk)
        self.checkBox_search = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_search.setObjectName("checkBox_search")
        self.horizontalLayout_11.addWidget(self.checkBox_search)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.lineEdit_trans_num = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_trans_num.setObjectName("lineEdit_trans_num")
        self.horizontalLayout_9.addWidget(self.lineEdit_trans_num)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.checkBox_transmain = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_transmain.setObjectName("checkBox_transmain")
        self.horizontalLayout_12.addWidget(self.checkBox_transmain)
        self.comboBox_unicode = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_unicode.setObjectName("comboBox_unicode")
        self.comboBox_unicode.addItem("")
        self.comboBox_unicode.addItem("")
        self.horizontalLayout_12.addWidget(self.comboBox_unicode)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.gridLayout.addLayout(self.verticalLayout_4, 7, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(186, 72, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 3, 2, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QtCore.QSize(120, 30))
        self.label_6.setMaximumSize(QtCore.QSize(120, 31))
        self.label_6.setStyleSheet("image: url(:/image/LM.png);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 4, 2, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1264, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setStyleSheet("QStatusBar{\n"
"border-top-width:2px;\n"
"border-color:color: rgb(180, 180, 180);\n"
"}")
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionKafkaTool = QtWidgets.QAction(MainWindow)
        self.actionKafkaTool.setObjectName("actionKafkaTool")
        self.actionSQLTool = QtWidgets.QAction(MainWindow)
        self.actionSQLTool.setObjectName("actionSQLTool")
        self.menu.addAction(self.actionKafkaTool)
        self.menu.addAction(self.actionSQLTool)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.comboBox_unicode.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "nihao"))
        self.label.setText(_translate("MainWindow", "数据类型"))
        self.comboBox_msgtype.setItemText(0, _translate("MainWindow", "SBMSMessage"))
        self.comboBox_msgtype.setItemText(1, _translate("MainWindow", "BMSSHisSendData"))
        self.comboBox_msgtype.setItemText(2, _translate("MainWindow", "BMSSHisRepData"))
        self.comboBox_msgtype.setItemText(3, _translate("MainWindow", "BMSSRepNotifyData"))
        self.comboBox_msgtype.setItemText(4, _translate("MainWindow", "BMSSHisMOData"))
        self.comboBox_msgtype.setItemText(5, _translate("MainWindow", "BMSMoAccBlist"))
        self.comboBox_msgtype.setItemText(6, _translate("MainWindow", "BMSMonitor"))
        self.comboBox_msgtype.setItemText(7, _translate("MainWindow", "SCloudMsg"))
        self.comboBox_msgtype.setItemText(8, _translate("MainWindow", "MsgSendData"))
        self.comboBox_msgtype.setItemText(9, _translate("MainWindow", "MsgHisRepData"))
        self.comboBox_msgtype.setItemText(10, _translate("MainWindow", "MOData"))
        self.comboBox_msgtype.setItemText(11, _translate("MainWindow", "RepNotifyData"))
        self.comboBox_msgtype.setItemText(12, _translate("MainWindow", "Monitor_Cloud"))
        self.comboBox_msgtype.setItemText(13, _translate("MainWindow", "SPackageStat"))
        self.comboBox_msgtype.setItemText(14, _translate("MainWindow", "DispatchNofify"))
        self.pushButton_save.setText(_translate("MainWindow", "保存配置"))
        self.pushButton_load.setText(_translate("MainWindow", "加载配置"))
        self.checkBox.setText(_translate("MainWindow", "kafka队列"))
        self.checkBox_Play.setText(_translate("MainWindow", "DisPlay"))
        self.pushButton_pausesend.setText(_translate("MainWindow", "暂停接收"))
        self.label_9.setText(_translate("MainWindow", "接收量："))
        self.label_num_recv.setText(_translate("MainWindow", "0"))
        self.pushButton_stoprecv_2.setText(_translate("MainWindow", "单条接收"))
        self.pushButton_stopsend.setText(_translate("MainWindow", "停止批量发送"))
        self.pushButton_startrecv.setText(_translate("MainWindow", "批量接收"))
        self.pushButton_threadsend.setText(_translate("MainWindow", "批量发送"))
        self.label_3.setText(_translate("MainWindow", "topic"))
        self.label_11.setText(_translate("MainWindow", "接收速度："))
        self.label_recv_speed.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "group "))
        self.pushButton_send.setText(_translate("MainWindow", "单条发送"))
        self.label_2.setText(_translate("MainWindow", "topic"))
        self.label_12.setText(_translate("MainWindow", "分区"))
        self.comboBoxpartition.setItemText(0, _translate("MainWindow", "-1"))
        self.comboBoxpartition.setItemText(1, _translate("MainWindow", "0"))
        self.comboBoxpartition.setItemText(2, _translate("MainWindow", "1"))
        self.comboBoxpartition.setItemText(3, _translate("MainWindow", "2"))
        self.comboBoxpartition.setItemText(4, _translate("MainWindow", "3"))
        self.comboBoxpartition.setItemText(5, _translate("MainWindow", "4"))
        self.comboBoxpartition.setItemText(6, _translate("MainWindow", "5"))
        self.comboBoxpartition.setItemText(7, _translate("MainWindow", "6"))
        self.comboBoxpartition.setItemText(8, _translate("MainWindow", "7"))
        self.pushButton_stoprecv.setText(_translate("MainWindow", "停止接收"))
        self.label_7.setText(_translate("MainWindow", "发送速度："))
        self.label_send_speed.setText(_translate("MainWindow", "0"))
        self.label_5.setText(_translate("MainWindow", "发送量："))
        self.label_num_send.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "转移队列名"))
        self.checkBox_trans_kafk.setText(_translate("MainWindow", "kafka"))
        self.checkBox_search.setText(_translate("MainWindow", "队列转移"))
        self.label_10.setText(_translate("MainWindow", "转移数量  "))
        self.checkBox_transmain.setText(_translate("MainWindow", "转换主消息"))
        self.comboBox_unicode.setItemText(0, _translate("MainWindow", "UNICODE>>非UNICODE"))
        self.comboBox_unicode.setItemText(1, _translate("MainWindow", "非UNICODE>>UNICODE"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actionKafkaTool.setText(_translate("MainWindow", "KafkaTool"))
        self.actionSQLTool.setText(_translate("MainWindow", "SQLTool"))

import main_rc
