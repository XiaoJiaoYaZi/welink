

from SMessage import msg_header,EBmsMsgType,Node
from ctypes import *
import struct
from enum import Enum

__all__ = ['SubmitMonitorMsg','DispatchMonitorMsg','SResourceState','HisCenterMonitorData','HisPreDealMonitorData',
           'SHeartBeat','log_struct']

class SMonitorDataBase(msg_header):
    _fields_ = [
        ('_id', c_uint),
        ('_time', c_int64),
        ('_period', c_uint),
    ]

    __OneByte = struct.Struct("<6IiqI")
    def Value(self):
        return self.__OneByte.pack(*(
            self._length,
            self._type,
            self._version,
            self._offset,
            self._item_count,
            self._item_total_size,
            self._id,
            self._time,
            self._period
        ))
        pass

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self._length            =data[0]
        self._type              =data[1]
        self._version           =data[2]
        self._offset            =data[3]
        self._item_count        =data[4]
        self._item_total_size   =data[5]
        self._id                =data[6]
        self._time              =data[7]
        self._period            =data[8]

    def __len__(self):
        return self.__OneByte.size


class SubmitMonitorMsgDefine(Structure):
    _fields_ = [
        ("_succ",c_uint),
        ("_fail", c_uint),
        ("_succ_fee", c_uint),
    ]

    __OneByte = struct.Struct("<III")

    def Value(self):
        return self.__OneByte.pack(*(
            self._succ,
            self._fail,
            self._succ_fee
        ))

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self._succ      = data[0]
        self._fail      = data[1]
        self._succ_fee  = data[2]

    def __len__(self):
        return self.__OneByte.size

class SubmitMonitorMsg(Structure):
    class ItemIndex(Enum):
        ITEM_CNT     = 0

    _fields_ = [
        ("baseheader",SMonitorDataBase),
        ("define",SubmitMonitorMsgDefine)
    ]

    impl_version = 0x0001
    impl_type = EBmsMsgType.SUBMIT_MONITOR.value[0]
    kMaxMsgSize = 200
    kMaxCache = kMaxMsgSize

    def __init__(self):
        self.baseheader._item_count = self.ItemIndex.ITEM_CNT.value
        self.baseheader._offset = len(self.baseheader) + len(self.define)

    def write_header(self):
        self.baseheader._type = self.impl_type
        self.baseheader._version = self.impl_version
        self.baseheader._length = self.getsize()

    def clear(self):
        self.baseheader._item_total_size = 0
        self.baseheader._length = 0

    def getsize(self):
        return self.baseheader._offset

    def Value(self):
        return self.baseheader.Value() + self.define.Value()

    def fromBytes(self, b):
        l = len(self.baseheader)
        self.baseheader.fromBytes(b[:l])
        self.define.fromBytes(b[l:])


class DispatchMonitorMsgDefine(Structure):
    _fields_ = [
        ('dispatch_states',c_uint*32),
        ('dispatch_province',c_uint*36),
        ('dispatch_telcom',c_uint*8)
    ]

    __OneByte = struct.Struct('<76I')

    def Value(self):
        data = tuple([self.dispatch_states[i] for i in range(32)])+\
                tuple([self.dispatch_province[i] for i in range(36)])+\
            tuple([self.dispatch_telcom[i] for i in range(8)])
        return self.__OneByte.pack(*data)

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        for i in range(32):
            self.dispatch_states[i] = data[i]
        for i in range(32,68):
            self.dispatch_province[i] = data[i]
        for i in range(68,76):
            self.dispatch_telcom[i] = data[i]

    def __len__(self):
        return self.__OneByte.size


