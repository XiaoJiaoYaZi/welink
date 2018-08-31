from kafka import KafkaProducer,KafkaConsumer
from kafka.errors import *
import threading
from configparser import ConfigParser
import queue
import os
import typing
import win32com.client
import ctypes
import inspect


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stop_thread(thread):
    _async_raise(thread.ident, SystemExit)


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
        self.__kafkconsume = {}
        self.__kafkaproduce = {}
        for item in self.config.items('broker'):
            self.__kafkconsume[item[0]] = item[1]
            self.__kafkaproduce[item[0]] = item[1]

        for item in self.config.items("produce"):
            self.__kafkaproduce[item[0]] = int(item[1])

        for item in self.config.items('consume'):
            self.__kafkconsume[item[0]] = int(item[1])

    def create_producer(self,topic):
        topic = topic.strip()
        topic = topic.lower()
        self._topick = topic
        self.__producer = KafkaProducer(**self.__kafkaproduce)

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
        self.__kafkconsume['group_id'] = groupid
        self.__consumer = KafkaConsumer(topic, **self.__kafkconsume)

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
        self._t_recvOne = threading.Thread(target=self.__recvOne,args=(func,))
        self._t_recvOne.start()
        self.timer=threading.Timer(5,self.__recverror)
        self.timer.start()

    def __recverror(self):
        if self._t_recvOne.is_alive():
            self._onerecvd = True
            self._t_recvOne.join()
            self._t_recvOne = None
            print("recv None in 5s exit")

    def __recvOne(self,func):
        self._onerecvd = False
        while not self._onerecvd:
            for message in self.__consumer:
                with open('data.dat','wb') as f:
                    f.write(message.value)
                func(message.value)
                self._onerecvd = True
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
        self.b_started = False

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
        if not self.b_started:
            self.b_started = True
            self._thread = threading.Thread(target=self.__startrecv,args=(func,))
            self._thread.start()
        pass

    def __startrecv(self,func):
        while self.b_started:
            try:
                msg = self.__consumer.Receive()
                if isinstance(msg.Body, memoryview):
                    func(msg.Body.tobytes())
                else:
                    func(msg.Body)
            except:
                print("recv error")
        pass

    def stopRecv(self):
        if self.b_started:
            self.b_started = False
            self._thread.join()
            self.__consumer.Close()
        pass


    def recvOne(self,func):
        global t
        t = threading.Thread(target=self.__recvOne,args=(func,))
        t.start()
        threading.Timer(5,self.__recverror)

    def __recverror(self):
        if t.is_alive():
            stop_thread(t)

    def __recvOne(self,func):
        try:
            msg = self.__consumer.Receive()
            if isinstance(msg.Body,memoryview):
                func(msg.Body.tobytes())
            else:
                func(msg.Body)
        except:
            print("Recv msg error")
        pass

    def kafkadetai(self):
        pass

    def close(self):
        if self.__consumer is not None:
            self.__consumer.Close()
        if self.__producer is not None:
            self.__producer.Close()
        pass