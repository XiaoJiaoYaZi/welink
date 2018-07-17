from ctypes import *
import struct
from enum import Enum



class EBmsMsgType(Enum):

    #0x100起为平台基础传输信息类型
    MSG_SUBMIT = 0x100,

    #0x200起为历史或状态报告相关信息类型
    MSG_HIS_MT = 0x200,
    MSG_HIS_REP = 0x201,
    MSG_HIS_MO = 0x202,
    MSG_RPT_MO = 0x203,
    MSG_HIS_REMT = 0x204,
    MSG_REP_NTF = 0x205,

    #0x500起为业务处理信息类型
    MSG_NEED_REGIST_SIGN = 0x500,
    MSG_NEED_ACCBLIST = 0x501,


    #0x1000起为监控信息类型
    SUBMIT_MONITOR = 0x1000,
    FEECENTER_MONITOR = 0x1001,
    DISPATCH_MONITOR = 0x1002,
    RESOURCE_MONITOR = 0x1003,
    TIMESCAN_MONITOR = 0x1004,
    HISPREDEAL_MONITOR = 0x1005,
    HISCENTER_MONITOR = 0x1006,
    RESSTANOTIFY_MONITOR = 0x1007,
    RESCOMSTATIS_MONITOR = 0x1008,
    ALLOW_MONITOR =0x1080


class msg_header(Structure):
    _fields_ = [("_length",c_uint),
                ("_type", c_uint),
                ("_version", c_uint),
                ("_offset", c_uint),
                ("_item_count", c_uint),
                ("_item_total_size", c_uint),
    ]
    __OneByte = struct.Struct("<6I")

    def Value(self):
        return self.__OneByte.pack(*(self._length,self._type,self._version,
                                     self._offset,self._item_count,self._item_total_size))

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self._length = data[0]
        self._type = data[1]
        self._version = data[2]
        self._offset = data[3]
        self._item_count = data[4]
        self._item_total_size = data[5]

    def __len__(self):
        return self.__OneByte.size


class SBmsMessageDispatchHead(Structure):
    _fields_ = [
        ("Priority",c_ubyte),
        ("MsgFormat", c_ubyte),
        ("MsgId", c_int64),
        ("PrdExId", c_uint),
        ("SubmitPrdExId", c_uint),
        ("StartSendDateTime", c_double),
        ("EndSendDateTime", c_double),
        ("StartSendTime", c_double),
        ("EndSendTime", c_double),
        ("CommitTime", c_double),
        ("ChargeQuantity", c_int),
        ("MsgState", c_ubyte),
        ("MsgType", c_ubyte),
        ("MobilesCount", c_uint),
        ("SubmitType", c_ubyte),
        ("AccId", c_int),
        ("AuditorId", c_int),
        ("CommitIp", c_ulong)
    ]
    field = {
        "Priority":0,

    }
    __OneByte = struct.Struct("<BBqIIdddddiBBIBiiL")

    def Value(self):
        return self.__OneByte.pack(*(self.Priority,self.MsgFormat,self.MsgId,
                                     self.PrdExId, self.SubmitPrdExId, self.StartSendDateTime,
                                     self.EndSendDateTime, self.StartSendTime, self.EndSendTime,
                                     self.CommitTime, self.ChargeQuantity, self.MsgState, self.MsgType,
                                     self.MobilesCount, self.SubmitType, self.AccId, self.AuditorId,
                                     self.CommitIp
                                    ))

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self.Priority = data[0]
        self.MsgFormat = data[1]
        self.MsgId = data[2]
        self.PrdExId = data[3]
        self.SubmitPrdExId = data[4]
        self.StartSendDateTime = data[5]
        self.EndSendDateTime = data[6]
        self.StartSendTime = data[7]
        self.EndSendTime = data[8]
        self.CommitTime = data[9]
        self.ChargeQuantity = data[10]
        self.MsgState = data[11]
        self.MsgType = data[12]
        self.MobilesCount = data[13]
        self.SubmitType = data[14]
        self.AccId = data[15]
        self.AuditorId = data[16]
        self.CommitIp = data[17]


    def __len__(self):
        return self.__OneByte.size


class SBmsMessageDispatchTail(Structure):
    _fields_ = [
        ("InnerDispatchTimes",c_int),
        ("Pagetotal", c_ubyte),
        ("FlagBits", c_int64),
        ("LastFailResId", c_int),
        ("FailedType", c_ubyte),
        ("FailedState", c_ubyte),
        ("LastDiapatchTime", c_double),
        ("ResSendTimes", c_ushort),
        ("TotalSndFldResndTimes", c_ubyte),
        ("TotalRepFldResndTimes", c_ubyte),
        ("PackageTotal", c_int),
        ("PackageNum", c_int)
    ]

    __OneByte = struct.Struct("<iBqiBBdHBBii")

    def Value(self):
        return  self.__OneByte.pack(*(self.InnerDispatchTimes,self.Pagetotal,
                                      self.FlagBits,self.LastFailResId,
                                      self.FailedType,self.FailedState,
                                      self.LastDiapatchTime,self.ResSendTimes,
                                      self.TotalSndFldResndTimes,self.TotalRepFldResndTimes,
                                      self.PackageTotal,self.PackageNum))

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self.InnerDispatchTimes = data[0]
        self.Pagetotal = data[1]
        self.FlagBits = data[2]
        self.LastFailResId = data[3]
        self.FailedType = data[4]
        self.FailedState = data[5]
        self.LastDiapatchTime = data[6]
        self.ResSendTimes = data[7]
        self.TotalSndFldResndTimes = data[8]
        self.TotalRepFldResndTimes = data[9]
        self.PackageTotal = data[10]
        self.PackageNum = data[11]

    def __len__(self):
        return self.__OneByte.size