class DispatchMonitorMsg(Structure):
    class ItemIndex(Enum):
        ITEM_CNT     = 0

    _fields_ = [
        ("baseheader",SMonitorDataBase),
        ("define",DispatchMonitorMsgDefine)
    ]

    impl_version = 0x0001
    impl_type = EBmsMsgType.DISPATCH_MONITOR.value[0]
    kMaxMsgSize = 200
    kMaxCache = kMaxMsgSize

    def __init__(self):
        self.baseheader._item_count = self.ItemIndex.ITEM_CNT.value
        self.baseheader._offset = len(self.baseheader) + len(self.define)

    def write_header(self):
        self.baseheader._type = self.impl_type
        self.baseheader._version = self.impl_version
        self.baseheader._length = self.getsize()

    def clear(self):
        self.baseheader._item_total_size = 0
        self.baseheader._length = 0

    def getsize(self):
        return self.baseheader._offset

    def Value(self):
        return self.baseheader.Value() + self.define.Value()

    def fromBytes(self, b):
        l = len(self.baseheader)
        self.baseheader.fromBytes(b[:l])
        self.define.fromBytes(b[l:])

class SResourceStateDefine(Structure):
    _fields_ = [
        ('resourceId',c_int),
        ('reportTime', c_double),
        ('statisticsConfig', c_int),
        ('currentStock', c_int),
        ('lastStock', c_int),
        ('reportTimeInterval', c_int),
        ('submitTotal', c_int),
        ('currentSubmitSuccess', c_int),
        ('currentSubmitFail', c_int),
        ('reportTotal', c_int),
        ('currentReportSuccess', c_int),
        ('currentReportFail', c_int),
        ('moTotal', c_int),
        ('currentMoTotal', c_int),
        ('state', c_int)
    ]

    __OneByte = struct.Struct('<idiiiiiiiiiiiii')

    def Value(self):
        return self.__OneByte.pack(*(
                                    self.resourceId,
                                    self.reportTime,
                                    self.statisticsConfig,
                                    self.currentStock,
                                    self.lastStock,
                                    self.reportTimeInterval,
                                    self.submitTotal,
                                    self.currentSubmitSuccess,
                                    self.currentSubmitFail,
                                    self.reportTotal,
                                    self.currentReportSuccess,
                                    self.currentReportFail,
                                    self.moTotal,
                                    self.currentMoTotal,
                                    self.state
                                    ))

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self.resourceId             = data[0]
        self.reportTime             = data[1]
        self.statisticsConfig       = data[2]
        self.currentStock           = data[3]
        self.lastStock              = data[4]
        self.reportTimeInterval     = data[5]
        self.submitTotal            = data[6]
        self.currentSubmitSuccess   = data[7]
        self.currentSubmitFail      = data[8]
        self.reportTotal            = data[9]
        self.currentReportSuccess   = data[10]
        self.currentReportFail      = data[11]
        self.moTotal                = data[12]
        self.currentMoTotal         = data[13]
        self.state                  = data[14]

    def __len__(self):
        return self.__OneByte.size

class SResourceState(Structure):
    class ItemIndex(Enum):
        ITEM_CNT     = 0

    _fields_ = [
        ("baseheader",SMonitorDataBase),
        ("define",SResourceStateDefine)
    ]

    impl_version = 0x0001
    impl_type = EBmsMsgType.RESOURCE_MONITOR.value[0]
    kMaxMsgSize = 200
    kMaxCache = kMaxMsgSize

    def __init__(self):
        self.baseheader._item_count = self.ItemIndex.ITEM_CNT.value
        self.baseheader._offset = len(self.baseheader) + len(self.define)

    def write_header(self):
        self.baseheader._type = self.impl_type
        self.baseheader._version = self.impl_version
        self.baseheader._length = self.getsize()

    def clear(self):
        self.baseheader._item_total_size = 0
        self.baseheader._length = 0

    def getsize(self):
        return self.baseheader._offset

    def Value(self):
        return self.baseheader.Value()+self.define.Value()

    def fromBytes(self,b):
        l = len(self.baseheader)
        self.baseheader.fromBytes(b[:l])
        self.define.fromBytes(b[l:])

