from kafka import KafkaProducer,KafkaConsumer
from kafka.errors import *
import threading
from configparser import ConfigParser
import os
import win32com.client
import ctypes

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
                            self.__consumer.close()
                            self.b_started = False
                            print('接收完成')
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
        #self.__recverror()
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
            except Exception as e:
                print(e)
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


RECVFUNC = ctypes.CFUNCTYPE(None,ctypes.c_void_p,ctypes.c_int64)

class MsMqManageerDLL(object):
    def __init__(self):
        try:
            self._dll = ctypes.cdll.LoadLibrary('./dll/MSMQMoudle.dll')
        except Exception as e:
            print(e)
        self.b_started = False

    def create_producer(self,topic:str):
        try:
            ret = self._dll.API_CreateSender(topic.encode('gbk'))
            if ret != 1:
                print('create msmq sender failed,mq_name:',topic)
        except Exception as e:
            print(e)

    def settopic_producer(self):
        pass

    def send(self,data):
        if isinstance(data,bytes):
            self._dll.API_Send(data,len(data))
        elif isinstance(data,str):
            data = data.encode('gbk')
            self._dll.API_Send(data, len(data))
        else:
            raise Exception('wrong type',type(data))


    def create_consumer(self,topic:str,groupid:str = None):
        try:
            ret = self._dll.API_CreateReceiver(topic.encode('gbk'))
            if ret != 1:
                print('create msmq receiver failed,mq_name:',topic)
        except Exception as e:
            print(e)

    def _recv(self,msg,size):
        msg = ctypes.string_at(msg,size)
        #print(msg)
        return self._recvFunc(msg)


    def startiocp_recv(self,func,recvone = False):

        if not recvone:
            self._recvFunc = func
            self.recv = RECVFUNC(self._recv)
            self._dll.API_RecvOne.restype = ctypes.c_bool
            try:
                ret = self._dll.API_StartReceive(self.recv)
                if not ret:
                    print('start recv failed')
            except Exception as e:
                print(e)

        #self._recv_num = num
        else:
            if not self.b_started:
                self.b_started = True
                self._thread = threading.Thread(target=self.__startrecv,args=(func,))
                self._thread.start()

    def __startrecv(self,func):
        buf = ctypes.create_string_buffer(1024 * 1024 * 3)
        size = ctypes.c_int64(ctypes.sizeof(buf))
        self._dll.API_RecvOne.restype = ctypes.c_bool
        ret = 0
        while self.b_started:
            try:
                ret = self._dll.API_RecvOne(ctypes.pointer(buf), ctypes.byref(size))
                if ret:
                    ret = func(buf.raw[:size.value])
                    if not ret:
                        self._dll.API_CloseReceiver()
                        break
                else:
                    print('time out')
            except Exception as e:
                print(e)
        self.b_started = False
        buf =None
        print('__startrecv return')


        # self._recvFunc = func
        # self.recv = RECVFUNC(self._recv)
        # self._dll.API_RecvOne.restype = ctypes.c_bool
        # try:
        #     ret = self._dll.API_StartReceive(self.recv)
        #     if not ret:
        #         print('start recv failed')
        # except Exception as e:
        #     print(e)

    def recvOne(self,func):
        try:
            buf = ctypes.create_string_buffer(1024*1024*2)
            size = ctypes.c_int64(ctypes.sizeof(buf))
            ret = self._dll.API_RecvOne(ctypes.pointer(buf), ctypes.byref(size))
            if ret:
                func(buf.raw[:size.value])
                return
            #raise Exception('msmq recv one error')
        except Exception as e:
            print(e)

    def close(self):
        self._dll.API_CloseSender()
        self._dll.API_CloseReceiver()
        pass

    def stopRecv(self):
        if self.b_started:
            self.b_started = False
            self._thread.join()
            self._thread = None
        self._dll.API_CloseReceiver()


if __name__ == "__main__":
    pass

