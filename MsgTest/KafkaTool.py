from PyQt5 import QtWidgets, QtCore
from PyUI.UI_KafkaTool import Ui_KafkaTool
from pykafka import Cluster,handlers
from threading import Thread,Event,Lock
import time
from collections import namedtuple
from pykafka.protocol import PartitionOffsetFetchRequest
from PyQt5.QtWidgets import QTableWidgetItem


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
            # earlistoffset = descrips.earliest_available_offsets()
            # latestoffset = descrips.latest_available_offsets()
            topicdescrip = {}
            for id, partition in descrips.partitions.items():
                leader = partition.leader.id
                Replicas = []
                isr = []
                for i in partition.replicas:
                    Replicas.append(i.id)
                for i in partition.isr:
                    isr.append(i.id)
                # offsets1 = earlistoffset[id].offset[0]
                # offsets2 = latestoffset[id].offset[0]
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
        self._topic2consumer = {}


    def cancel(self):
        self.finished.set()

    def _get_group_descrips(self):
        start = time.time()
        consumers = self._cluster.get_managed_group_descriptions()
        print('use111 {}s'.format((time.time() - start)))
        start = time.time()
        self._consumer_descrips = Descrip4Consumer(consumers)
        print('use222 {}s'.format((time.time() - start)))

    def gettopic(self):
        return self._cluster.topics.keys()

    def _get_topic_descrips(self):
        start = time.time()
        with self._lock_topic:
            self._topic_descrips = Descrip4Topic(self._cluster.topics)
        print('use3333 {}s'.format((time.time() - start)))

    #待定是否实现topic到consumer的对应关系
    # def gettopic2consumer(self):
    #     consumers = self._cluster.get_managed_group_descriptions()
    #     for consumer in consumers:
    #

    def getoffsets(self,group_id):
        with self._lock_consumer:
            group_descrips = self._cluster.get_managed_group_descriptions()
            if group_id in group_descrips:
                if group_id == b'KafkaManagerOffsetCache':
                    return None
                descrips = group_descrips[group_id]
                if descrips[5] != {}:
                    descrip = {}
                    for member_id, groupMember in descrips[5].items():
                        partitions = groupMember[4].partition_assignment[0][1]
                        topics = groupMember[3].topic_names
                        for topic in topics:
                            reqs = [PartitionOffsetFetchRequest(topic, i) for i in
                                    self._cluster.topics[topic].partitions]
                            offset = self._cluster.get_group_coordinator(group_id).fetch_consumer_group_offsets(
                                group_id, reqs)

                            for partition in partitions:
                                descrip[partition] = ConsumerDescrip(partition,
                                                                      offset.topics[topic][partition].offset,
                                                                      group_id,
                                                                      member_id,
                                                                      groupMember[1],
                                                                      groupMember[2],
                                                                      groupMember[3].topic_names,
                                                                      )
                    print(descrip)
                    return descrip
                else:
                    descrip = {}
                    for i in range(8):
                        descrip[i] = ConsumerDescrip(i,
                                                 0,
                                                 b'-',
                                                 b'-',
                                                 b'-',
                                                 b'-',
                                                 [b'-'],
                                                 )
                    return descrip


                # topics = self._consumer_descrips.offsets[group_id][0].topic
                # descrip = {}
                # for topic in topics:
                #     reqs = [PartitionOffsetFetchRequest(topic,i)for i in  self._cluster.topics[topic].partitions]
                #     offset = self._cluster.get_group_coordinator(group_id).fetch_consumer_group_offsets(group_id,reqs)
                #
                #     print(offset.topics)

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
        print('update')
        start = time.time()
        self._cluster.update()
        #self._get_group_descrips()
        #self._get_topic_descrips()
        print('use {}s'.format((time.time()-start)))

    def run(self):
        while not self.finished.is_set():
            self._update()
            time.sleep(self._interval)

        print('run')




class KafkaTool(QtWidgets.QWidget,Ui_KafkaTool):
    sendCmd_signal = QtCore.pyqtSignal(str)
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


    def _createconnections(self):

        self.connect.pressed.connect(self._connect)
        self.unconnect.pressed.connect(self._unconnect)
        self.fresh.pressed.connect(self._fresh_topic)
        self.topic.doubleClicked.connect(self.showtopic)
        self.freshconsumer.pressed.connect(self._fresh_consumer)
        self.consumer.doubleClicked.connect(self.showconsumer)

    def _connect(self):
        self._host = self.host.text()
        try:
            self._cluster = ClusterManager(host=self._host)
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

    def _fresh_topic(self):
        try:
            self.topic.clear()
            topics = self._cluster.gettopic()

            for topic in topics:
                self.topic.addItem(topic.decode())
        except Exception as e:
            print(e)

    def showtopic(self,index):
        try:
            topic = index.data()
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
            self.consumer.clear()
            for consumer in consumers:
                self.consumer.addItem(consumer.decode('utf-8'))
        except Exception as e:
            print(e)

    def showconsumer(self,index):
        try:
            consumer = index.data()
            offsets = self._cluster.getoffsets(consumer.encode('utf-8'))
            if offsets is not None:
                topic = offsets[0].topic
                topicoffsets = self._cluster.getoffsets_topic(topic[0])
                print(topicoffsets)
                self.consumer_descrips.clear()
                self.consumer_descrips.setHorizontalHeaderLabels(['Partition','LogSize','Offset','Lag','group_id','member_id','client_id','client_host'])
                try:
                    for id,descrip in offsets.items():
                        self.consumer_descrips.setItem(id, 0, QTableWidgetItem(str(id)))
                        self.consumer_descrips.setItem(id, 1, QTableWidgetItem(str(topicoffsets[id].latist)))
                        self.consumer_descrips.setItem(id, 2, QTableWidgetItem(str(descrip.LogSize)))
                        self.consumer_descrips.setItem(id, 3, QTableWidgetItem(str(topicoffsets[id].latist-descrip.LogSize)))
                        self.consumer_descrips.setItem(id, 4, QTableWidgetItem(str(descrip.group_id.decode('utf-8'))))
                        self.consumer_descrips.setItem(id, 5, QTableWidgetItem(str(descrip.member_id.decode('utf-8'))))
                        self.consumer_descrips.setItem(id, 6, QTableWidgetItem(str(descrip.client_id.decode('utf-8'))))
                        self.consumer_descrips.setItem(id, 7, QTableWidgetItem(str(descrip.client_host.decode('utf-8'))))
                except Exception as e:
                    print(e)
        except Exception as e:
            print(e)
    def closeEvent(self,e):
        if self._started:
            self._unconnect()



if __name__ == '__main__':
    pass
    clust = ClusterManager('10.1.63.126:9092,10.1.63.127:9092,10.1.63.128:9092')
    clust.start()
    # time.sleep(5)
    # print(clust.getoffsets(b'10.1.120.111.dispatchcenter'))
    # time.sleep(20)
    # print(clust.getoffsets_topic(b'0.0.0.0.bmsaccount'))
    # pass