class Node(Structure):
    _fields_ = [
        ("m_offset",c_uint),
        ("m_size", c_uint),
    ]

    __OneByte = struct.Struct("<II")
    def Value(self):
        return self.__OneByte.pack(*(self.m_offset,self.m_size))


    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self.m_offset = data[0]
        self.m_size = data[1]

    def __len__(self):
        return self.__OneByte.size



    @classmethod
    def len(cls):
        return cls.__len__(cls)



class SBmsMessage(Structure):
    class EBmsMsgItem(Enum):
        EBMI_MOBILE = 0					#///号码
        EBMI_CONTENT  = 1                    #///<短信内容
        EBMI_SIGN	=2					       # ///签名(内容中不再包含签名)
        EBMI_EXT_NUMBER=3                #///extend number
        EBMI_ACC_MSGID   =4                #///客户自定义参数
        EBMI_MMS_TITLE     =5              #  ///彩信标题
        EBMI_MMS_FILENAME   =6        # ///彩信存储文件路径名称
        EBMI_ITEM_COUNT=7


    _fields_ = [
        ("msgheader",msg_header),
        ("SBmsMsgHead", SBmsMessageDispatchHead),
        ("SBmsMsgTail", SBmsMessageDispatchTail),
        ("node", Node * EBmsMsgItem.EBMI_ITEM_COUNT.value),

    ]
    _mobile      =None
    message     =None
    sign        =None
    extnumber   =None
    accmsgid    =None
    title       =None
    mmsfilename =None
    impl_version = 0x10
    impl_type = EBmsMsgType.MSG_SUBMIT.value[0]
    kMaxMsgSize = 8 * 1024
    kMaxCache = kMaxMsgSize + 256

    def Value(self):
        l = 0
        for i in range(self.EBmsMsgItem.EBMI_ITEM_COUNT.value):
            l+=self.node[i].m_size
        self.__OneByte = struct.Struct("<%ds" %(l,))
        #定长
        value = self.msgheader.Value()+self.SBmsMsgHead.Value()+self.SBmsMsgTail.Value()
        #动长node
        for i in range(self.EBmsMsgItem.EBMI_ITEM_COUNT.value):
            value += self.node[i].Value()
        #动长
        value +=self.__OneByte.pack(*(self._mobile + b'\x00' +
                                      self.message +b'\x00\x00' +
                                      self.sign +b'\x00\x00' +
                                      self.extnumber +b'\x00' +
                                      self.accmsgid +b'\x00' +
                                      self.title +b'\x00\x00' +
                                      self.mmsfilename +b'\x00',))
        return value

    def fromBytes(self,b):
        b = bytearray(b)
        l1 = len(self.msgheader)
        l2 = len(self.SBmsMsgHead)
        l3 = len(self.SBmsMsgTail)
        l4 = len(self.node[0])
        l5 = self.msgheader._offset+7*l4
        self.msgheader.fromBytes(b[:l1])
        self.SBmsMsgHead.fromBytes(b[l1:l1+l2])
        self.SBmsMsgTail.fromBytes(b[l1+l2:l1+l2+l3])
        for i in range(self.msgheader._item_count):
            self.node[i].fromBytes(b[l1+l2+l3+i*l4:l1+l2+l3+(i+1)*l4])
        self._mobile     = bytes(b[l5 + self.node[0].m_offset:l5 + self.node[0].m_offset + self.node[0].m_size])
        self.message    = bytes(b[l5+self.node[1].m_offset:l5+self.node[1].m_offset+self.node[1].m_size])
        self.sign       = bytes(b[l5+self.node[2].m_offset:l5+self.node[2].m_offset+self.node[2].m_size])
        self.extnumber  = bytes(b[l5+self.node[3].m_offset:l5+self.node[3].m_offset+self.node[3].m_size])
        self.accmsgid   = bytes(b[l5+self.node[4].m_offset:l5+self.node[4].m_offset+self.node[4].m_size])
        self.title      = bytes(b[l5+self.node[5].m_offset:l5+self.node[5].m_offset+self.node[5].m_size])
        self.mmsfilename= bytes(b[l5+self.node[6].m_offset:l5+self.node[6].m_offset+self.node[6].m_size])

    def __init__(self):
        self.msgheader._item_count = self.EBmsMsgItem.EBMI_ITEM_COUNT.value
        self.msgheader._offset = len(self.msgheader)+len(self.SBmsMsgHead)+len(self.SBmsMsgTail)

    def write_header(self):
        self.msgheader._type = self.impl_type
        self.msgheader._version = self.impl_version
        self.msgheader._length = self.getsize()

    def clear(self):
        self.msgheader._item_total_size = 0
        self.msgheader._length = 0

    def getsize(self):
        return self.msgheader._offset + self.msgheader._item_total_size+self.get_indexes_size()

    def get_indexes_size(self):
        return self.msgheader._item_count*len(self.node[0])

    def remove_item(self,index):
        if index > self.msgheader._item_count:
            return False
        pass

    def write_items(self,*args):
        pass

    def write_getsize(self,index,text):
        if index ==0:
            if isinstance(text,str):
                self._mobile = bytes(text, encoding='utf-8')
            else:
                raise TypeError(text)
            return len(self._mobile) + 1
        elif index == 1:
            if isinstance(text,str):
                self.message = text.encode('utf_16_le')
            else:
                raise TypeError(text)
            return len(self.message)+2
        elif index == 2:
            if isinstance(text,str):
                self.sign = text.encode('utf_16_le')
            else:
                raise TypeError(text)
            return len(self.sign)+2
        elif index == 3:
            if isinstance(text,str):
                self.extnumber = bytes(text,encoding='utf-8')
            else:
                raise TypeError(text)
            return len(self.extnumber)+1
        elif index == 4:
            if isinstance(text,str):
                self.accmsgid = bytes(text,encoding='utf-8')
            else:
                raise TypeError(text)
            return len(self.accmsgid)+1
        elif index == 5:
            if isinstance(text,str):
                self.title = text.encode('utf_16_le')
            else:
                raise TypeError(text)
            return len(self.title)+2
        elif index == 6:
            if isinstance(text,str):
                self.mmsfilename = bytes(text,encoding='utf-8')
            else:
                raise TypeError(text)
            return len(self.mmsfilename)+1
        else:
            raise ValueError(index)

    def __write_item(self,index,text):
        if index > self.msgheader._item_count:
            return False
        #self.remove_item(index)
        self.node[index].m_offset = self.msgheader._item_total_size
        size = self.write_getsize(index,text)
        self.node[index].m_size = size
        self.msgheader._item_total_size += size

    def write_mobile(self,text):
        self.__write_item(SBmsMessage.EBmsMsgItem.EBMI_MOBILE.value,text)
    def write_message(self,text):
        self.__write_item(SBmsMessage.EBmsMsgItem.EBMI_CONTENT.value, text)
    def write_sign(self,text):
        self.__write_item(SBmsMessage.EBmsMsgItem.EBMI_SIGN.value, text)
    def write_extnumber(self,text):
        self.__write_item(SBmsMessage.EBmsMsgItem.EBMI_EXT_NUMBER.value, text)
    def write_acc_msgid(self,text):
        self.__write_item(SBmsMessage.EBmsMsgItem.EBMI_ACC_MSGID.value, text)
    def write_mms_title(self,text):
        self.__write_item(SBmsMessage.EBmsMsgItem.EBMI_MMS_TITLE.value, text)
    def write_mms_path(self,text):
        self.__write_item(SBmsMessage.EBmsMsgItem.EBMI_MMS_FILENAME.value, text)

    @property
    def messages(self):
        return self.message.decode('utf_16_le')
    @messages.setter
    def messages(self,value):
        self.__write_item(SBmsMessage.EBmsMsgItem.EBMI_CONTENT.value, value)
    @property
    def signs(self):
        return self.sign.decode('utf_16_le')
    @signs.setter
    def signs(self,value):
        self.__write_item(SBmsMessage.EBmsMsgItem.EBMI_SIGN.value, value)
    @property
    def extnumbers(self):
        return self.extnumber.decode('utf-8')
    @extnumbers.setter
    def extnumbers(self,value):
        self.__write_item(SBmsMessage.EBmsMsgItem.EBMI_EXT_NUMBER.value, value)
    @property
    def accmsgids(self):
        return self.accmsgid.decode('utf-8')
    @accmsgids.setter
    def accmsgids(self,value):
        self.__write_item(SBmsMessage.EBmsMsgItem.EBMI_ACC_MSGID.value, value)
    @property
    def titles(self):
        return self.title.decode('utf_16_le')
    @titles.setter
    def titles(self,value):
        self.__write_item(SBmsMessage.EBmsMsgItem.EBMI_MMS_TITLE.value, value)
    @property
    def path(self):
        return self.mmsfilename.decode('utf-8')
    @path.setter
    def path(self,value):
        self.__write_item(SBmsMessage.EBmsMsgItem.EBMI_MMS_FILENAME.value, value)
    @property
    def mobiles(self):
        return self._mobile.decode('utf-8')
    @mobiles.setter
    def mobiles(self,value):
        self.__write_item(SBmsMessage.EBmsMsgItem.EBMI_MOBILE.value, value)


