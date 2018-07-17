from kafka import KafkaProducer,KafkaConsumer,KafkaClient
from kafka.structs import TopicPartition
from ctypes import *
from enum import Enum
import threading
import time
class msg_header(Structure):
    _fields_ = [
        ('_length',c_uint),

    ]
class MyEnum(c_int):
    a = 0
    b = 1
    c = 1
    d = 1


print(sizeof(MyEnum))
from SMessage import SBmsMessage,SHisSendData
print(MyEnum.a)
def worker():
    producer = KafkaProducer(bootstrap_servers = '192.168.18.134:9092')
    # msg = SBmsMessage()
    # msg.write_mobile('123123')
    # msg.write_message("你好")
    # msg.write_sign("签名")
    # msg.write_extnumber('123123')
    # msg.write_acc_msgid('123123')
    # msg.write_mms_title("标题")
    # msg.write_mms_path("123123")
    # msg.write_header()
    msg = SHisSendData()
    msg.Data.timeStamp = int(time.time())
    msg.write_message('你好')
    msg.write_whlMsg('你好，整包信息')
    msg.write_sign('【签名】')
    msg.write_spno('1069')
    msg.write_extnum('8888')
    msg.write_accmsgid('12132')
    msg.write_sendresult('222')
    msg.write_title('标题')
    msg.write_header()
    data = msg.Value()
    while 1:
        #for i in range(10):
        producer.send('2.1.1.1.python-test',value=msg.Value())



t = threading.Thread(target=worker)
t.start()


