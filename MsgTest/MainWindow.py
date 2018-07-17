from PyQt5 import QtWidgets,QtCore,Qt

from SMessage import SBmsMessage, SHisSendData
from UI_MainWindow import Ui_MainWindow
from BMSMessage import BMSMessage,BMSSHisSendData,BMSSHisRepData,BMSSRepNotifyData,BMSSHisMOData,BMSMoAccBlist,BMSMonitor
import sys

import time
import os
import threading
from KafkaManager import KafkaManager
from configparser import ConfigParser

_num_recv = 0
_num_send = 0

class BMSMsgTest(QtWidgets.QMainWindow,Ui_MainWindow):
    _sendData = []
    _recvData = []
    signal_recv = QtCore.pyqtSignal(bytes)
    def __init__(self):
        super(BMSMsgTest,self).__init__()
        self.setupUi(self)
        self._kafka = KafkaManager()
        self._init()
        self.initUI()


    def _init(self):
        self.b_start = False
        try:
            self._config = ConfigParser()
            self._config.read(os.getcwd()+'/config/config.ini',encoding='utf-8')
        except:
            print('read config error')
        self._kafka.create_producer(self._config['MsgTest']['topic_producer'])
        self._sendData.append(BMSMessage())
        self._sendData.append(BMSSHisSendData())
        self._sendData.append(BMSSHisRepData())
        self._sendData.append(BMSSRepNotifyData())
        self._sendData.append(BMSSHisMOData())
        self._sendData.append(BMSMoAccBlist())
        self._sendData.append(BMSMonitor())

        self._recvData.append(BMSMessage)
        self._recvData.append(BMSSHisSendData)
        self._recvData.append(BMSSHisRepData)
        self._recvData.append(BMSSRepNotifyData)
        self._recvData.append(BMSSHisMOData)
        self._recvData.append(BMSMoAccBlist)
        self._recvData.append(BMSMonitor)

        self.num_send = 0
        self.num_recv = 0
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.speed)
        self.timer.start(1000)

    def initUI(self):
        self.stackedWidget.insertWidget(0, self._sendData[0])
        self.stackedWidget.insertWidget(1, self._sendData[1])
        self.stackedWidget.insertWidget(2, self._sendData[2])
        self.stackedWidget.insertWidget(3, self._sendData[3])
        self.stackedWidget.insertWidget(4, self._sendData[4])
        self.stackedWidget.insertWidget(5, self._sendData[5])
        self.stackedWidget.insertWidget(6, self._sendData[6])
        self.stackedWidget.setCurrentIndex(0)
        self.pushButton_stoprecv.setEnabled(False)
        self.pushButton_stopsend.setEnabled(False)
        self.pushButton_pausesend.setEnabled(False)
        self.lineEdit_topick_send.setText(self._config['MsgTest']['topic_producer'])
        self.lineEdit_topick_recv.setText(self._config['MsgTest']['topic_consumer'])
        self.lineEdit_group.setText(self._config['MsgTest']['groupid'])
        #self.lineEdit_topick_send.textChanged()
        self.signal_recv.connect(self.analyze,QtCore.Qt.QueuedConnection)

    def on_lineEdit_topick_send_textChanged(self,a0):
        self._config['MsgTest']['topic_producer'] = a0
        self._kafka.settopic_producer(a0)

    def on_lineEdit_topick_recv_textChanged(self,a0):
        self._config['MsgTest']['topic_consumer'] = a0

    def on_lineEdit_group_textChanged(self,a0):
        self._config['MsgTest']['groupid'] = a0

    def saveconfig(self):
        with open(os.getcwd()+'/config/config.ini','w',encoding='utf-8') as f:
            self._config.write(f)


    def createconnections(self):
        self.comboBox_msgtype.currentIndexChanged()
        pass

    def on_comboBox_msgtype_currentIndexChanged(self,a0):
        print(a0)
        if isinstance(a0,int):
            self.stackedWidget.setCurrentIndex(a0)

    def on_pushButton_send_pressed(self):
        # print(self.__BMSMessage.timeEdit_StartSendTime.time().toString("HH:mm:ss"))
        # print(self.__BMSMessage.timeEdit_StartSendTime.time().toPyTime())
        # t = self.__BMSMessage.dateTimeEdit_StartSendDateTime.dateTime().toPyDateTime().ctime()
        # t = time.mktime(time.strptime(t))
        # print(type(t))
        # print(self.__BMSMessage.textEdit_content.toPlainText())
        data = self._sendData[self.comboBox_msgtype.currentIndex()].getValue()
        print(data)
        self._kafka.send(data)
        self.num_send += 1


    def on_pushButton_save_pressed(self):
        filename = QtWidgets.QInputDialog.getText(self,'保存配置','文件名')
        print(filename)
        if filename[1] and filename[0] !='':
            self._sendData[self.comboBox_msgtype.currentIndex()].saveConfig(filename[0])

    def on_pushButton_load_pressed(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self,'选择配置',os.getcwd(),"*.ini")
        print(filename)
        if filename[1] and filename[0] != '':
            self._sendData[self.comboBox_msgtype.currentIndex()].loadConfig(filename)

    def on_pushButton_threadsend_pressed(self):
        self.b_start = True
        self._thread = threading.Thread(target= self.thread_send)
        self._thread.start()
        self.pushButton_stopsend.setEnabled(True)
        self.pushButton_threadsend.setEnabled(False)
        self.pushButton_pausesend.setEnabled(True)

    def thread_send(self):
        data = self._sendData[self.comboBox_msgtype.currentIndex()].getValue()
        while self.b_start:
            self.num_send += 1
            data = self._sendData[self.comboBox_msgtype.currentIndex()].updatedata()
            self._kafka.send(data)

    def on_pushButton_stopsend_pressed(self):
        if self.b_start:
            self.b_start = False
            self._thread.join()
            self.pushButton_stopsend.setEnabled(False)
            self.pushButton_threadsend.setEnabled(True)

    def on_pushButton_startrecv_pressed(self):
        self._kafka.create_consumer(self._config['MsgTest']['topic_consumer'],
                                    self._config['MsgTest']['groupid'])
        self._kafka.startiocp_recv(self.recv_func)
        self.pushButton_stoprecv.setEnabled(True)
        self.pushButton_startrecv.setEnabled(False)
        pass

    def on_pushButton_stoprecv_pressed(self):
        self._kafka.stopRecv()
        self.pushButton_stoprecv.setEnabled(False)
        self.pushButton_startrecv.setEnabled(True)
        pass

    def on_pushButton_stoprecv_2_pressed(self):
        self._kafka.create_consumer(self._config['MsgTest']['topic_consumer'],
                                    self._config['MsgTest']['groupid'])
        self._kafka.recvOne(self.recv_func)
        pass

    def recv_func(self,kafka_message):
        #print(kafka_message)
        global _num_time
        time.sleep(0.0001)
        self.signal_recv.emit(kafka_message)
        self.num_recv += 1

    def analyze(self,value):
        #print(value)
        try:
            self._sendData[self.comboBox_msgtype.currentIndex()].analyze(value)
        except:
            print('analyze error')
        #QtCore.QCoreApplication.processEvents()

    def speed(self):
        QtCore.QCoreApplication.processEvents()
        self.label_num_send.setText(str(self.num_send))
        self.label_num_recv.setText(str(self.num_recv))
        global _num_recv
        global _num_send
        self.label_send_speed.setText(str(self.num_send-_num_send))
        self.label_recv_speed.setText(str(self.num_recv-_num_recv))
        _num_recv = self.num_recv
        _num_send = self.num_send
        pass

    def closeEvent(self,event):
        self.on_pushButton_stoprecv_pressed()
        self.on_pushButton_stopsend_pressed()
        self._kafka.close()
        event.accept()