class SHisSendFixedData(Structure):
    _fields_=[
        ("msgId",c_int64),
        ("accId", c_int),
        ("prdExId", c_int),
        ("submitPrdExid", c_int),
        ("sendDateTime", c_double),
        ("commitDateTime", c_double),
        ("mobile", c_int64),
        ("matchId", c_int64),
        ("pkTotal", c_ubyte),
        ("pkNum", c_ubyte),
        ("chargeQuantity", c_int),
        ("sendTimes", c_short),
        ("msgType", c_ubyte),
        ("sendState", c_bool),
        ("priority", c_ubyte),
        ("flagBits", c_int64),
        ("rmSndFldRsndTimes", c_ubyte),
        ("rmRepFldRsndTimes", c_ubyte),
        ("dealTimes", c_uint),
        ("timeStamp", c_int64)
    ]

    __OneByte = struct.Struct("<qiiiddqqBBihBBBqBBIq")

    def Value(self):
        print(struct.Struct('q').pack(self.timeStamp))
        test = (self.msgId,
                                     self.accId,
                                     self.prdExId,
                                     self.submitPrdExid,
                                     self.sendDateTime,
                                     self.commitDateTime,
                                     self.mobile,
                                     self.matchId,
                                     self.pkTotal,
                                     self.pkNum,
                                     self.chargeQuantity,
                                     self.sendTimes,
                                     self.msgType,
                                     int(self.sendState),
                                     self.priority,
                                     self.flagBits,
                                     self.rmSndFldRsndTimes,
                                     self.rmRepFldRsndTimes,
                                     self.dealTimes,
                                     self.timeStamp)
        return self.__OneByte.pack(*test)

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self.msgId              =data[0]
        self.accId              =data[1]
        self.prdExId            =data[2]
        self.submitPrdExid      =data[3]
        self.sendDateTime       =data[4]
        self.commitDateTime     =data[5]
        self.mobile             =data[6]
        self.matchId            =data[7]
        self.pkTotal            =data[8]
        self.pkNum              =data[9]
        self.chargeQuantity     =data[10]
        self.sendTimes          =data[11]
        self.msgType            =data[12]
        self.sendState          =data[13]
        self.priority           =data[14]
        self.flagBits           =data[15]
        self.rmSndFldRsndTimes  =data[16]
        self.rmRepFldRsndTimes  =data[17]
        self.dealTimes          =data[18]
        self.timeStamp          =data[19]

    def __len__(self):
        return self.__OneByte.size


