from PyQt5 import QtWidgets, QtCore,QtGui
from PyUI.UI_KafkaTool import Ui_KafkaTool
from PyUI.UI_Descrip_Consumer import Ui_Descrip
from PyUI.UI_ReadMessage import Ui_Dialog_ReadMessage
from PyUI.UI_Message import Ui_Message
from PyUI.UI_Search import Ui_FindMessage
from pykafka import Cluster,handlers
from threading import Thread,Event,Lock
from collections import namedtuple,defaultdict
from pykafka.protocol import PartitionOffsetFetchRequest,PartitionFetchRequest,message
from PyQt5.QtWidgets import QTableWidgetItem
from BMSMessage import m_key,m_keys_MonitorHeader
from CloudMsg import m_keys_umc
from SMessage import SBmsMessage,SBmsHisSendData,SBmsHisRepData,SBmsRepNotifyData,SBmsHisMOData,SBmsMoAccBlist
from MonitorMsgHeader import SBmsSubmitMonitorMsg,SBmsDispatchMonitorMsg,SBmsResourceState,SBmsHisCenterMonitorData,SBmsHisPreDealMonitorData,SBmsHeartBeat,SBmslog_struct
from PlatformPublicDefine import *
import pandas as np
import time

m_keys = m_key.copy()
for i in range(6,12):
    if i == 10 or i == 12:
        continue
    m_keys[i] = m_keys_MonitorHeader + m_key[i]
m_keys += m_keys_umc

Message_Type = [
    # region BMC
    SBmsMessage(),
    SBmsHisSendData(),
    SBmsHisRepData(),
    SBmsRepNotifyData(),
    SBmsHisMOData(),
    SBmsMoAccBlist(),
    SBmsSubmitMonitorMsg(),
    SBmsHisPreDealMonitorData(),
    SBmsHisCenterMonitorData(),
    SBmsResourceState(),
    SBmsHeartBeat(),
    SBmsDispatchMonitorMsg(),
    SBmslog_struct(),
    # endregion

    # region UMC
    SCloudMessage(),
    SMsgSendData(),
    SMsgHisRepData(),
    SMOData(),
    SRepNotifyData(),
    ResourceStateNotify(),
    SDispatchStatistics(),
    SResComStatistics(),
    SResourceState(),
    SPackageStatStruct(),
    SPackageStatStructRetry()
    # endregion
]

Message_Descrip = [
    '重客主消息数据',
    '重客历史预处理数据',
    '重客状态报告数据',
    '重客状态报告通知数据',
    '重客历史上行数据',
    '重客账号黑名单数据',
    '重客提交统计数据',
    '重客历史预处理统计数据',
    '重客历史中心统计数据',
    '重客资源状态数据',
    '重客心跳数据',
    '重客调度统计数据',
    '重客日志告警数据',

    ########################
    '云平台主消息数据',
    '云平台下行数据',
    '云平台状态报告数据',
    '云平台上行数据',
    '云平台状态报告通知数据',
    '云平台资源状态报告数据',
    '云平台调度统计数据',
    '云平台资源统计数据',
    '云平台资源状态数据',
    '云平台打包状态数据',
    '云平台导报状态重试数据',
]



# <editor-fold desc="MessageBox for Struct">
class Message(QtWidgets.QDialog,Ui_Message):
    def __init__(self,data,param,parent = None):
        super(Message,self).__init__(parent=parent)
        self.setupUi(self)
        self._init()
        self.pushButton_save.pressed.connect(self._saveMessages,QtCore.Qt.QueuedConnection)
        if param[0]:
            self._decode_byte(data)
        else:
            self._decode(data,param[2])

    def _init(self):
        self.messages = defaultdict()
        self._header = []

    def _decode_byte(self,data):
        self.treeWidget.clear()
        self.treeWidget.setHeaderLabels(['offset','value'])
        for temp in data:
            item = QtWidgets.QTreeWidgetItem(self.treeWidget,[str(temp.offset),str(temp.value)])
            self.treeWidget.addTopLevelItem(item)

    def _decode(self,data,type):
        self.treeWidget.clear()
        self._header = ['offset','timestamp']+list(m_keys[type])
        self.treeWidget.setHeaderLabels(self._header)
        for temp in data:
            try:
                Message_Type[type].fromBytes(temp.value)
                _data = [str(temp.offset),temp.timestamp_dt.strftime('%Y-%m-%d %H:%M:%S:%f')]+Message_Type[type].toList()
                item = QtWidgets.QTreeWidgetItem(self.treeWidget,_data)
                self.treeWidget.addTopLevelItem(item)
                self.messages[temp.offset] = _data
            except Exception as e:
                print(e)
                print('解析消息失败 offset:{}'.format(temp.offset))
                #self.treeWidget.addTopLevelItem(QtWidgets.QTreeWidgetItem(self.treeWidget,[str(temp.offset),str(temp.value)]))

    def _saveMessages(self):
        filename = QtWidgets.QInputDialog.getText(self,'保存文件','文件名')
        if not filename[1]:
            return
        #with open('./data/{}.csv'.format(filename[0]),'w') as f:
        data = [self._header] + [x for x in self.messages.values()]
        temp = np.DataFrame(data)
        temp.to_excel('./data/{}.xlsx'.format(filename[0]),header=False, index=False, encoding='utf-16')
