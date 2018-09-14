

from ctypes import *


def Pack(ctype_instance):
    return string_at(addressof(ctype_instance),sizeof(ctype_instance))

def UnPack(ctype,buf):
    cstring = create_string_buffer(buf)
    return cast(pointer(cstring),POINTER(ctype)).contents

class DispatchFixedHead(LittleEndianStructure):
    _fields_ = [
        ('Priority',c_ubyte),
        ('MsgId', c_longlong),
        ('ProductExtendId', c_uint),
        ('RealProductExtendId', c_uint),
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