class SHisSendData(Structure):
    class ItemIndex(Enum):
        MSGCONTENT_IND  = 0#// 信息内容
        WHLMSG_IND      = 1#// 长短信总内容（信息自动重发用）
        MSG_SIGN        = 2#// 签名
        SPNO_IND        = 3#// 服务商号码
        EXTEND_NUM      = 4#// 扩展号码
        ACCMSGID_IND    = 5# // 客户自定义信息ID
        SENDRESINFO_IND = 6#// 发送结果内容
        TITLE_IND       = 7#// 彩信标题
        ITEM_CNT        = 8#// ItemCnt

    _fields_=[
        ("msgheader",msg_header),
        ("Data",SHisSendFixedData),
        ("node",Node * ItemIndex.ITEM_CNT.value),
    ]

    _message    = None
    _whlMsg     = None
    _sign       = None
    _spno       = None
    _extendNum  = None
    _acc_msgid  = None
    _sendResultInfo = None
    _title      = None
    impl_version = 0x10
    impl_type = EBmsMsgType.MSG_HIS_MT.value[0]
    kMaxMsgSize = 8 * 1024
    kMaxCache = kMaxMsgSize + 256

    def __init__(self):
        self.msgheader._item_count = self.ItemIndex.ITEM_CNT.value
        self.msgheader._offset = len(self.msgheader)+len(self.Data)

    def write_header(self):
        self.msgheader._type = self.impl_type
        self.msgheader._version = self.impl_version
        self.msgheader._length = self.getsize()

    def clear(self):
        self.msgheader._item_total_size = 0
        self.msgheader._length = 0

    def getsize(self):
        return self.msgheader._offset + self.msgheader._item_total_size+self.get_indexes_size()

    def get_indexes_size(self):
        return self.msgheader._item_count*len(self.node[0])


    def Value(self):
        l=0
        for i in range(self.ItemIndex.ITEM_CNT.value):
            l +=self.node[i].m_size
        self.__OneByte = struct.Struct("<%ds" %(l,))
        #定长
        value = self.msgheader.Value()+self.Data.Value()
        #动长node
        for i in range(self.ItemIndex.ITEM_CNT.value):
            value += self.node[i].Value()
        #动长
        value +=self.__OneByte.pack(*(self._message + b'\x00\x00' +
                                      self._whlMsg + b'\x00\x00' +
                                      self._sign + b'\x00\x00' +
                                      self._spno + b'\x00' +
                                      self._extendNum + b'\x00' +
                                      self._acc_msgid + b'\x00' +
                                      self._sendResultInfo + b'\x00' +
                                      self._title + b'\x00\x00',))
        return value

    def fromBytes(self,b):
        b = bytearray(b)
        l1 = len(self.msgheader)
        l2 = len(self.Data)
        l4 = len(self.node[0])
        l5 = self.msgheader._offset+self.ItemIndex.ITEM_CNT.value*l4
        self.msgheader.fromBytes(b[:l1])
        self.Data.fromBytes(b[l1:l1+l2])
        for i in range(self.msgheader._item_count):
            self.node[i].fromBytes(b[l1+l2+i*l4:l1+l2+(i+1)*l4])
        self._message        = bytes(b[l5 + self.node[0].m_offset:l5 + self.node[0].m_offset + self.node[0].m_size])
        self._whlMsg         = bytes(b[l5 + self.node[1].m_offset:l5 + self.node[1].m_offset + self.node[1].m_size])
        self._sign           = bytes(b[l5 + self.node[2].m_offset:l5 + self.node[2].m_offset + self.node[2].m_size])
        self._spno           = bytes(b[l5 + self.node[3].m_offset:l5 + self.node[3].m_offset + self.node[3].m_size])
        self._extendNum      = bytes(b[l5 + self.node[4].m_offset:l5 + self.node[4].m_offset + self.node[4].m_size])
        self._acc_msgid      = bytes(b[l5 + self.node[5].m_offset:l5 + self.node[5].m_offset + self.node[5].m_size])
        self._sendResultInfo = bytes(b[l5 + self.node[6].m_offset:l5 + self.node[6].m_offset + self.node[6].m_size])
        self._title          = bytes(b[l5 + self.node[7].m_offset:l5 + self.node[7].m_offset + self.node[7].m_size])

    def write_getsize(self,index,text):
        if index ==0:
            if isinstance(text,str):
                self._message = text.encode('utf_16_le')#+'\x00\x00'.encode('utf_8')
                #c_char_p.value =
            else:
                raise TypeError(text)
            return len(self._message) + 2
        elif index == 1:
            if isinstance(text,str):
                self._whlMsg = text.encode('utf_16_le')#+'..'.encode('utf_8')
            else:
                raise TypeError(text)
            return len(self._whlMsg) + 2
        elif index == 2:
            if isinstance(text,str):
                self._sign = text.encode('utf_16_le')#+'..'.encode('utf_8')
            else:
                raise TypeError(text)
            return len(self._sign) + 2
        elif index == 3:
            if isinstance(text,str):
                self._spno = bytes(text, encoding='utf-8')
            else:
                raise TypeError(text)
            return len(self._spno) + 1
        elif index == 4:
            if isinstance(text,str):
                self._extendNum = bytes(text, encoding='utf-8')
            else:
                raise TypeError(text)
            return len(self._extendNum) + 1
        elif index == 5:
            if isinstance(text,str):
                self._acc_msgid = bytes(text, encoding='utf-8')
            else:
                raise TypeError(text)
            return len(self._acc_msgid) + 1
        elif index == 6:
            if isinstance(text,str):
                self._sendResultInfo = bytes(text, encoding='utf-8')
            else:
                raise TypeError(text)
            return len(self._sendResultInfo) + 1
        elif index == 7:
            if isinstance(text,str):
                self._title = text.encode('utf_16_le')#+'..'.encode('utf_8')
            else:
                raise TypeError(text)
            return len(self._title) + 2
        else:
            raise ValueError(index)

    def __write_item(self,index,text):
        if index > self.msgheader._item_count:
            return False
        self.node[index].m_offset = self.msgheader._item_total_size
        size = self.write_getsize(index,text)
        self.node[index].m_size = size
        self.msgheader._item_total_size += size

    def write_message(self,text):
        self.__write_item(self.ItemIndex.MSGCONTENT_IND.value,text)
    def write_whlMsg(self,text):
        self.__write_item(self.ItemIndex.WHLMSG_IND.value, text)
    def write_sign(self,text):
        self.__write_item(self.ItemIndex.MSG_SIGN.value, text)
    def write_spno(self,text):
        self.__write_item(self.ItemIndex.SPNO_IND.value, text)
    def write_extnum(self,text):
        self.__write_item(self.ItemIndex.EXTEND_NUM.value, text)
    def write_accmsgid(self,text):
        self.__write_item(self.ItemIndex.ACCMSGID_IND.value, text)
    def write_sendresult(self,text):
        self.__write_item(self.ItemIndex.SENDRESINFO_IND.value, text)
    def write_title(self,text):
        self.__write_item(self.ItemIndex.TITLE_IND.value, text)

    @property
    def message(self):
        return self._message.decode('utf_16_le')
    @property
    def whlMsg(self):
        return self._whlMsg.decode('utf_16_le')
    @property
    def sign(self):
        return self._sign.decode('utf_16_le')
    @property
    def spno(self):
        return self._spno.decode('utf-8')
    @property
    def extnum(self):
        return self._extendNum.decode('utf-8')
    @property
    def accmsgid(self):
        return self._acc_msgid.decode('utf-8')
    @property
    def sendresult(self):
        return self._sendResultInfo.decode('utf-8')
    @property
    def title(self):
        return self._title.decode('utf_16_le')


