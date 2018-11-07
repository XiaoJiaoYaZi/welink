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
import pywintypes
import re

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
        self._t_recvOne =None
        self._trans = False

    def init(self):
        self.config.read(os.getcwd()+'/config/kafka_base.ini',encoding='gbk')
        print(self.config['broker']['bootstrap_servers'])
        self.__kafkconsume = {}
        self.__kafkaproduce = {}
        for item in self.config.items('broker'):
            self.__kafkconsume[item[0]] = item[1]
            self.__kafkaproduce[item[0]] = item[1]

        for item in self.config.items("produce"):
            self.__kafkaproduce[item[0]] = int(item[1])

        for item in self.config.items('consume'):
            result = re.findall('[a-zA-Z]+',item[1])
            if len(result) >0:
                self.__kafkconsume[item[0]] = result[0]
            else:
                self.__kafkconsume[item[0]] = int(item[1])
        print('producer config:\n',self.__kafkaproduce)
        print('consumer config:\n',self.__kafkconsume)

    @property
    def trans(self):
        return self._trans
    @trans.setter
    def trans(self,value):
        self._trans = value
        print(1,self._trans)

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
        try:
            topic = topic.strip()
            topic = topic.lower()
            if groupid is None or groupid == '':
                groupid = topic
            self._groupid = groupid
            self.__kafkconsume['group_id'] = groupid
            self.__consumer = KafkaConsumer(topic, **self.__kafkconsume)
        except Exception as e:
            print(e)
            raise  Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))

    def startiocp_recv(self,func):
        if not self.b_started:
            self.b_started = True
            self._thread = threading.Thread(target=self.__startrecv,args=(func,),daemon = True)
            self._thread.start()

    def __startrecv(self,func):
        while self.b_started:
            try:
                for message in self.__consumer:
                    if self.b_started:
                        if not func(message.value):
                            print('转移完成2')
                            return
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
        try:
            self._onerecvd = False
            self._t_recvOne = threading.Thread(target=self.__recvOne,args=(func,))
            self._t_recvOne.start()
            # self.timer=threading.Timer(5,self.__recverror)
            # self.timer.start()
        except Exception as e:
                print(e)
                raise Exception("module:{} func:{} line:{} error".format(
                    __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))

    def __recverror(self):
        try:
            if self._t_recvOne is not None:
                if self._t_recvOne.is_alive():
                    self._onerecvd = True
                    self._t_recvOne.join()
                    print("recv None in 5s exit")
        except Exception as e:
            print(e)

    def __recvOne(self,func):
        while not self._onerecvd:
            for message in self.__consumer:
                # with open('data.dat','wb') as f:
                #     f.write(message.value)
                func(message.value)
                self._onerecvd = True
                self._brecv1 = True
                break
        self.__consumer.close()
        print('recv succ')

    def kafkadetai(self):
        self.__consumer.offsets(self._groupid)
        #self.__consumer.offsets_for_times()

    def close(self):
        self.__recverror()
        if self.__producer is not None:
            self.__producer.close()
        if self.__consumer is not None:
            self.__consumer.close()


class MsMqManageer(object):
    def __init__(self):
        self._msg = win32com.client.Dispatch("MSMQ.MSMQMessage")
        self.b_started = False
        self._brecv1 = True
        self.t = None
        self.__consumer = None
        self.__producer = None

    def create_producer(self,topic):
        if self.__producer is not None:
            self.__producer.Close()
        qinfo = win32com.client.Dispatch('MSMQ.MSMQQueueInfo')
        qinfo.FormatName = topic
        try:
            self.__producer = qinfo.Open(2, 0)
        except Exception as e:
            print(e)
            raise Exception('create producer error')

    def settopic_producer(self,topic):
        pass

    def send(self,data):
        if isinstance(data,bytes):
            self._msg.Body = data
            #print(data)
            try:
                self._msg.Send(self.__producer)
            except Exception as e:
                print(e)

    def create_consumer(self,topic:str,groupid:str = None):
        qinfo = win32com.client.Dispatch('MSMQ.MSMQQueueInfo')
        qinfo.FormatName = topic
        try:
            self.__consumer = qinfo.Open(1, 0)
        except Exception as e:
            print(e)
            raise Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))
        pass

    def startiocp_recv(self,func):
        if not self.b_started:
            self.b_started = True
            self._thread = threading.Thread(target=self.__startrecv,args=(func,))
            self._thread.start()
        pass

    def __startrecv(self,func):
        print('start recv')
        while self.b_started:
            try:
                try:
                    msg = self.__consumer.Receive()
                except Exception as e:
                    print(e)
                    break
                #print(msg.Body.tobytes(),type(msg))
                if isinstance(msg.Body, memoryview):
                    func(msg.Body.tobytes())
                else:
                    func(msg.Body)
            except:
                print("recv error")
        print('thread end')
        pass

    def stopRecv(self):
        if self.b_started:
            self.b_started = False
            if self._thread:
                stop_thread(self._thread)
            self.__consumer.Close()
        pass


    def recvOne(self,func):
        try:
            self.t = threading.Thread(target=self.__recvOne,args=(func,))
            self.t.start()
            # ti = threading.Timer(5,self.__recverror)
            # ti.start()
        except  Exception as e:
            print(e)
            raise  Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))

    def __recverror(self):
        try:
            if self.t is not None:
                if self.t.is_alive():
                    stop_thread(self.t)
                    print("recv None in 5s exit")
        except Exception as e:
            print(e)

    def __recvOne(self,func):
        try:
            msg = self.__consumer.Receive()
            if isinstance(msg.Body,memoryview):
                func(msg.Body.tobytes())
            else:
                func(msg.Body)
            self.__consumer.Close()
            print('recv succ')
        except:
            print("Recv msg error")
        pass

    def kafkadetai(self):
        pass

    def close(self):
        self.__recverror()
        if self.__consumer is not None:
            self.__consumer.Close()
        if self.__producer is not None:
            self.__producer.Close()
        pass