class HisPreDealMonitorDefine(Structure):
    _fields_ = [
        ('rcvCnt',c_long),
        ('perRcvCnt', c_long),
        ('mtchCnt', c_long),
        ('sndFldRsndCnt', c_long),
        ('repFldRsndCnt', c_long),
        ('repTmoutRsndCnt', c_long),
    ]

    __OneByte = struct.Struct('<6i')

    def Value(self):
        return self.__OneByte.pack(*(
                                    self.rcvCnt,
                                    self.perRcvCnt,
                                    self.mtchCnt,
                                    self.sndFldRsndCnt,
                                    self.repFldRsndCnt,
                                    self.repTmoutRsndCnt,
                                    ))

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self.rcvCnt         = data[0]
        self.perRcvCnt      = data[1]
        self.mtchCnt        = data[2]
        self.sndFldRsndCnt  = data[3]
        self.repFldRsndCnt  = data[4]
        self.repTmoutRsndCnt= data[5]

    def __len__(self):
        return self.__OneByte.size

class HisPreDealMonitorData(Structure):
    class ItemIndex(Enum):
        ITEM_CNT     = 0

    _fields_ = [
        ("baseheader",SMonitorDataBase),
        ("define",HisPreDealMonitorDefine)
    ]

    impl_version = 0x0001
    impl_type = EBmsMsgType.HISPREDEAL_MONITOR.value[0]
    kMaxMsgSize = 200
    kMaxCache = kMaxMsgSize

    def __init__(self):
        self.baseheader._item_count = self.ItemIndex.ITEM_CNT.value
        self.baseheader._offset = len(self.baseheader) + len(self.define)

    def write_header(self):
        self.baseheader._type = self.impl_type
        self.baseheader._version = self.impl_version
        self.baseheader._length = self.getsize()

    def clear(self):
        self.baseheader._item_total_size = 0
        self.baseheader._length = 0

    def getsize(self):
        return self.baseheader._offset

    def Value(self):
        return self.baseheader.Value()+self.define.Value()

    def fromBytes(self,b):
        l = len(self.baseheader)
        self.baseheader.fromBytes(b[:l])
        self.define.fromBytes(b[l:])

class HisCenterMonitorDefine(Structure):
    _fields_ = [
        ('preCnt',c_long),
        ('rcvMsgCnt', c_long),
        ('directInstCnt', c_long),
        ('repMtchCnt', c_long),
        ('repRtryMtchCnt', c_long),
        ('repDismtchCnt', c_long),
        ('moMsgCnt', c_long),
    ]

    __OneByte = struct.Struct('<7i')

    def Value(self):
        return self.__OneByte.pack(*(
                                    self.preCnt,
                                    self.rcvMsgCnt,
                                    self.directInstCnt,
                                    self.repMtchCnt,
                                    self.repRtryMtchCnt,
                                    self.repDismtchCnt,
                                    self.moMsgCnt,
                                ))

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self.preCnt         = data[0]
        self.rcvMsgCnt      = data[1]
        self.directInstCnt  = data[2]
        self.repMtchCnt     = data[3]
        self.repRtryMtchCnt = data[4]
        self.repDismtchCnt  = data[5]
        self.moMsgCnt       = data[6]

    def __len__(self):
        return self.__OneByte.size

class HisCenterMonitorData(Structure):
    class ItemIndex(Enum):
        ITEM_CNT     = 0

    _fields_ = [
        ("baseheader",SMonitorDataBase),
        ("define",HisCenterMonitorDefine)
    ]

    impl_version = 0x0001
    impl_type = EBmsMsgType.HISCENTER_MONITOR.value[0]
    kMaxMsgSize = 200
    kMaxCache = kMaxMsgSize

    def __init__(self):
        self.baseheader._item_count = self.ItemIndex.ITEM_CNT.value
        self.baseheader._offset = len(self.baseheader) + len(self.define)

    def write_header(self):
        self.baseheader._type = self.impl_type
        self.baseheader._version = self.impl_version
        self.baseheader._length = self.getsize()

    def clear(self):
        self.baseheader._item_total_size = 0
        self.baseheader._length = 0

    def getsize(self):
        return self.baseheader._offset

    def Value(self):
        return self.baseheader.Value()+self.define.Value()

    def fromBytes(self,b):
        l = len(self.baseheader)
        self.baseheader.fromBytes(b[:l])
        self.define.fromBytes(b[l:])