class SHisRepFixedData(Structure):
    _fields_=[
        ('mobile',c_int64),
        ('matchId', c_int64),
        ('resId', c_int),
        ('reportDateTime', c_double),
        ('reportState', c_bool),
        ('flagBits', c_int64),
        ('retryTimes', c_uint),
        ('timeStamp', c_int64),
    ]

    __OneByte = struct.Struct('<qqidBqIq')

    def Value(self):
        return self.__OneByte.pack(*(
                                    self.mobile,
                                    self.matchId,
                                    self.resId,
                                    self.reportDateTime,
                                    self.reportState,
                                    self.flagBits,
                                    self.retryTimes,
                                    self.timeStamp,
                                    ))

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self.mobile         =data[0]
        self.matchId        =data[1]
        self.resId          =data[2]
        self.reportDateTime =data[3]
        self.reportState    =data[4]
        self.flagBits       =data[5]
        self.retryTimes     =data[6]
        self.timeStamp      =data[7]

    def __len__(self):
        return self.__OneByte.size


class SHisRepData(Structure):
    class ItemIndex(Enum):
        REPINFO = 0
        ITEM_CNT = 1

    _fields_ = [
        ("msgheader",msg_header),
        ("Data",SHisRepFixedData),
        ("node",Node * ItemIndex.ITEM_CNT.value),
    ]
    _repResultInfo =None
    impl_version = 0x0001
    impl_type = EBmsMsgType.MSG_HIS_REP.value[0]
    kMaxMsgSize = 65
    kMaxCache = kMaxMsgSize

    def __init__(self):
        self.msgheader._item_count = self.ItemIndex.ITEM_CNT.value
        self.msgheader._offset = len(self.msgheader) + len(self.Data)

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
                self._repResultInfo = text.encode('utf_8')#+'\x00\x00'.encode('utf_8')
            else:
                raise TypeError(text)
            return len(self._repResultInfo) + 1
        else:
            raise ValueError(index)

    def __write_item(self,index,text):
        if index > self.msgheader._item_count:
            return False
        self.node[index].m_offset = self.msgheader._item_total_size
        size = self.write_getsize(index,text)
        self.node[index].m_size = size
        self.msgheader._item_total_size += size

    def write_repResultInfo(self,text):
        self.__write_item(0,text)

    def Value(self):
        l = 0
        for i in range(self.ItemIndex.ITEM_CNT.value):
            l += self.node[i].m_size
        self.__OneByte = struct.Struct("<%ds" % (l,))
        # 定长
        value = self.msgheader.Value() + self.Data.Value()
        # 动长node
        for i in range(self.ItemIndex.ITEM_CNT.value):
            value += self.node[i].Value()
        # 动长
        value += self.__OneByte.pack(*(self._repResultInfo + b'\x00',))
        return value

    def fromBytes(self,b):
        b = bytearray(b)
        l1 = len(self.msgheader)
        l2 = len(self.Data)
        l4 = len(self.node[0])
        l5 = self.msgheader._offset+self.ItemIndex.ITEM_CNT.value*l4
        self.msgheader.fromBytes(b[:l1])
        self.Data.fromBytes(b[l1:l1+l2])
        for i in range(self.msgheader._item_count):
            self.node[i].fromBytes(b[l1+l2+i*l4:l1+l2+(i+1)*l4])
        self._repResultInfo = bytes(b[l5 + self.node[0].m_offset:l5 + self.node[0].m_offset + self.node[0].m_size])

    @property
    def repResultInfo(self):
        return self._repResultInfo.decode('utf-8')