def call(b):
    print(b)
if __name__ == "__main__":
    from pykafka import KafkaClient
    pass
    from kafka.structs import TopicPartition,OffsetRequestPayload,OffsetCommitRequestPayload,ListOffsetRequestPayload,OffsetFetchRequestPayload,OffsetAndMetadata,MetadataRequest,ConsumerMetadataRequest
    from kafka.client import SimpleClient,KafkaClient
    from kafka.protocol import create_message
    from kafka.protocol.offset import OffsetRequest_v0,OffsetResponse_v0
    from kafka.protocol.commit import *
    from kafka import SimpleConsumer
    from kafka.coordinator.protocol import *
    from kafka.coordinator.consumer import *
    from kafka.common import *
    from kafka.protocol.legacy import KafkaProtocol
    import kafka.protocol.api
    #
    # #producer = KafkaProducer(bootstrap_servers = '192.168.18.134:9092')
    # i=0
    # # while i<10:
    # #     producer.send(topic='0.0.0.0.kfk',value='hello'.encode('gbk'),partition=0)
    # #     i+=1
    consumer = KafkaConsumer('__consumer_offsets',group_id ='test' ,bootstrap_servers = '192.168.18.134:9092')
    for message in consumer:
        print(message.value)
        res = GroupCoordinatorResponse_v1.decode(message.value)
        res = KafkaProtocol.decode_offset_response(OffsetResponse_v0.decode(message.value))
    #
    #client = SimpleClient(hosts='10.1.63.126:9092,10.1.63.127:9092,10.1.63.128:9092')
    res = None
    #
    client = KafkaClient(bootstrap_servers='10.1.63.126:9092,10.1.63.127:9092,10.1.63.128:9092')
    #consumer = SimpleConsumer(client=client,group='test',topic='0.0.0.0.kfk')
    client.send(1,OffsetRequest_v0(replica_id=-1, topics=[('10.1.120.111.dispatchcentersave', [(0, -1, 1)])]))
    res = client.poll()
    client.send(1,OffsetFetchRequest_v1(consumer_group = '1.1.1.1.adispatchstatisticsmonitor',topics = [('1.1.1.1.adispatchstatisticsmonitor',[0])]))
    res = client.poll()

    client = SimpleClient(hosts='10.1.63.126:9092,10.1.63.127:9092,10.1.63.128:9092')
    while 1:
        res = client.send_metadata_request(MetadataRequest('0.0.0.0.kfk'))
        res = client.send_consumer_metadata_request(ConsumerMetadataRequest(['test']))
        res = client.send_offset_request(payloads=(OffsetRequestPayload('0.0.0.0.kfk',0,1000,99999999),))
        res = client.send_list_offset_request(payloads=(ListOffsetRequestPayload('0.0.0.0.kfk',0,1000),))
        res = client.send_offset_fetch_request_kafka((b'kafka-python',1,'test'),[OffsetFetchRequestPayload('0.0.0.0.kfk',0)])
    #
    #
    # from kafka import KafkaConsumer
    # #consumer = KafkaConsumer('0.0.0.0.kfk',group_id ='test' ,bootstrap_servers = '192.168.18.134:9092')
    # # for message in consumer:
    # #     print(message.value)
    # consumer = KafkaConsumer('0.0.0.0.kfk',group_id='test', bootstrap_servers='192.168.18.134:9092')
    # #consumer.assign([TopicPartition('0.0.0.0.kfk',0),])
    # partitions = consumer.partitions_for_topic('0.0.0.0.kfk')
    # #print(consumer.assignment())
    # print(consumer.beginning_offsets([TopicPartition('0.0.0.0.kfk',0),]))#起始偏移量
    # print(consumer.end_offsets([TopicPartition('0.0.0.0.kfk', 0), ]))#终止偏移量
    # print(consumer.committed(TopicPartition('0.0.0.0.kfk', 0)))
    # consumer.seek_to_beginning(TopicPartition('0.0.0.0.kfk',0))
    # consumer.seek(TopicPartition('0.0.0.0.kfk',0),0)
    # print(consumer.position(TopicPartition('0.0.0.0.kfk',0)))
    # consumer.close()
    # consumer = KafkaConsumer('0.0.0.0.kfk',group_id='test', bootstrap_servers='192.168.18.134:9092')
    #
    # for message in consumer:
    #     print(i,message.value)
    #     i+=1
    #
    # #all_consumed[partition] = OffsetAndMetadata(state.position, '')
    # #consumer.commit({TopicPartition('0.0.0.0.kfk',0):OffsetAndMetadata(0,'')})
    # consumer.close()

