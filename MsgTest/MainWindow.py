from PyQt5 import QtWidgets,QtCore
from PyUI.UI_MainWindow import Ui_MainWindow
from BMSMessage import BMSMessage,BMSSHisSendData,BMSSHisRepData,BMSSRepNotifyData,BMSSHisMOData,BMSMoAccBlist,BMSMonitor
from CloudMsg import CloudMsg,MsgSendData,MsgHisRepData,MOData,RepNotifyData,Monitor_Cloud,SPackageStat

import time
import os
import threading
from KafkaManager import KafkaManager,MsMqManageerDLL
from configparser import ConfigParser
from KafkaTool import KafkaTool
from SQL import SQLView
from PlatformPublicDefine import Old2New,New2Old


_num_recv = 0
_num_send = 0


def SendFunc(func):
    def transmsg(cls,msg, old, needtran):
        if needtran:
            if old:
                msg = Old2New(msg)
            else:
                msg = New2Old(msg)
        return func(cls,msg, old, needtran)

    return transmsg
def MsgFunc(func):
    def transmsg(cls,msg,size,usekafka):
        if not usekafka:
            msg = None


class Senders(object):
    def __init__(self,kafka,msmq,**kwargs):
        self._kafka = kafka
        self._msmq = msmq

    def send(self,msg,kafka = True):
        if kafka:
            self._kafka.send(msg)
        else:
            self._msmq.send(msg)