# </editor-fold>

# <editor-fold desc="Read Meesage Box">
class ReadMsg(QtWidgets.QDialog,Ui_Dialog_ReadMessage):
    signal_messagecfg = QtCore.pyqtSignal(tuple)
    def __init__(self,parent = None):
        super(ReadMsg,self).__init__(parent=parent)
        self.setupUi(self)
        self.__initUI()
        self._createConnections()

    def __initUI(self):
        self.lineEdit.setText('0')

    def _showDescrip(self,index):
        QtWidgets.QToolTip.showText(QtGui.QCursor.pos(),Message_Descrip[index])

    def _createConnections(self):
        self.checkBox.clicked.connect(self.change)
        self.buttonBox.accepted.connect(self.onOK)
        self.comboBox.highlighted.connect(self._showDescrip)

    def change(self,checked):
        self.comboBox.setEnabled(not checked)

    def onOK(self):
        self.signal_messagecfg.emit((self.checkBox.isChecked(),int(self.lineEdit.text().strip()),self.comboBox.currentIndex()))
# </editor-fold>

# <editor-fold desc="Find Message Box">
class SearchMsg(QtWidgets.QDialog,Ui_FindMessage):
    signal_serarchCfg = QtCore.pyqtSignal(tuple)
    def __init__(self,parent = None):
        super(SearchMsg,self).__init__(parent=parent)
        self.setupUi(self)
        self._initUI()
        self._init()
        self._createConnections()

    def _initUI(self):
        #self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
        # self.lineEdit_min.setValidator(QtGui.QIntValidator(0,0xffffffff))
        # self.lineEdit_max.setValidator(QtGui.QIntValidator(0,0xffffffff))
        pass

    def _init(self):
        self._starttime = 0
        self._endtime = 0
        self._max = 0
        self._min = 0

    def _createConnections(self):
        self.buttonBox.accepted.connect(self.onOK)
        self.buttonBox.rejected.connect(self.close)

    def onOK(self):
        self._type = self.comboBox.currentIndex()
        if self.checkBox_time.isChecked():
            self._starttime = dt_Datetime(self.dateTimeEdit_start.dateTime().toPyDateTime().ctime())
            self._endtime = dt_Datetime(self.dateTimeEdit_end.dateTime().toPyDateTime().ctime())
        if self.checkBox_id.isChecked():
            self._max = int(self.lineEdit_max.text())
            self._min = int(self.lineEdit_min.text())
        self.signal_serarchCfg.emit((self._type,self._starttime,self._endtime,self._max,self._min))
        self.accept()

# </editor-fold>


# region namedtuple for kafka
ConsumerDescrip = namedtuple('ConsumerDescrip',
    ['Partition','LogSize','group_id','member_id','client_id','client_host','topic']
)

ConsumerOffsets = namedtuple('Consumers',
    ['consum_group','descrips']
)

Topic2Consumer = namedtuple('topic2consumer',
    ['topic','consumer']
)

TopicDescrip = namedtuple('TopicDescrip',
    ['Partition','Leader','Replicas','ISR','earlist','latist']
)
# endregion

