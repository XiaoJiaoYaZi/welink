# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_KafkaTool.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_KafkaTool(object):
    def setupUi(self, KafkaTool):
        KafkaTool.setObjectName("KafkaTool")
        KafkaTool.resize(1474, 872)
        KafkaTool.setMinimumSize(QtCore.QSize(1200, 800))
        self.gridLayout_2 = QtWidgets.QGridLayout(KafkaTool)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(KafkaTool)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.host = QtWidgets.QLineEdit(KafkaTool)
        self.host.setObjectName("host")
        self.horizontalLayout.addWidget(self.host)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.connect = QtWidgets.QPushButton(KafkaTool)
        self.connect.setObjectName("connect")
        self.horizontalLayout_2.addWidget(self.connect)
        self.unconnect = QtWidgets.QPushButton(KafkaTool)
        self.unconnect.setObjectName("unconnect")
        self.horizontalLayout_2.addWidget(self.unconnect)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(KafkaTool)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.fresh = QtWidgets.QPushButton(self.page)
        self.fresh.setObjectName("fresh")
        self.horizontalLayout_3.addWidget(self.fresh)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.lineEdit_search_topic = QtWidgets.QLineEdit(self.page)
        self.lineEdit_search_topic.setObjectName("lineEdit_search_topic")
        self.verticalLayout_3.addWidget(self.lineEdit_search_topic)
        self.topic = QtWidgets.QListWidget(self.page)
        self.topic.setObjectName("topic")
        self.verticalLayout_3.addWidget(self.topic)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 2, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.page)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.topic_decrips = QtWidgets.QTableWidget(self.page)
        self.topic_decrips.setMinimumSize(QtCore.QSize(580, 0))
        self.topic_decrips.setStyleSheet("QWidget{border: 1px solid color: rgb(0, 0, 0) ; border-radius: 5px}\n"
"")
        self.topic_decrips.setGridStyle(QtCore.Qt.SolidLine)
        self.topic_decrips.setObjectName("topic_decrips")
        self.topic_decrips.setColumnCount(7)
        self.topic_decrips.setRowCount(8)
        item = QtWidgets.QTableWidgetItem()
        self.topic_decrips.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.topic_decrips.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.topic_decrips.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.topic_decrips.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.topic_decrips.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.topic_decrips.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.topic_decrips.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.topic_decrips.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.topic_decrips.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.topic_decrips.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.topic_decrips.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.topic_decrips.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.topic_decrips.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.topic_decrips.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.topic_decrips.setHorizontalHeaderItem(6, item)
        self.topic_decrips.horizontalHeader().setVisible(True)
        self.topic_decrips.horizontalHeader().setDefaultSectionSize(80)
        self.topic_decrips.horizontalHeader().setHighlightSections(True)
        self.topic_decrips.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.topic_decrips)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.page)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.freshconsumer = QtWidgets.QPushButton(self.page)
        self.freshconsumer.setObjectName("freshconsumer")
        self.horizontalLayout_4.addWidget(self.freshconsumer)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.lineEdit_search_consume = QtWidgets.QLineEdit(self.page)
        self.lineEdit_search_consume.setObjectName("lineEdit_search_consume")
        self.verticalLayout_2.addWidget(self.lineEdit_search_consume)
        self.consumer = QtWidgets.QListWidget(self.page)
        self.consumer.setObjectName("consumer")
        self.verticalLayout_2.addWidget(self.consumer)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.page)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.tabWidget = QtWidgets.QTabWidget(self.page)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.gridLayout.setObjectName("gridLayout")
        self.consumer_descrips = QtWidgets.QTableWidget(self.tab)
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
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_4.addWidget(self.tabWidget)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 1, 1, 1, 2)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_2.addWidget(self.stackedWidget, 1, 0, 1, 1)
        self.action_delete = QtWidgets.QAction(KafkaTool)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/image/edit_remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_delete.setIcon(icon)
        self.action_delete.setObjectName("action_delete")
        self.action_fresh = QtWidgets.QAction(KafkaTool)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/image/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_fresh.setIcon(icon1)
        self.action_fresh.setObjectName("action_fresh")

        self.retranslateUi(KafkaTool)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(KafkaTool)

    def retranslateUi(self, KafkaTool):
        _translate = QtCore.QCoreApplication.translate
        KafkaTool.setWindowTitle(_translate("KafkaTool", "KafkaTool"))
        self.label.setText(_translate("KafkaTool", "Host"))
        self.host.setText(_translate("KafkaTool", "10.1.63.126:9092,10.1.63.127:9092,10.1.63.128:9092"))
        self.connect.setText(_translate("KafkaTool", "链接"))
        self.unconnect.setText(_translate("KafkaTool", "断开"))
        self.label_5.setText(_translate("KafkaTool", "Topic"))
        self.fresh.setText(_translate("KafkaTool", "刷新"))
        self.label_3.setText(_translate("KafkaTool", "Partition Information"))
        item = self.topic_decrips.verticalHeaderItem(0)
        item.setText(_translate("KafkaTool", "新建行"))
        item = self.topic_decrips.verticalHeaderItem(1)
        item.setText(_translate("KafkaTool", "新建行"))
        item = self.topic_decrips.verticalHeaderItem(2)
        item.setText(_translate("KafkaTool", "新建行"))
        item = self.topic_decrips.verticalHeaderItem(3)
        item.setText(_translate("KafkaTool", "新建行"))
        item = self.topic_decrips.verticalHeaderItem(4)
        item.setText(_translate("KafkaTool", "新建行"))
        item = self.topic_decrips.verticalHeaderItem(5)
        item.setText(_translate("KafkaTool", "新建行"))
        item = self.topic_decrips.verticalHeaderItem(6)
        item.setText(_translate("KafkaTool", "新建行"))
        item = self.topic_decrips.verticalHeaderItem(7)
        item.setText(_translate("KafkaTool", "新建行"))
        item = self.topic_decrips.horizontalHeaderItem(0)
        item.setText(_translate("KafkaTool", "分区"))
        item = self.topic_decrips.horizontalHeaderItem(1)
        item.setText(_translate("KafkaTool", "Leader"))
        item = self.topic_decrips.horizontalHeaderItem(2)
        item.setText(_translate("KafkaTool", "Replicas"))
        item = self.topic_decrips.horizontalHeaderItem(3)
        item.setText(_translate("KafkaTool", "ISR"))
        item = self.topic_decrips.horizontalHeaderItem(4)
        item.setText(_translate("KafkaTool", "最早偏移量"))
        item = self.topic_decrips.horizontalHeaderItem(5)
        item.setText(_translate("KafkaTool", "最晚偏移量"))
        item = self.topic_decrips.horizontalHeaderItem(6)
        item.setText(_translate("KafkaTool", "总偏移量"))
        self.label_2.setText(_translate("KafkaTool", "Consumers consuming from this topic"))
        self.freshconsumer.setText(_translate("KafkaTool", "刷新"))
        self.label_4.setText(_translate("KafkaTool", "Consumer Offsets"))
        item = self.consumer_descrips.verticalHeaderItem(0)
        item.setText(_translate("KafkaTool", "新建行"))
        item = self.consumer_descrips.verticalHeaderItem(1)
        item.setText(_translate("KafkaTool", "新建行"))
        item = self.consumer_descrips.verticalHeaderItem(2)
        item.setText(_translate("KafkaTool", "新建行"))
        item = self.consumer_descrips.verticalHeaderItem(3)
        item.setText(_translate("KafkaTool", "新建行"))
        item = self.consumer_descrips.verticalHeaderItem(4)
        item.setText(_translate("KafkaTool", "新建行"))
        item = self.consumer_descrips.verticalHeaderItem(5)
        item.setText(_translate("KafkaTool", "新建行"))
        item = self.consumer_descrips.verticalHeaderItem(6)
        item.setText(_translate("KafkaTool", "新建行"))
        item = self.consumer_descrips.verticalHeaderItem(7)
        item.setText(_translate("KafkaTool", "新建行"))
        item = self.consumer_descrips.horizontalHeaderItem(0)
        item.setText(_translate("KafkaTool", "Partition"))
        item = self.consumer_descrips.horizontalHeaderItem(1)
        item.setText(_translate("KafkaTool", "LogSize"))
        item = self.consumer_descrips.horizontalHeaderItem(2)
        item.setText(_translate("KafkaTool", "Offset"))
        item = self.consumer_descrips.horizontalHeaderItem(3)
        item.setText(_translate("KafkaTool", "Lag"))
        item = self.consumer_descrips.horizontalHeaderItem(4)
        item.setText(_translate("KafkaTool", "group_id"))
        item = self.consumer_descrips.horizontalHeaderItem(5)
        item.setText(_translate("KafkaTool", "member_id"))
        item = self.consumer_descrips.horizontalHeaderItem(6)
        item.setText(_translate("KafkaTool", "client_id"))
        item = self.consumer_descrips.horizontalHeaderItem(7)
        item.setText(_translate("KafkaTool", "client_host"))
        self.action_delete.setText(_translate("KafkaTool", "删除"))
        self.action_delete.setToolTip(_translate("KafkaTool", "<html><head/><body><p>删除主题</p><p><br/></p></body></html>"))
        self.action_fresh.setText(_translate("KafkaTool", "刷新"))

import main_rc
