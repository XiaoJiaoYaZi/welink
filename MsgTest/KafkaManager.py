from kafka import KafkaProducer,KafkaConsumer
from kafka.errors import *
import threading
from configparser import ConfigParser
import queue
import os
import typing
import win32com.client


class KafkaManager(object):
    def __init__(self):
        super(KafkaManager,self).__init__()
        self.b_started = False
        self.config = ConfigParser()
        self.init()
        self.__producer = None
        self.__consumer = None

    def init(self):
        self.config.read(os.getcwd()+'/config/kafka_base.ini',encoding='utf-8')
        print(self.config['broker']['bootstrap_servers'])
        self.__kafkabase = {}

        for item in self.config.items('broker'):
            self.__kafkabase[item[0]] = item[1]

    def create_producer(self,topic):
        topic = topic.strip()
        topic = topic.lower()
        self._topick = topic
        self.__producer = KafkaProducer(bootstrap_servers=self.config['broker']['bootstrap_servers'])

    def settopic_producer(self,topic):
        topic = topic.strip()
        topic = topic.lower()
        self._topick = topic

    def send(self,data):
        if isinstance(data,bytes):
            self.__producer.send(self._topick,data)

    def create_consumer(self,topic:str,groupid:str = None):
        topic = topic.strip()
        topic = topic.lower()
        if groupid is None or groupid == '':
            groupid = topic
        self._groupid = groupid
        self.__kafkabase['group_id'] = groupid
        self.__consumer = KafkaConsumer(topic,**self.__kafkabase)

    def startiocp_recv(self,func):
        if not self.b_started:
            self.b_started = True
            self._thread = threading.Thread(target=self.__startrecv,args=(func,))
            self._thread.start()

    def __startrecv(self,func):
        while self.b_started:
            try:
                for message in self.__consumer:
                    if self.b_started:
                        func(message.value)
                    else:
                        break
                print('time out')
            except KafkaTimeoutError as e:
                print(e)
            except KafkaError as e:
                print(e)
            finally:
               pass
        print("__startrecv return")

    def stopRecv(self):
        if self.b_started:
            self.b_started = False
            self._thread.join()
            self.__consumer.close()


    def recvOne(self,func):
        t = threading.Thread(target=self.__recvOne,args=(func,))
        t.start()

    def __recvOne(self,func):
        recvd = False
        while not recvd:
            for message in self.__consumer:
                with open('data.dat','wb') as f:
                    f.write(message.value)
                func(message.value)
                recvd = True
                break
        self.__consumer.close()
        print('recv succ')

    def kafkadetai(self):
        self.__consumer.offsets(self._groupid)
        #self.__consumer.offsets_for_times()

    def close(self):
        if self.__producer is not None:
            self.__producer.close()
        if self.__consumer is not None:
            self.__consumer.close()


class MsMqManageer(object):
    def __init__(self):
        self._msg = win32com.client.Dispatch("MSMQ.MSMQMessage")

    def create_producer(self,topic):
        qinfo = win32com.client.Dispatch('MSMQ.MSMQQueueInfo')
        print(topic)
        qinfo.FormatName = topic
        self.__producer = qinfo.Open(2, 0)

    def settopic_producer(self,topic):
        pass

    def send(self,data):
        if isinstance(data,bytes):
            self._msg.Body = data
            self._msg.Send(self.__producer)

    def create_consumer(self,topic:str,groupid:str = None):
        qinfo = win32com.client.Dispatch('MSMQ.MSMQQueueInfo')
        qinfo.FormatName = topic
        self.__consumer = qinfo.Open(1, 0)
        pass

    def startiocp_recv(self,func):
        pass

    def __startrecv(self,func):
        pass

    def stopRecv(self):
        pass


    def recvOne(self,func):
        t = threading.Thread(target=self.__recvOne,args=(func,))
        t.start()

    def __recvOne(self,func):
        pass

    def kafkadetai(self):
        pass

    def close(self):
        pass