

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

class MyStruct(Structure):
    _fields_ = [
        ('a',c_int),
        ('b',c_double),
        ('c',c_char*32),
    ]
    _pack_ = 1

def callFunc(a,b):
    print('callbakcfunc',a,b)
    return a-b

if __name__ == '__main__':
    dll = cdll.LoadLibrary('D:\\users\\welink\\documents\\visual studio 2015\\Projects\\Testkafka\\x64\\Debug\\DLL1.dll')
    print(dll)
    print(dll.fnDLL1())

    dll.fnDLL3.restype = c_char_p
    type_p_int = POINTER(c_int)
    temp = type_p_int(c_int(0))

    print(dll.fnDLL2(1,c_float(2.0),c_double(3.0),'hell0'.encode('gbk'),temp))
    print('int *',temp,temp[0],temp.contents)
    res = dll.fnDLL3('hello'.encode('gbk'))
    print(res,type(res))
    buf = create_string_buffer('hello'.encode('gbk'),10)
    dll.fnDLL4(byref(buf),10)
    print(buf.value)

    mystruct = MyStruct()
    mystruct.a = 1
    mystruct.b = 1.0
    mystruct.c = 'helloworld'.encode('gbk')
    dll.fnDLL5(byref(mystruct))
    dll.fnDLL5(pointer(mystruct))
#pack
    print(string_at(addressof(mystruct),sizeof(mystruct)))
#unpack
    buf = create_string_buffer(sizeof(MyStruct))
    res = cast(pointer(buf),POINTER(MyStruct)).contents
    print(res,type(res))
    print('mystruct:',res.a,res.b,res.c)

    dll.fnDLL6.restype = MyStruct
    res = dll.fnDLL6()
    print(res)
    print('mystruct:', res.a, res.b, res.c)
    del res

# callback
    CMPFUNC = CFUNCTYPE(c_int,c_int,c_int)
    cmp_func = CMPFUNC(callFunc)
    dll.fnDLL7(1,2,cmp_func)











