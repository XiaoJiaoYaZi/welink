from PyQt5 import QtWidgets, QtCore,QtGui
from PyUI.UI_KafkaTool import Ui_KafkaTool
from PyUI.UI_Descrip_Consumer import Ui_Descrip
from PyUI.UI_ReadMessage import Ui_Dialog_ReadMessage
from pykafka import Cluster,handlers
from threading import Thread,Event,Lock
import time
from collections import namedtuple
from pykafka.protocol import PartitionOffsetFetchRequest,PartitionFetchRequest,message
from PyQt5.QtWidgets import QTableWidgetItem
from collections import defaultdict


class ReadMsg(QtWidgets.QDialog,Ui_Dialog_ReadMessage):
    signal_messagecfg = QtCore.pyqtSignal(tuple)
    def __init__(self,parent = None):
        super(ReadMsg,self).__init__(parent=parent)
        self.setupUi(self)
        self.__initUI()
        self._createConnections()

    def __initUI(self):
        pass

    def _createConnections(self):
        self.checkBox.clicked.connect(self.change)
        self.buttonBox.accepted.connect(self.onOK)

    def change(self,checked):
        self.comboBox.setEnabled(not checked)

    def onOK(self):
        self.signal_messagecfg.emit((self.checkBox.isChecked(),int(self.lineEdit.text().strip())))




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
        self._cluster = Cluster(hosts=self._host,handler=self._handler)
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

    def getMessage(self,topic,partition,offset):
        for id,broker in self._cluster.brokers.items():
            request = PartitionFetchRequest(topic,partition,offset,1024*1024*5)
            message = broker.fetch_messages({request})
            print(message)

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

class KafkaTool(QtWidgets.QWidget,Ui_KafkaTool):
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


    def _initMenu(self):
        self.topic_menu = QtWidgets.QMenu(self.topic)
        self.topic_menu.addAction(self.action_delete)
        self.topic_menu.addAction(self.action_fresh)

        self.topic_decrips_menu = QtWidgets.QMenu(self.topic_decrips)
        self.topic_decrips_menu.addAction(self.action_ReadMessage)

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
        self.Dialog_ReadMsg.signal_messagecfg.connect(self.ReadMessage)

    def showReadMenu(self,pos):
        self.topic_decrips_menu.exec(QtGui.QCursor.pos())

    def showgetMessage(self):
        self.Dialog_ReadMsg.show()

    def ReadMessage(self,partition):
        print(partition)


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