class SRepNotifyFixedData(Structure):
    _fields_ = [
        ("msgId",c_int64),
        ("accId", c_int),
        ("mobile", c_int64),
        ("sendState", c_bool),
        ("reportState", c_bool),
        ("sendDateTime", c_double),
        ("reportDateTime", c_double),
        ("recvReportDateTime",c_double),
        ("pk_total", c_ubyte),
        ("pk_num", c_ubyte),
        ("flagBits", c_int64),
    ]

    __OneByte = struct.Struct('<qiqBBdddBBq')

    def Value(self):
        data = (
            self.msgId,
            self.accId,
            self.mobile,
            self.sendState,
            self.reportState,
            self.sendDateTime,
            self.reportDateTime,
            self.recvReportDateTime,
            self.pk_total,
            self.pk_num,
            self.flagBits,
        )
        return self.__OneByte.pack(*(
            self.msgId,
            self.accId,
            self.mobile,
            self.sendState,
            self.reportState,
            self.sendDateTime,
            self.reportDateTime,
            self.recvReportDateTime,
            self.pk_total,
            self.pk_num,
            self.flagBits,
        ))

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self.msgId              =data[0]
        self.accId              =data[1]
        self.mobile             =data[2]
        self.sendState          =data[3]
        self.reportState        =data[4]
        self.sendDateTime       =data[5]
        self.reportDateTime     =data[6]
        self.recvReportDateTime =data[7]
        self.pk_total           =data[8]
        self.pk_num             =data[9]
        self.flagBits           =data[10]

    def __len__(self):
        return self.__OneByte.size