class SHeartBeatDefine(Structure):
    _fields_ = [
        ('timeInterval',c_int),
        ('alarmTime', c_double),
        ('stat', c_byte),
    ]

    __OneByte = struct.Struct('<idb')

    def Value(self):
        return self.__OneByte.pack(*(
                                self.timeInterval,
                                self.alarmTime,
                                self.stat,
                                ))

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self.alarmTime      = data[0]
        self.stat           = data[1]
        self.timeInterval   = data[2]

    def __len__(self):
        return self.__OneByte.size

class SHeartBeat(Structure):
    class ItemIndex(Enum):
        MOUDULE_CNT  = 0
        ITEM_CNT     = 1

    _fields_ = [
        ("msgheader",msg_header),
        ("define",SHeartBeatDefine),
        ('node',Node* ItemIndex.ITEM_CNT.value),
        ('alarm_module',c_char_p)
    ]

    impl_version = 0x0001
    impl_type = 0x01
    kMaxMsgSize = 200
    kMaxCache = kMaxMsgSize

    def __init__(self):
        self.msgheader._item_count = self.ItemIndex.ITEM_CNT.value
        self.msgheader._offset = len(self.msgheader) + len(self.define)

    def write_header(self):
        self.msgheader._type = self.impl_type
        self.msgheader._version = self.impl_version
        self.msgheader._length = self.getsize()

    def clear(self):
        self.msgheader._item_total_size = 0
        self.msgheader._length = 0

    def getsize(self):
        return self.msgheader._offset + self.msgheader._item_total_size + self.get_indexes_size()

    def get_indexes_size(self):
        return self.msgheader._item_count * len(self.node[0])

    def write_getsize(self,index,text):
        if index ==0:
            if isinstance(text,str):
                self.alarm_module = text.encode('utf_8')#+'\x00\x00'.encode('utf_8')
            else:
                raise TypeError(text)
            return len(self.alarm_module)+1
        else:
            raise ValueError(index)

    def __write_item(self,index,text):
        if index > self.msgheader._item_count:
            return False
        self.node[index].m_offset = self.msgheader._item_total_size
        size = self.write_getsize(index,text)
        self.node[index].m_size = size
        self.msgheader._item_total_size += size

    def write_alarm_module(self,text):
        self.__write_item(self.ItemIndex.MOUDULE_CNT.value,text)

    def Value(self):
        l=0
        for i in range(self.ItemIndex.ITEM_CNT.value):
            l+=self.node[i].m_size

        self.__OneByte = struct.Struct("<%ds" % (l,))
        # 定长
        value = self.msgheader.Value() + self.define.Value()
        # 动长node
        for i in range(self.ItemIndex.ITEM_CNT.value):
            value += self.node[i].Value()
        # 动长
        value += self.__OneByte.pack(*(self.alarm_module + b'\x00'
                                       ,))
        return value

    def fromBytes(self,b):
        b = bytearray(b)
        l1 = len(self.msgheader)
        l2 = len(self.define)
        l4 = len(self.node[0])
        l5 = self.msgheader._offset+self.ItemIndex.ITEM_CNT.value*l4
        self.msgheader.fromBytes(b[:l1])
        self.define.fromBytes(b[l1:l1+l2])
        for i in range(self.msgheader._item_count):
            self.node[i].fromBytes(b[l1+l2+i*l4:l1+l2+(i+1)*l4])
        self.alarm_module = bytes(b[l5+self.node[0].m_offset:l5+self.node[0].m_offset+self.node[0].m_size])

    @property
    def module(self):
        return self.alarm_module.decode('utf-8')