class BMSMsgTest(QtWidgets.QMainWindow,Ui_MainWindow):
    _sendData = []
    _recvData = []
    signal_recv = QtCore.pyqtSignal(bytes)
    sender = None
    def __init__(self):
        super(BMSMsgTest,self).__init__()
        self.setupUi(self)
        self._kafka = KafkaManager()
        self._kafka_trans = KafkaManager()
        self._msmq = MsMqManageerDLL()
        self._msmq_trans = MsMqManageerDLL()
        self._init()
        self.initUI()



    def _init(self):
        self.b_start = False
        self._brecv1 = True
        self._isold = True
        self.b_needtran = False
        self.i_partition = None
        try:
            self._config = ConfigParser()
            self._config.read(os.getcwd()+'/config/config.ini',encoding='gbk')
        except:
            print('read config error')
            return
        self._kafka.create_producer(self._config['MsgTest']['topic_producer'])
        self._kafka_trans.create_producer(self._config['MsgTest']['topic_trans'])
        self._msmq.create_producer(self._config['MsgTest']['msmqpath_producer'])
        self._initData()
        self._createconnections()

        self.kafkatool = KafkaTool()
        self.sqltool = SQLView(self)

        self.num_send = 0
        self.num_recv = 0
        self.num_trans = 0xffffffff


    def _createconnections(self):
        #self.comboBox_unicode.currentIndexChanged()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.speed)
        self.timer.start(1000)
        self.comboBoxpartition.currentIndexChanged.connect(self.set_partition)


    def _initData(self):
        self._sendData.append(BMSMessage())
        self._sendData.append(BMSSHisSendData())
        self._sendData.append(BMSSHisRepData())
        self._sendData.append(BMSSRepNotifyData())
        self._sendData.append(BMSSHisMOData())
        self._sendData.append(BMSMoAccBlist())
        self._sendData.append(BMSMonitor())
        self._sendData.append(CloudMsg())
        self._sendData.append(MsgSendData())
        self._sendData.append(MsgHisRepData())
        self._sendData.append(MOData())
        self._sendData.append(RepNotifyData())
        self._sendData.append(Monitor_Cloud())
        self._sendData.append(SPackageStat())

        self._recvData.append(BMSMessage)
        self._recvData.append(BMSSHisSendData)
        self._recvData.append(BMSSHisRepData)
        self._recvData.append(BMSSRepNotifyData)
        self._recvData.append(BMSSHisMOData)
        self._recvData.append(BMSMoAccBlist)
        self._recvData.append(BMSMonitor)
        self._recvData.append(CloudMsg)


    def initUI(self):
        for i in range(len(self._sendData)):
            self.stackedWidget.insertWidget(i,self._sendData[i])

        self.stackedWidget.setCurrentIndex(0)
        self.lineEdit_trans_num.setText(str(self.num_trans))
        self.comboBox_unicode.setEnabled(False)
        self.lineEdit_topic_trans.setEnabled(False)
        self.lineEdit_trans_num.setEnabled(False)
        self.checkBox_trans_kafk.setEnabled(False)
        self.pushButton_stoprecv.setEnabled(False)
        self.pushButton_stopsend.setEnabled(False)
        self.pushButton_pausesend.setEnabled(False)
        if int(self._config['MsgTest']['kafka']) == 0:
            self.lineEdit_topick_send.setText(self._config['MsgTest']['msmqpath_producer'])
            self.lineEdit_topick_recv.setText(self._config['MsgTest']['msmqpath_consumer'])
        else:
            self.lineEdit_topick_send.setText(self._config['MsgTest']['topic_producer'])
            self.lineEdit_topick_recv.setText(self._config['MsgTest']['topic_consumer'])
        self.lineEdit_group.setText(self._config['MsgTest']['groupid'])
        self.lineEdit_topic_trans.setText(self._config['MsgTest']['topic_trans'])
        self.checkBox.setChecked(bool(int(self._config['MsgTest']['kafka'])))
        self._usekafka = bool(int(self._config['MsgTest']['kafka']))
        #self.lineEdit_topick_send.textChanged()
        #self.checkBox.stateChanged()
        self.signal_recv.connect(self.analyze,QtCore.Qt.QueuedConnection)



        self.label_status = QtWidgets.QLabel()
        self.statusbar.addWidget(self.label_status)
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self._showtime)
        self._timer.start(1000)

    def _showtime(self):
        self.label_status.setText(time.asctime())

    def set_partition(self,index):
        temp = self.comboBoxpartition.currentText()
        if temp == '-1':
            self.i_partition = None
        else:
            self.i_partition = int(temp)
        #print(self.i_partition)

    def on_checkBox_stateChanged(self,a0):
        self._config['MsgTest']['kafka'] = str(int(bool(a0)))
        self._usekafka = bool(a0)

    def on_checkBox_search_stateChanged(self,a0):
        self.lineEdit_topic_trans.setEnabled(a0)
        self.lineEdit_trans_num.setEnabled(a0)
        self.checkBox_trans_kafk.setEnabled(a0)
        self._kafka_trans.trans = a0

    def on_comboBox_unicode_currentIndexChanged(self,index):
        self._isold = bool(index)

    def on_checkBox_transmain_stateChanged(self,a0):
        print(a0)
        self.comboBox_unicode.setEnabled(a0)
        self.b_needtran = bool(a0)

    def on_lineEdit_trans_num_textChanged(self,a0):
        try:
            if a0 !='':
                self.num_trans = int(a0)
        except:
            print('error number')

    def on_lineEdit_topic_trans_textChanged(self,a0):
        self._config['MsgTest']['topic_trans'] = a0
        if self.checkBox_search.isChecked():
            self._kafka_trans.settopic_producer(a0)


    def on_lineEdit_topick_send_textChanged(self,a0):
        if int(self._config['MsgTest']['kafka']) == 1:
            self._config['MsgTest']['topic_producer'] = a0
            self._kafka.settopic_producer(a0)
        else:
            self._config['MsgTest']['msmqpath_producer'] = a0

    def on_lineEdit_topick_recv_textChanged(self,a0):
        if int(self._config['MsgTest']['kafka']) == 1:
            self._config['MsgTest']['topic_consumer'] = a0
        else:
            self._config['MsgTest']['msmqpath_consumer'] = a0

    def on_lineEdit_group_textChanged(self,a0):
        self._config['MsgTest']['groupid'] = a0

    def saveconfig(self):
        with open(os.getcwd()+'/config/config.ini','w',encoding='gbk') as f:
            self._config.write(f)


    def createconnections(self):
        self.comboBox_msgtype.currentIndexChanged()
        pass

    def on_comboBox_msgtype_currentIndexChanged(self,a0):
        print(a0)
        if isinstance(a0,int):
            self.stackedWidget.setCurrentIndex(a0)

    def on_pushButton_send_pressed(self):
        try:
            data = self._sendData[self.comboBox_msgtype.currentIndex()].getValue()
        except Exception as e:
            print(e)
            return
        try:
            if int(self._config['MsgTest']['kafka']) == 0:
                self._msmq.create_producer(self._config['MsgTest']['msmqpath_producer'])
                self._msmq.send(data)
            else:
                self._kafka.send(data,partition=self.i_partition)
            self.num_send += 1
        except Exception as e:
            print(e)


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
        try:
            self.b_start = True
            self._thread = threading.Thread(target= self.thread_send)
            self._thread.start()
            self.pushButton_stopsend.setEnabled(True)
            self.pushButton_threadsend.setEnabled(False)
            self.pushButton_pausesend.setEnabled(True)
        except Exception as e:
            print(e)

    def thread_send(self):
        data = self._sendData[self.comboBox_msgtype.currentIndex()].getValue()
        while self.b_start:
            try:
                self.num_send += 1
                data = self._sendData[self.comboBox_msgtype.currentIndex()].updatedata()
                if int(self._config['MsgTest']['kafka']) == 0:
                    self._msmq.send(data)
                else:
                    self._kafka.send(data,partition=self.i_partition)
            except Exception as e:
                print(e)

    def on_pushButton_stopsend_pressed(self):
        try:
            if self.b_start:
                self.b_start = False
                self._thread.join()
                self.num_send = 0
                self.pushButton_stopsend.setEnabled(False)
                self.pushButton_threadsend.setEnabled(True)
        except Exception as e:
            print(e)

    def on_pushButton_startrecv_pressed(self):
        self.checkBox.setEnabled(False)
        self.num_trans = 0xffffffff
        if self.checkBox_search.isChecked():
            self.num_trans = int(self.lineEdit_trans_num.text())
        if not self.checkBox_trans_kafk.isChecked() and self.checkBox_search.isChecked():
            try:
                self._msmq_trans.create_producer(self.lineEdit_topic_trans.text())
            except Exception as e:
                print(e)
                return

        if int(self._config['MsgTest']['kafka']) == 0:
            try:
                self._msmq.create_consumer(self._config['MsgTest']['msmqpath_consumer'])
                self._msmq.startiocp_recv(self.recv_func)
            except Exception as e:
                print(e)
                return
            pass
        else:
            self._kafka.create_consumer(self._config['MsgTest']['topic_consumer'],
                                    self._config['MsgTest']['groupid'])
            self._kafka.startiocp_recv(self.recv_func)

        self.pushButton_stoprecv.setEnabled(True)
        self.pushButton_startrecv.setEnabled(False)
        pass

    def on_pushButton_stoprecv_pressed(self):
        self.checkBox.setEnabled(True)
        if int(self._config['MsgTest']['kafka']) == 0:
            self._msmq.stopRecv()
        else:
            self._kafka.stopRecv()
        self.num_recv = 0
        self.pushButton_stoprecv.setEnabled(False)
        self.pushButton_startrecv.setEnabled(True)
        pass

    def on_pushButton_stoprecv_2_pressed(self):
        if self._brecv1:
            self._brecv1 = False
            self.num_trans = 1
            if (not self.checkBox_trans_kafk.isChecked()) and self.checkBox_search.isChecked():
                try:
                    ret = self._msmq_trans.create_producer(self.lineEdit_topic_trans.text())
                    if not ret:
                        self._brecv1 = True
                        return
                except Exception as e:
                    print(e)
                    return
            if int(self._config['MsgTest']['kafka']) == 0:
                try:
                    self._msmq.create_consumer(self._config['MsgTest']['msmqpath_consumer'])
                    self._msmq.startiocp_recv(self.recv_func,True)
                except Exception as e:
                    print(e)
                    return
                pass
            else:
                self._kafka.create_consumer(self._config['MsgTest']['topic_consumer'],
                                            self._config['MsgTest']['groupid'])
                self._kafka.startiocp_recv(self.recv_func)

    @SendFunc
    def send(self,msg,old,needtran):
        #print('send',self,msg,old,needtran)
        if self.checkBox_trans_kafk.isChecked():
            self._kafka_trans.send(msg)
        else:
            self._msmq_trans.send(msg)

    def recv_func(self,kafka_message):
        #print(kafka_message)
        self._brecv1 = True
        self.num_recv += 1
        self.pushButton_stoprecv_2.setEnabled(True)
        global _num_time
        #return True
        if self.checkBox_Play.isChecked() and not self.checkBox_search.isChecked():
            time.sleep(0.0001)
            self.signal_recv.emit(kafka_message)
        if self.num_recv < self.num_trans:
            if self.checkBox_search.isChecked():
                self.send(kafka_message, self._isold, self.b_needtran)
        else:
            if self.checkBox_search.isChecked():
                self.send(kafka_message, self._isold, self.b_needtran)
            return False
        return True



    def analyze(self,value):
        #print(value)
        try:
            self._sendData[self.comboBox_msgtype.currentIndex()].analyze(value)
        except Exception as e:
            print(e)
            print('analyze error')


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
        self.saveconfig()
        self.on_pushButton_stoprecv_pressed()
        self.on_pushButton_stopsend_pressed()
        self._msmq.close()
        self._msmq_trans.close()
        self._kafka.close()
        self._kafka_trans.close()
        event.accept()

    def on_actionKafkaTool_triggered(self):
        self.kafkatool.show()

    def on_actionSQLTool_triggered(self):
        self.sqltool.show()

    # def on_pushButton_min_pressed(self):
    #     filename = QtWidgets.QFileDialog.getOpenFileName(self,'选择配置',os.getcwd(),"*.ini")
    #     print(filename)
    #     if filename[1] and filename[0] != '':
    #         self._sendData[self.comboBox_msgtype.currentIndex()].loadMin(filename)

    # def on_pushButton_max_pressed(self):
    #     filename = QtWidgets.QFileDialog.getOpenFileName(self, '选择配置', os.getcwd(), "*.ini")
    #     print(filename)
    #     if filename[1] and filename[0] != '':
    #         self._sendData[self.comboBox_msgtype.currentIndex()].loadMax(filename)