class SRepNotifyData(Structure):
    class ItemIndex(Enum):
        SENDRESINFO_IND =0  #//发送结果内容
        REPRESINFO_IND  =1  #//状态报告结果内容
        SPNO_IND        =2  #//服务商号码
        ACCMSGID_IND    =3  #//客户自定义信息ID
        EXTENDNUM_IND   =4  #//扩展号码
        ITEM_CNT        =5  #//Item数量

    _fields_ = [
        ('msgheader',msg_header),
        ('Data',SRepNotifyFixedData),
        ('node',Node * ItemIndex.ITEM_CNT.value),
    ]

    _sendResultInfo  =None
    _repResultInfo   =None
    _spno            =None
    _acc_msgid       =None
    _extnumber       =None

    impl_version = 0x0001
    impl_type = EBmsMsgType.MSG_REP_NTF.value[0]
    kMaxMsgSize = 200
    kMaxCache = kMaxMsgSize

    def __init__(self):
        self.msgheader._item_count = self.ItemIndex.ITEM_CNT.value
        self.msgheader._offset = len(self.msgheader) + len(self.Data)

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
                self._sendResultInfo = text.encode('utf_8')#+'\x00\x00'.encode('utf_8')
            else:
                raise TypeError(text)
            return len(self._sendResultInfo) + 1
        elif index ==1:
            if isinstance(text,str):
                self._repResultInfo = text.encode('utf_8')#+'\x00\x00'.encode('utf_8')
            else:
                raise TypeError(text)
            return len(self._repResultInfo) + 1
        elif index == 2:
            if isinstance(text,str):
                self._spno = text.encode('utf_8')#+'\x00\x00'.encode('utf_8')
            else:
                raise TypeError(text)
            return len(self._spno) + 1
        elif index == 3:
            if isinstance(text,str):
                self._acc_msgid = text.encode('utf_8')#+'\x00\x00'.encode('utf_8')
            else:
                raise TypeError(text)
            return len(self._acc_msgid) + 1
        elif index == 4:
            if isinstance(text,str):
                self._extnumber = text.encode('utf_8')#+'\x00\x00'.encode('utf_8')
            else:
                raise TypeError(text)
            return len(self._extnumber) + 1
        else:
            raise ValueError(index)

    def __write_item(self,index,text):
        if index > self.msgheader._item_count:
            return False
        self.node[index].m_offset = self.msgheader._item_total_size
        size = self.write_getsize(index,text)
        self.node[index].m_size = size
        self.msgheader._item_total_size += size

    def write_sendResultInfo(self,text):
        self.__write_item(self.ItemIndex.SENDRESINFO_IND.value,text)
    def write_repResultInfo(self,text):
        self.__write_item(self.ItemIndex.REPRESINFO_IND.value,text)
    def write_spno(self,text):
        self.__write_item(self.ItemIndex.SPNO_IND.value,text)
    def write_acc_msgid(self,text):
        self.__write_item(self.ItemIndex.ACCMSGID_IND.value,text)
    def write_extnumber(self,text):
        self.__write_item(self.ItemIndex.EXTENDNUM_IND.value,text)

    def Value(self):
        l=0
        for i in range(self.ItemIndex.ITEM_CNT.value):
            l+=self.node[i].m_size

        self.__OneByte = struct.Struct("<%ds" % (l,))
        # 定长
        value = self.msgheader.Value() + self.Data.Value()
        # 动长node
        for i in range(self.ItemIndex.ITEM_CNT.value):
            value += self.node[i].Value()
        # 动长
        value += self.__OneByte.pack(*(self._sendResultInfo + b'\x00' +
                                       self._repResultInfo + b'\x00' +
                                       self._spno + b'\x00' +
                                       self._acc_msgid + b'\x00' +
                                       self._extnumber + b'\x00'
                                       ,))
        return value

    def fromBytes(self,b):
        b = bytearray(b)
        l1 = len(self.msgheader)
        l2 = len(self.Data)
        l4 = len(self.node[0])
        l5 = self.msgheader._offset+self.ItemIndex.ITEM_CNT.value*l4
        self.msgheader.fromBytes(b[:l1])
        self.Data.fromBytes(b[l1:l1+l2])
        for i in range(self.msgheader._item_count):
            self.node[i].fromBytes(b[l1+l2+i*l4:l1+l2+(i+1)*l4])
        self._sendResultInfo = bytes(b[l5 + self.node[0].m_offset:l5 + self.node[0].m_offset + self.node[0].m_size])
        self._repResultInfo  = bytes(b[l5 + self.node[1].m_offset:l5 + self.node[1].m_offset + self.node[1].m_size])
        self._spno           = bytes(b[l5 + self.node[2].m_offset:l5 + self.node[2].m_offset + self.node[2].m_size])
        self._acc_msgid      = bytes(b[l5 + self.node[3].m_offset:l5 + self.node[3].m_offset + self.node[3].m_size])
        self._extnumber      = bytes(b[l5 + self.node[4].m_offset:l5 + self.node[4].m_offset + self.node[4].m_size])

    @property
    def sendResultInfo(self):
        return self._sendResultInfo.decode('utf-8')
    @property
    def repResultInfo(self):
        return self._repResultInfo.decode('utf-8')
    @property
    def spno(self):
        return self._spno.decode('utf-8')
    @property
    def acc_msgid(self):
        return self._acc_msgid.decode('utf-8')
    @property
    def extnumber(self):
        return self._extnumber.decode('utf-8')


class SHisMOFixedData(Structure):
    _fields_ = [
        ('msgId',c_int64),
        ('msgType', c_ubyte),
        ('accId', c_int),
        ('mobile', c_int64),
        ('moTime', c_double),
        ('resId', c_int),
        ('timeStamp', c_int64),
        ('dealTimes', c_uint),
    ]

    __OneByte = struct.Struct("<qBiqdiqI")

    def Value(self):
        return self.__OneByte.pack(*(
                                    self.msgId,
                                    self.msgType,
                                    self.accId,
                                    self.mobile,
                                    self.moTime,
                                    self.resId,
                                    self.timeStamp,
                                    self.dealTimes
                                    ))

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self.msgId      = data[0]
        self.msgType    = data[1]
        self.accId      = data[2]
        self.mobile     = data[3]
        self.moTime     = data[4]
        self.resId      = data[5]
        self.timeStamp  = data[6]
        self.dealTimes  = data[7]

    def __len__(self):
        return self.__OneByte.size

