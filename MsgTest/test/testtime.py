import time

time.gmtime()




import ctypes
from ctypes import *
import os


class DispatchFixedHead(LittleEndianStructure):
    _fields_ = [
        ('Priority',c_char),
        ('MsgId', c_int64),
        ('ProductExtendId', c_int),
        ('RealProductExtendId', c_int),
        ('StartSendDateTime', c_double),
        ('EndSendDateTime', c_double),
        ('StartSendTime', c_double),
        ('EndSendTime', c_double),
        ('ChargeQuantity', c_int),
        ('MsgState', c_ubyte),
        ('MsgType', c_ubyte),
        ('CommitTime', c_double),
        ('Package', c_ushort),
        ('MobilesContentLen', c_uint),
        ('MsgContentLen', c_uint),
        ('MobilesCount', c_uint),
        ('DispatchTimes', c_uint),
        ('Telcom', c_char),
        ('ProvinceId', c_char),
        ('CityId', c_short),
        ('TPCBChecked', c_bool),
        ('SendedTimes', c_ubyte),
        ('DispatchFailedState', c_ubyte),
        ('SubmitType', c_ubyte),
        ('Telcom', c_int),
        ('CloudMsgTemplateID', c_int),
        ('CommitIp', c_uint)
    ]
    _pack_=1

class DispatchFixedTail(LittleEndianStructure):
    _fields_ = [
        ('pagetotal',c_ubyte),
        ('packagetotal', c_ushort),
        ('typeComponentParam', c_int),
        ('lastFailResourceId', c_int),
        ('failedType', c_ubyte),
        ('lastDiapatchTime', c_double),
        ('resourceSendTimes', c_ushort),
        ('auditorId', c_int),
        ('totalSendTimes', c_ubyte),
        ('repResendTimeOut', c_int),
        ('innerDispatchTimes', c_int),
        ('extComponentParam', c_int),
        ('m_old_struct', c_char)
    ]
    _pack_ = 1

class UserSubmitData(LittleEndianStructure):
    _fields_ = [
        ('head',DispatchFixedHead),
        ('tail',DispatchFixedTail),
        ('AccountId',c_char*32),
        ('ExtNumber', c_char*16),
        ('AccMsgId', c_char*64),
        ('Title', c_char*64),
        ('ResultCode', c_int),
        ('Password', c_char*50),
        ('FailReason', c_char*128),
        ('FailMobiles', c_char*120),
        ]
    _pack_ = 1

stru_info= create_string_buffer(sizeof(UserSubmitData))
p_rec = POINTER(UserSubmitData)(stru_info)

mobilesize = c_int(12)
contentsize = c_int(10)
submit_content = create_unicode_buffer(4096)
submit_content_size = c_int(4096)
submit_content_len = c_int(0)

mobiles = create_string_buffer("13000000000".encode('gbk'))
content = create_unicode_buffer('你好【微网通联】',4096)

##
data = UserSubmitData()
data.head.StartSendDateTime = 36352
data.head.EndSendDateTime = 36352
data.head.ProductExtendId = 1011618888
data.head.MobilesCount = 1
data.head.MsgType = 1
data.head.SubmitType = 1
data.head.ChargeQuantity = 1
data.AccountId = 'anbaili'.encode('gbk')
data.Password = 'anbaili9981'.encode('gbk')
data.ExtNumber = '66898'.encode('gbk')
data.AccMsgId = 'test'.encode('gbk')



os.chdir("D:\\svn\\msgplatform\\source\\生产平台\\短彩提交接口vs2015\\Source\\KafkaReceiver\\bin\\Debug")
dll = ctypes.CDLL("D:\\svn\\msgplatform\\source\\生产平台\\短彩提交接口vs2015\\Source\\KafkaReceiver\\bin\\Debug\\MsgSubmit.dll")
print(dll)
ret = dll.MsgSubmitInit()
print(ret)
ret = dll.Commit(byref(data),byref(mobiles),byref(content),12,12,byref(submit_content),4096,byref(submit_content_len))
print(ret)
print(submit_content)

dll.MsgSubmitUninit()