class log_struct_define(Structure):
    _fields_ = [
        ('level',c_int),
        ('ip', c_ulong),
        ('time', c_double),
    ]

    __OneByte = struct.Struct('<iid')

    def Value(self):
        return self.__OneByte.pack(*(
                                self.level,
                                self.ip,
                                self.time,
                                ))

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self.level  = data[0]
        self.ip     = data[1]
        self.time   = data[2]

    def __len__(self):
        return self.__OneByte.size

class log_struct(Structure):
    class ItemIndex(Enum):
        NAME_CNT    = 0
        MSG_CNT     = 1
        ITEM_CNT    = 2

    _fields_ = [
        ("msgheader",msg_header),
        ("define",log_struct_define),
        ('node',Node* ItemIndex.ITEM_CNT.value),
        ('name',c_char_p),
        ('msg', c_char_p)
    ]

    impl_version = 0x0001
    impl_type = 0x02
    kMaxMsgSize = 200
    kMaxCache = kMaxMsgSize

    def __init__(self):
        self.msgheader._item_count = self.ItemIndex.ITEM_CNT.value
        self.msgheader._offset = len(self.msgheader) + len(self.define)

    def write_header(self):
        self.msgheader._type = self.impl_type
        self.msgheader._version = self.impl_version
        self.msgheader._length = self.getsize()

    def clear(self):
        self.msgheader._item_total_size = 0
        self.msgheader._length = 0

    def getsize(self):
        return self.msgheader._offset + self.msgheader._item_total_size + self.get_indexes_size()

    def get_indexes_size(self):
        return self.msgheader._item_count * len(self.node[0])

    def write_getsize(self,index,text):
        if index ==0:
            if isinstance(text,str):
                self.name = text.encode('utf_8')#+'\x00\x00'.encode('utf_8')
            else:
                raise TypeError(text)
            return len(self.name)+1
        if index ==1:
            if isinstance(text,str):
                self.msg = text.encode('utf_8')#+'\x00\x00'.encode('utf_8')
            else:
                raise TypeError(text)
            return len(self.msg)+1
        else:
            raise ValueError(index)

    def __write_item(self,index,text):
        if index > self.msgheader._item_count:
            return False
        self.node[index].m_offset = self.msgheader._item_total_size
        size = self.write_getsize(index,text)
        self.node[index].m_size = size
        self.msgheader._item_total_size += size

    def write_name(self,text):
        self.__write_item(self.ItemIndex.NAME_CNT.value,text)
    def write_msg(self,text):
        self.__write_item(self.ItemIndex.MSG_CNT.value,text)


    def Value(self):
        l=0
        for i in range(self.ItemIndex.ITEM_CNT.value):
            l+=self.node[i].m_size

        self.__OneByte = struct.Struct("<%ds" % (l,))
        # 定长
        value = self.msgheader.Value() + self.define.Value()
        # 动长node
        for i in range(self.ItemIndex.ITEM_CNT.value):
            value += self.node[i].Value()
        # 动长
        value += self.__OneByte.pack(*(self.name + b'\x00',
                                       self.msg + b'\x00'
                                       ,))
        return value

    def fromBytes(self,b):
        b = bytearray(b)
        l1 = len(self.msgheader)
        l2 = len(self.define)
        l4 = len(self.node[0])
        l5 = self.msgheader._offset+self.ItemIndex.ITEM_CNT.value*l4
        self.msgheader.fromBytes(b[:l1])
        self.define.fromBytes(b[l1:l1+l2])
        for i in range(self.msgheader._item_count):
            self.node[i].fromBytes(b[l1+l2+i*l4:l1+l2+(i+1)*l4])
        self.name = bytes(b[l5+self.node[0].m_offset:l5+self.node[0].m_offset+self.node[0].m_size])
        self.msg = bytes(b[l5 + self.node[1].m_offset:l5 + self.node[1].m_offset + self.node[1].m_size])

    @property
    def names(self):
        return self.name.decode('utf-8')
    @property
    def msgs(self):
        return self.msg.decode('utf-8')