class SHisMOData(Structure):
    class ItemIndex(Enum):
        MOCONTENT_IND   =0  #//上行信息内容
        SPNO_IND        =1  #//服务商号码
        ITEM_CNT        =2  #//数量


    _fields_ = [
        ('msgheader',msg_header),
        ('Data',SHisMOFixedData),
        ('node',Node * ItemIndex.ITEM_CNT.value),
    ]

    _MoContent   =None
    _SpNum       =None

    impl_version = 0x0001
    impl_type = EBmsMsgType.MSG_HIS_MO.value[0]
    kMaxMsgSize = 200
    kMaxCache = kMaxMsgSize

    def __init__(self):
        self.msgheader._item_count = self.ItemIndex.ITEM_CNT.value
        self.msgheader._offset = len(self.msgheader) + len(self.Data)

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
                self._MoContent = text.encode('utf_16_le')#+'\x00\x00'.encode('utf_8')
            else:
                raise TypeError(text)
            return len(self._MoContent) + 2
        elif index ==1:
            if isinstance(text,str):
                self._SpNum = text.encode('utf_8')#+'\x00\x00'.encode('utf_8')
            else:
                raise TypeError(text)
            return len(self._SpNum) + 1
        else:
            raise ValueError(index)

    def __write_item(self,index,text):
        if index > self.msgheader._item_count:
            return False
        self.node[index].m_offset = self.msgheader._item_total_size
        size = self.write_getsize(index,text)
        self.node[index].m_size = size
        self.msgheader._item_total_size += size

    def write_MoContent(self,text):
        self.__write_item(self.ItemIndex.MOCONTENT_IND.value,text)
    def write_SpNum(self,text):
        self.__write_item(self.ItemIndex.SPNO_IND.value,text)

    def Value(self):
        l=0
        for i in range(self.ItemIndex.ITEM_CNT.value):
            l+=self.node[i].m_size

        self.__OneByte = struct.Struct("<%ds" % (l,))
        # 定长
        value = self.msgheader.Value() + self.Data.Value()
        # 动长node
        for i in range(self.ItemIndex.ITEM_CNT.value):
            value += self.node[i].Value()
        # 动长
        value += self.__OneByte.pack(*(self._MoContent + b'\x00\x00' +
                                       self._SpNum + b'\x00'
                                       ,))
        return value

    def fromBytes(self,b):
        b = bytearray(b)
        l1 = len(self.msgheader)
        l2 = len(self.Data)
        l4 = len(self.node[0])
        l5 = self.msgheader._offset+self.ItemIndex.ITEM_CNT.value*l4
        self.msgheader.fromBytes(b[:l1])
        self.Data.fromBytes(b[l1:l1+l2])
        for i in range(self.msgheader._item_count):
            self.node[i].fromBytes(b[l1+l2+i*l4:l1+l2+(i+1)*l4])
        self._MoContent = bytes(b[l5 + self.node[0].m_offset:l5 + self.node[0].m_offset + self.node[0].m_size])
        self._SpNum  = bytes(b[l5 + self.node[1].m_offset:l5 + self.node[1].m_offset + self.node[1].m_size])

    @property
    def MoContent(self):
        return self._MoContent.decode('utf_16_le')
    @property
    def SpNum(self):
        return self._SpNum.decode('utf-8')

class SMoAccBlist(Structure):
    _fields_ = [
        ('mobile',c_int64),
        ('accid', c_int),
        ('level', c_int),
        ('flag', c_int64),
    ]

    __OneByte = struct.Struct('<qiiq')

    def Value(self):
        return self.__OneByte.pack(*(
                                self.mobile,
                                self.accid,
                                self.level,
                                self.flag,
                                ))

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self.mobile = data[0]
        self.accid  = data[1]
        self.level  = data[2]
        self.flag   = data[3]

    def __len__(self):
        return self.__OneByte.size

class MoAccBlist(Structure):
    class ItemIndex(Enum):
        OPERATOR_CNT = 0
        REMARK_CNT   = 1
        ITEM_CNT     = 2

    _fields_ = [
        ('msgheader', msg_header),
        ('Data', SMoAccBlist),
        ('node', Node * ItemIndex.ITEM_CNT.value),

    ]

    _operator = None
    _remark   = None

    impl_version = 0x0001
    impl_type = EBmsMsgType.MSG_NEED_ACCBLIST.value[0]
    kMaxMsgSize = 200
    kMaxCache = kMaxMsgSize

    def __init__(self):
        self.msgheader._item_count = self.ItemIndex.ITEM_CNT.value
        self.msgheader._offset = len(self.msgheader) + len(self.Data)

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
                self._operator = text.encode('utf_8')#+'\x00\x00'.encode('utf_8')
            else:
                raise TypeError(text)
            return len(self._operator) + 1
        elif index ==1:
            if isinstance(text,str):
                self._remark = text.encode('utf_8')#+'\x00\x00'.encode('utf_8')
            else:
                raise TypeError(text)
            return len(self._remark) + 1
        else:
            raise ValueError(index)

    def __write_item(self,index,text):
        if index > self.msgheader._item_count:
            return False
        self.node[index].m_offset = self.msgheader._item_total_size
        size = self.write_getsize(index,text)
        self.node[index].m_size = size
        self.msgheader._item_total_size += size

    def write_operator(self,text):
        self.__write_item(self.ItemIndex.OPERATOR_CNT.value,text)
    def write_remark(self,text):
        self.__write_item(self.ItemIndex.REMARK_CNT.value,text)

    def Value(self):
        l=0
        for i in range(self.ItemIndex.ITEM_CNT.value):
            l+=self.node[i].m_size

        self.__OneByte = struct.Struct("<%ds" % (l,))
        # 定长
        value = self.msgheader.Value() + self.Data.Value()
        # 动长node
        for i in range(self.ItemIndex.ITEM_CNT.value):
            value += self.node[i].Value()
        # 动长
        value += self.__OneByte.pack(*(self._operator + b'\x00' +
                                       self._remark + b'\x00'
                                       ,))
        return value

    def fromBytes(self,b):
        b = bytearray(b)
        l1 = len(self.msgheader)
        l2 = len(self.Data)
        l4 = len(self.node[0])
        l5 = self.msgheader._offset+self.ItemIndex.ITEM_CNT.value*l4
        self.msgheader.fromBytes(b[:l1])
        self.Data.fromBytes(b[l1:l1+l2])
        for i in range(self.msgheader._item_count):
            self.node[i].fromBytes(b[l1+l2+i*l4:l1+l2+(i+1)*l4])
        self._operator = bytes(b[l5 + self.node[0].m_offset:l5 + self.node[0].m_offset + self.node[0].m_size])
        self._remark  = bytes(b[l5 + self.node[1].m_offset:l5 + self.node[1].m_offset + self.node[1].m_size])

    @property
    def operator(self):
        return self._operator.decode('utf-8')
    @property
    def remark(self):
        return self._remark.decode('utf-8')