class Descrip4Consumer(object):
    def __init__(self,descrip_consumer:dict):
        self._offsets = {}
        for group_id,descrip in descrip_consumer.items():
            if group_id == b'KafkaManagerOffsetCache':
                continue
            if descrip[5] != {}:
                descrips = {}
                for member_id,groupMember in descrip[5].items():
                    partitions = groupMember[4].partition_assignment[0][1]
                    for partition in partitions:
                        descrips[partition] = ConsumerDescrip(partition,
                                                             [0],
                                                             group_id,
                                                             member_id,
                                                              groupMember[1],
                                                              groupMember[2],
                                                              groupMember[3].topic_names,
                                                             )
                self._offsets[group_id] = descrips

    @property
    def offsets(self):
        return self._offsets

    def updateOffsets(self,group_id,offsets):
        for partition,offset in offsets:
            descrip = {}
            if group_id in self._offsets.keys():
                self._offsets[group_id][partition].LogSize[0] = offset.offset
            else:
                descrip[partition] = ConsumerDescrip(partition,
                                                     '-',
                                                     '-',
                                                     '-',
                                                     '-',
                                                     '-',
                                                     [''])

class Descrip4Topic(object):
    def __init__(self,topics):
        self._topicdescrip = {}
        for topic in topics:
            descrips = topics[topic]
            topicdescrip = {}
            for id, partition in descrips.partitions.items():
                leader = partition.leader.id
                Replicas = []
                isr = []
                for i in partition.replicas:
                    Replicas.append(i.id)
                for i in partition.isr:
                    isr.append(i.id)
                topicdescrip[id] = TopicDescrip(id, leader, Replicas, isr, [0], [0])

            self._topicdescrip[topic] = topicdescrip

    @property
    def descrips(self):
        return self._topicdescrip

    def updateoffsets(self,topic,partition,offset_earlist,offset_latest):
        if topic in self._topicdescrip:
            self._topicdescrip[topic][partition].earlist[0] = offset_earlist
            self._topicdescrip[topic][partition].latist[0] = offset_latest

class AutoLock:
    def __init__(self):
        self._lock = Lock()
    def __enter__(self):
        self._lock.acquire()
    def __exit__(self, exc_type, exc_val, exc_tb):
        self._lock.release()

class ClusterManager(Thread):
    def __init__(self,host,timeInterval = 1):
        Thread.__init__(self)
        self._host = host
        self._interval = timeInterval
        self.finished = Event()
        self._lock_consumer = AutoLock()
        self._lock_topic = AutoLock()
        self._handler = handlers.ThreadingHandler()
        self._cluster = Cluster(hosts=self._host,handler=self._handler,broker_version='0.11.0')
        self._topic2group = defaultdict(set)

    def cancel(self):
        self.finished.set()

    def gettopic(self):
        return self._cluster.topics.keys()

    def deletetopic(self,topic):
        for id,broker in self._cluster.brokers.items():
            try:
                ret = broker.delete_topics([topic,])
                print(ret)
            except Exception as e:
                pass
        pass

    #待定是否实现topic到consumer的对应关系
    def gettopic2group(self, topic):
        if topic in self._topic2group:
            return self._topic2group[topic]
        return {}

    def updatetopic2group(self):
        group_descrips = self._cluster.get_managed_group_descriptions()
        for group_id,descrips in group_descrips.items():
            if group_id == b'KafkaManagerOffsetCache' or descrips[5] == {}:
                continue
            for member_id,groupMember in descrips[5].items():
                topics = groupMember[3].topic_names
                for topic in topics:
                    self._topic2group[topic].add(group_id)

    def getoffsets(self,group_id):
        with self._lock_consumer:
            group_descrips = self._cluster.get_managed_group_descriptions()
            if group_id in group_descrips:
                if group_id == b'KafkaManagerOffsetCache':
                    return None
                descrips = group_descrips[group_id]
                if descrips[5] != {}:

                    descrip4topic = {}
                    for member_id, groupMember in descrips[5].items():
                        partitions = groupMember[4].partition_assignment[0][1]
                        topics = groupMember[3].topic_names
                        for topic in topics:
                            reqs = [PartitionOffsetFetchRequest(topic, i) for i in
                                    self._cluster.topics[topic].partitions]
                            offset = self._cluster.get_group_coordinator(group_id).fetch_consumer_group_offsets(
                                group_id, reqs)
                            descrip = {}
                            for partition in partitions:
                                descrip[partition] = ConsumerDescrip(partition,
                                                                      offset.topics[topic][partition].offset,
                                                                      group_id,
                                                                      member_id,
                                                                      groupMember[1],
                                                                      groupMember[2],
                                                                      groupMember[3].topic_names,
                                                                        )
                            descrip4topic[topic] = descrip
                    return descrip4topic
                else:
                    descrip = {}
                    descrip4topic = {}
                    for i in range(8):
                        descrip[i] = ConsumerDescrip(i,
                                                 0,
                                                 b'-',
                                                 b'-',
                                                 b'-',
                                                 b'-',
                                                 [b'-'],
                                                 )
                    descrip4topic[b''] = descrip
                    return descrip4topic
            return None

    def getoffsets_topic(self,topic):
        with self._lock_topic:
            if topic in self._cluster.topics:
                descrip = self._cluster.topics[topic]
                earlistoffset = descrip.earliest_available_offsets()
                latestoffset = descrip.latest_available_offsets()
                topicdescrip = {}
                for id, partition in descrip.partitions.items():
                    leader = partition.leader.id
                    Replicas = []
                    isr = []
                    for i in partition.replicas:
                        Replicas.append(i.id)
                    for i in partition.isr:
                        isr.append(i.id)
                    topicdescrip[id] = TopicDescrip(id, leader, Replicas, isr,
                                                    earlistoffset[id].offset[0],
                                                    latestoffset[id].offset[0])
                return topicdescrip
            else:
                topicdescrip = {}
                for i in range(8):
                    topicdescrip[i] = TopicDescrip(i,
                                                   0,
                                                   0,
                                                   0,
                                                   0,
                                                   0,
                                                   )
                return topicdescrip

    def getconsumers(self):
        return self._cluster.get_managed_group_descriptions().keys()

    def _update(self):
        start = time.time()
        self._cluster.update()
        self.updatetopic2group()
        print('update use : {}'.format(time.time()-start))

    def run(self):
        while not self.finished.is_set():
            self._update()
            time.sleep(self._interval)

        print('run end')

    def getMessage(self,broker,topic,partition,offset):
        request = PartitionFetchRequest(topic,partition,offset,1024*1024*2)
        message = self._cluster.brokers[broker].fetch_messages({request})
        return message.topics[topic][partition].messages

class Table_Consumer(Ui_Descrip,QtWidgets.QTableWidget):
    def __init__(self,topicoffsets,descrips:dict,parent = None):
        super(Table_Consumer,self).__init__(parent=parent)
        self.setupUi(self)
        self.setdata(topicoffsets,descrips)

    def setdata(self,topicoffsets,descrips:dict):
        for id, descrip in descrips.items():
            self.consumer_descrips.setItem(id, 0, QTableWidgetItem(str(id)))
            self.consumer_descrips.setItem(id, 1, QTableWidgetItem(str(topicoffsets[id].latist)))
            self.consumer_descrips.setItem(id, 2, QTableWidgetItem(str(descrip.LogSize)))
            self.consumer_descrips.setItem(id, 3, QTableWidgetItem(str(topicoffsets[id].latist - descrip.LogSize)))
            self.consumer_descrips.setItem(id, 4, QTableWidgetItem(str(descrip.group_id.decode('utf-8'))))
            self.consumer_descrips.setItem(id, 5, QTableWidgetItem(str(descrip.member_id.decode('utf-8'))))
            self.consumer_descrips.setItem(id, 6, QTableWidgetItem(str(descrip.client_id.decode('utf-8'))))
            self.consumer_descrips.setItem(id, 7, QTableWidgetItem(str(descrip.client_host.decode('utf-8'))))

class Table_Topic():
    pass


class ProgressBar(QtWidgets.QProgressBar):
    def __init__(self,parent = None):
        super().__init__(parent=parent)

    def _init(self):
        self.setStyleSheet('')
        self.setAlignment(QtCore.Qt.AlignHCenter)


class KafkaTool(QtWidgets.QWidget,Ui_KafkaTool):
    signal_find = QtCore.pyqtSignal(list)
    def __init__(self,parent = None):
        super(KafkaTool,self).__init__(parent=parent)
        self.setupUi(self)
        self._started = False
        self._initUi()
        self._createconnections()

    def _initUi(self):
        self.topic_decrips.setSpan(0, 6, 8, 1)
        self.unconnect.setEnabled(False)
        self.topic.setSortingEnabled(True)
        self.consumer.setSortingEnabled(True)
        self.stackedWidget.setEnabled(False)
        self.tabWidget.clear()
        self._initMenu()
        self.topic.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.topic_decrips.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.Dialog_ReadMsg = ReadMsg(self)
        self.Dialog_SearchMsg = SearchMsg(self)


    def _initMenu(self):
        self.topic_menu = QtWidgets.QMenu(self.topic)
        self.topic_menu.addAction(self.action_delete)
        self.topic_menu.addAction(self.action_fresh)

        self.topic_decrips_menu = QtWidgets.QMenu(self.topic_decrips)
        self.topic_decrips_menu.addAction(self.action_ReadMessage)
        self.topic_decrips_menu.addAction(self.action_findmessage)

    def _createconnections(self):
        self.connect.pressed.connect(self._connect)
        self.unconnect.pressed.connect(self._unconnect)
        self.fresh.pressed.connect(self._fresh_topic)
        self.topic.doubleClicked.connect(self.showtopic)
        self.freshconsumer.pressed.connect(self._fresh_consumer)
        self.consumer.doubleClicked.connect(self.showconsumer)
        self.lineEdit_search_topic.textChanged.connect(self.search_topic)
        self.lineEdit_search_consume.textChanged.connect(self.search_consume)
        self.topic.customContextMenuRequested.connect(self.show_topic_menu)
        self.action_delete.triggered.connect(self.delete_topic)
        self.action_fresh.triggered.connect(self._fresh_topic)
        self.topic_decrips.customContextMenuRequested.connect(self.showReadMenu)
        self.action_ReadMessage.triggered.connect(self.showgetMessage)
        self.Dialog_ReadMsg.signal_messagecfg.connect(self.ReadMessage,QtCore.Qt.QueuedConnection)
        self.action_findmessage.triggered.connect(self.findMessage)
        self.Dialog_SearchMsg.signal_serarchCfg.connect(self.searchMessage)

    def findMessage(self):
        self.Dialog_SearchMsg.exec()
        pass

    def searchMessage(self,param):
        thread = Thread(target=self._searchMessage,args=(param,),daemon=True)
        thread.start()

    def _searchMessage(self,param):
        print('start to search...')
        print(param)
        find_by_time = False
        if param[0]==0 and param[1]==0:
            find_by_time = True
        topic = self.topic.currentItem().text().encode('gbk')
        row = self.topic_decrips.currentItem().row()
        partition = int(self.topic_decrips.item(row,0).text())
        broker = int(self.topic_decrips.item(row,1).text())
        _max = int(self.topic_decrips.item(row,5).text())
        _min = int(self.topic_decrips.item(row,4).text())
        offset = _min
        messages = []
        while True:
            if offset>=_max:
                break
            message = self._cluster.getMessage(broker, topic, partition, offset)
            if find_by_time:
                _time_min = message[0].timestamp
                _time_max = message[-1].timestamp
                if _time_min > param[2]:#如果最小offset的时间戳比要找得数据时间戳的最大值还大，不可能找到
                    print('can not fine message min_time for offset:{},max_time for find:{}'.format(_time_min,param[2]))
                    break
                if _time_max <param[1]:#如果最大offset的时间戳比要找数据时间戳的最小值还小，直接去寻找下一段
                    offset += len(message)
                    continue
                for data in message:
                    if data.timestamp >=param[1] and data.timestamp <= param[2]:
                        messages.append(data)
                offset += len(messages)
                self.signal_find.emit(messages)
            else:
                _id_max = KafkaTool.getMsgId(Message_Type[param[0]].fromBytes(message[-1].value))
                _id_min = KafkaTool.getMsgId(Message_Type[param[0]].fromBytes(message[0].value))
                if _id_min > param[4]:
                    print('can not fine message min_msgid for offset:{},max_msgid for find:{}'.format(_id_min, param[4]))
                    break
                if _id_max < param[3]:
                    offset += len(message)
                    continue
                for data in message:
                    _id = KafkaTool.getMsgId(Message_Type[param[0]].fromBytes(message[-1].value))
                    if _id >= param[3] and _id <= param[4]:
                        messages.append(data)
                offset += len(messages)
                self.signal_find.emit(messages)
        return

    @classmethod
    def getMsgId(cls,data):
        if isinstance(data,SCloudMessage):
            return data.FixHead.MsgId
        elif isinstance(data,SMsgSendData):
            return data._body.msgId
        elif isinstance(data,SMOData):
            return data.msgId
        elif isinstance(data,SRepNotifyData):
            return data.msgId
        elif isinstance(data,SPackageStatStructRetry):
            return data.MsgId
        else:
            raise TypeError


    def showReadMenu(self,pos):
        self.topic_decrips_menu.exec(QtGui.QCursor.pos())

    def showgetMessage(self):
        self.Dialog_ReadMsg.exec()

    def ReadMessage(self,offset):
        print(offset)
        topic = self.topic.currentItem().text().encode('gbk')
        row = self.topic_decrips.currentItem().row()
        partition = int(self.topic_decrips.item(row,0).text())
        broker = int(self.topic_decrips.item(row,1).text())
        print(topic,partition,offset,broker)
        message = self._cluster.getMessage(broker,topic,partition,offset[1])
        label = Message(message,offset,self)
        label.exec()


    def show_topic_menu(self,pos):
        self.topic_menu.exec(QtGui.QCursor.pos())

    def delete_topic(self):
        topic = self.topic.currentItem().text()
        self._cluster.deletetopic(topic.encode('utf-8'))

    def _connect(self):
        self._host = self.host.text()
        try:
            self._cluster = ClusterManager(host=self._host,timeInterval=5)
            self._cluster.start()
            self._started = True
            self.stackedWidget.setEnabled(True)
            self.connect.setEnabled(False)
            self.unconnect.setEnabled(True)
        except Exception as e:
            print(e)

    def _unconnect(self):
        self._cluster.cancel()
        self._cluster.join(10)
        self._started = False
        self.stackedWidget.setEnabled(False)
        self.unconnect.setEnabled(False)
        self.connect.setEnabled(True)

    def search_topic(self,a0):
        num = self.topic.count()
        for i in range(num):
            self.topic.item(i).setHidden(True)
        items = self.topic.findItems(a0,QtCore.Qt.MatchContains)
        for item in items:
            item.setHidden(False)

    def search_consume(self,a0):
        num = self.consumer.count()
        for i in range(num):
            self.consumer.item(i).setHidden(True)
        items = self.consumer.findItems(a0,QtCore.Qt.MatchContains)
        for item in items:
            item.setHidden(False)

    def _fresh_topic(self):
        try:
            self.topic.clear()
            topics = self._cluster.gettopic()

            for topic in topics:
                self.topic.addItem(topic.decode())
        except Exception as e:
            print(e)

    def updategrouplist(self,group_ids):
        self.consumer.clear()
        for group_id in group_ids:
            self.consumer.addItem(group_id.decode('utf-8'))

    def showtopic(self,index):
        try:
            topic = index.data()
            group_ids = self._cluster.gettopic2group(topic.encode('utf-8'))
            self.updategrouplist(group_ids)
            offsets = self._cluster.getoffsets_topic(topic.encode('utf-8'))
            total_offset = 0
            self.topic_decrips.clear()
            self.topic_decrips.setHorizontalHeaderLabels(['分区','Leader','Replicas','ISR','最早偏移量','最晚偏移量','总偏移量'])
            for id,descrip in offsets.items():
                self.topic_decrips.setItem(id, 0, QTableWidgetItem(str(id)))
                self.topic_decrips.setItem(id, 1, QTableWidgetItem(str(descrip.Leader)))
                self.topic_decrips.setItem(id, 2, QTableWidgetItem(str(descrip.Replicas)))
                self.topic_decrips.setItem(id, 3, QTableWidgetItem(str(descrip.ISR)))
                self.topic_decrips.setItem(id, 4, QTableWidgetItem(str(descrip.earlist)))
                self.topic_decrips.setItem(id, 5, QTableWidgetItem(str(descrip.latist)))
                total_offset += descrip.latist
                #self.topic_decrips.setItem(id, 6, QTableWidgetItem(str(id)))
            self.topic_decrips.setItem(0,6,QTableWidgetItem(str(total_offset)))
        except Exception as e:
            print(e)

    def _fresh_consumer(self):
        try:
            consumers = self._cluster.getconsumers()
            self.updategrouplist(consumers)
        except Exception as e:
            print(e)

    def gettopic2group(self):
        pass

    def showconsumer(self,index):
        try:
            consumer = index.data()
            offsets4topic = self._cluster.getoffsets(consumer.encode('utf-8'))
            self.tabWidget.clear()
            if offsets4topic is not None:
                for topic,offsets in offsets4topic.items():
                    topicoffsets = self._cluster.getoffsets_topic(topic)
                    self.tabWidget.addTab(Table_Consumer(topicoffsets,offsets,self.tabWidget),topic.decode('utf-8','replace'))
        except Exception as e:
            print(e)

    def closeEvent(self,e):
        if self._started:
            self._unconnect()

if __name__ == '__main__':
    pass

