import struct
from enum import Enum
from PyQt5 import QtCore
from BMSMessage import Datetime_dt,dt_Datetime
import sys
from ctypes import *


def Pack(ctype_instance):
    return string_at(addressof(ctype_instance),sizeof(ctype_instance))

def UnPack(ctype,buf):
    cstring = create_string_buffer(buf)
    return cast(pointer(cstring),POINTER(ctype)).contents

class msg_header(object):
    __OneByte = struct.Struct('<6I')
    def __init__(self):
        self._length         = 0
        self._type           = 0
        self._version        = 0
        self._offset         = 0
        self._item_count     = 0
        self._item_total_size= 0

    def Value(self):
        try:
            return self.__OneByte.pack(*(self._length,self._type,self._version,
                                     self._offset,self._item_count,self._item_total_size))
        except Exception as e:
            print(e)

    def fromBytes(self,b):
        try:
            data = self.__OneByte.unpack(b)
            self._length = data[0]
            self._type = data[1]
            self._version = data[2]
            self._offset = data[3]
            self._item_count = data[4]
            self._item_total_size = data[5]
        except Exception as e:
            print(e)

    def __len__(self):
        return self.__OneByte.size


class DispatchFixedHead(object):
    __OneByte = struct.Struct("<BQIIddddiBBdHIIIIbbhbBBBII")
    def __init__(self):
        self.Priority               =0
        self.MsgId                  =0
        self.ProductExtendId        =0
        self.RealProductExtendId    =0
        self.StartSendDateTime      =0
        self.EndSendDateTime        =0
        self.StartSendTime          =0
        self.EndSendTime            =0
        self.ChargeQuantity         =0
        self.MsgState               =0
        self.MsgType                =0
        self.CommitTime             =0
        self.Package                =0
        self.MobilesContentLen      =0
        self.MsgContentLen          =0
        self.MobilesCount           =0
        self.DispatchTimes          =0
        self.Telcom                 =0
        self.ProvinceId             =0
        self.CityId                 =0
        self.TPCBChecked            =0
        self.SendedTimes            =0
        self.DispatchFailedState    =0
        self.SubmitType             =0
        self.CloudMsgTemplateID     =0
        self.CommitIp               =0


    def Value(self):
        try:
            return self.__OneByte.pack(*(
                self.Priority,
                self.MsgId,
                self.ProductExtendId,
                self.RealProductExtendId,
                self.StartSendDateTime,
                self.EndSendDateTime,
                self.StartSendTime,
                self.EndSendTime,
                self.ChargeQuantity,
                self.MsgState,
                self.MsgType,
                self.CommitTime,
                self.Package,
                self.MobilesContentLen,
                self.MsgContentLen,
                self.MobilesCount,
                self.DispatchTimes,
                self.Telcom,
                self.ProvinceId,
                self.CityId,
                self.TPCBChecked,
                self.SendedTimes,
                self.DispatchFailedState,
                self.SubmitType,
                self.CloudMsgTemplateID,
                self.CommitIp,
            ))
        except Exception as e:
            print(e)

    def fromBytes(self,b):
        try:
            data = self.__OneByte.unpack(b)
            self.Priority               = data[0]
            self.MsgId                  = data[1]
            self.ProductExtendId        = data[2]
            self.RealProductExtendId    = data[3]
            self.StartSendDateTime      = data[4]
            self.EndSendDateTime        = data[5]
            self.StartSendTime          = data[6]
            self.EndSendTime            = data[7]
            self.ChargeQuantity         = data[8]
            self.MsgState               = data[9]
            self.MsgType                = data[10]
            self.CommitTime             = data[11]
            self.Package                = data[12]
            self.MobilesContentLen      = data[13]
            self.MsgContentLen          = data[14]
            self.MobilesCount           = data[15]
            self.DispatchTimes          = data[16]
            self.Telcom                 = data[17]
            self.ProvinceId             = data[18]
            self.CityId                 = data[19]
            self.TPCBChecked            = data[20]
            self.SendedTimes            = data[21]
            self.DispatchFailedState    = data[22]
            self.SubmitType             = data[23]
            self.CloudMsgTemplateID     = data[24]
            self.CommitIp               = data[25]
        except Exception as e:
            print(e)
            Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))


    def __len__(self):
        return self.__OneByte.size


class DispatchFixedTail(object):
    __OneByte = struct.Struct('<BHiiBdHiBiiib')
    def __init__(self):
        self.pagetotal          =0
        self.packagetotal           =0
        self.typeComponentParam     =0
        self.lastFailResourceId     =0
        self.failedType             =0
        self.lastDiapatchTime       =0
        self.resourceSendTimes      =0
        self.auditorId              =0
        self.totalSendTimes         =0
        self.repResendTimeOut       =0
        self.innerDispatchTimes     =0
        self.extComponentParam      =0
        self.m_old_struct           = 0

    def Value(self):
        try:
            return self.__OneByte.pack(*(
                self.pagetotal,
                self.packagetotal,
                self.typeComponentParam,
                self.lastFailResourceId,
                self.failedType,
                self.lastDiapatchTime,
                self.resourceSendTimes,
                self.auditorId,
                self.totalSendTimes,
                self.repResendTimeOut,
                self.innerDispatchTimes,
                self.extComponentParam,
                self.m_old_struct
            ))
        except Exception as e:
            print(e)

    def fromBytes(self,b):
        try:
            data = self.__OneByte.unpack(b)
            self.pagetotal          = data[0]
            self.packagetotal           = data[1]
            self.typeComponentParam     = data[2]
            self.lastFailResourceId     = data[3]
            self.failedType             = data[4]
            self.lastDiapatchTime       = data[5]
            self.resourceSendTimes      = data[6]
            self.auditorId              = data[7]
            self.totalSendTimes         = data[8]
            self.repResendTimeOut       = data[9]
            self.innerDispatchTimes     = data[10]
            self.extComponentParam      = data[11]
            self.m_old_struct           = data[12]
        except Exception as e:
            print(e)

    def __len__(self):
        return self.__OneByte.size

class Node(object):
    __OneByte = struct.Struct("<II")
    def __init__(self):
        self.m_offset = 0
        self.m_size = 0
    def Value(self):
        try:
            return self.__OneByte.pack(*(self.m_offset,self.m_size))
        except Exception as e:
            print(e)

    def fromBytes(self,b):
        try:
            data = self.__OneByte.unpack(b)
            self.m_offset = data[0]
            self.m_size = data[1]
        except Exception as e:
            print(e)

    def __len__(self):
        return self.__OneByte.size


class SCloudMessage(object):
    impl_type = 0x55555555
    impl_version = 0xAAAAAAAA
    class ECloudMsgItem(Enum):
        ECMI_MOBILE         =0,
        ECMI_ACC_NAME       =1,
        ECMI_CONTENT        =2,
        ECMI_TEMPLATE_ID    =3,
        ECMI_MSG_TEMPLATE   =4,
        ECMI_PARAM_TEMPLATE =5,
        ECMI_EXT_NUMBER     =6,
        ECMI_SIGN           =7,
        ECMI_ACC_MSGID      =8,
        ECMI_MMS_TITLE      =9,
        ECMI_MMS_FILENAME   =10,
        ECMI_USER_DEF_ID    =11,
        ECMI_ITEM_COUNT     =12


    def __init__(self):
        self.msgheader = msg_header()
        self.FixHead = DispatchFixedHead()
        self.FixTail = DispatchFixedTail()
        self.node = []
        for i in range(self.ECloudMsgItem.ECMI_ITEM_COUNT.value):
            self.node.append(Node())

        self._mobiles = None
        self._acc_name =None
        self._message = None
        self._templateID = None
        self._msgtemplate = None
        self._paramtemplate = None
        self._extnumer = None
        self._sign = None
        self._acc_msgid =None
        self._mms_title = None
        self._mms_filename = None
        self._usr_def_id = None

        self.msgheader._item_count = self.ECloudMsgItem.ECMI_ITEM_COUNT.value
        self.msgheader._offset = len(self.msgheader)+len(self.FixHead)+len(self.FixTail)

    def Value(self):
        try:
            l = 0
            for i in range(self.ECloudMsgItem.ECMI_ITEM_COUNT.value):
                l+=self.node[i].m_size
            self.__OneByte = struct.Struct("<%ds" %(l,))
            #定长
            value = self.msgheader.Value()+self.FixHead.Value()+self.FixTail.Value()
            #动长node
            for i in range(self.ECloudMsgItem.ECMI_ITEM_COUNT.value):
                value += self.node[i].Value()
            #动长
            value +=self.__OneByte.pack(*(
                                self._mobiles+
                                self._acc_name+
                                self._message+
                                self._templateID+
                                self._msgtemplate+
                                self._paramtemplate+
                                self._extnumer+
                                self._sign+
                                self._acc_msgid+
                                self._mms_title+
                                self._mms_filename+
                                self._usr_def_id,))
            return value
        except Exception as e:
            print(e)

    def fromBytes(self,b):
        try:
            b = bytearray(b)
            l1 = len(self.msgheader)
            l2 = len(self.FixHead)
            l3 = len(self.FixTail)
            l4 = len(self.node[0])
            self.msgheader.fromBytes(b[:l1])
            l5 = self.msgheader._offset+12*l4
            self.FixHead.fromBytes(b[l1:l1+l2])
            self.FixTail.fromBytes(b[l1+l2:l1+l2+l3])
            for i in range(self.msgheader._item_count):
                self.node[i].fromBytes(b[l1+l2+l3+i*l4:l1+l2+l3+(i+1)*l4])
            self._mobiles           = bytes(b[l5 + self.node[0].m_offset:l5 + self.node[0].m_offset + self.node[0].m_size])
            self._acc_name          = bytes(b[l5+self.node[1].m_offset:l5+self.node[1].m_offset+self.node[1].m_size])
            self._message           = bytes(b[l5+self.node[2].m_offset:l5+self.node[2].m_offset+self.node[2].m_size])
            self._templateID        = bytes(b[l5+self.node[3].m_offset:l5+self.node[3].m_offset+self.node[3].m_size])
            self._msgtemplate       = bytes(b[l5+self.node[4].m_offset:l5+self.node[4].m_offset+self.node[4].m_size][8:])
            self._paramtemplate     = bytes(b[l5+self.node[5].m_offset:l5+self.node[5].m_offset+self.node[5].m_size][8:])
            self._extnumer          = bytes(b[l5+self.node[6].m_offset:l5+self.node[6].m_offset+self.node[6].m_size])
            self._sign              = bytes(b[l5+self.node[7].m_offset:l5+self.node[7].m_offset+self.node[7].m_size])
            self._acc_msgid         = bytes(b[l5+self.node[8].m_offset:l5+self.node[8].m_offset+self.node[8].m_size])
            self._mms_title         = bytes(b[l5+self.node[9].m_offset:l5+self.node[9].m_offset+self.node[9].m_size])
            self._mms_filename      = bytes(b[l5+self.node[10].m_offset:l5+self.node[10].m_offset+self.node[10].m_size])
            self._usr_def_id        = bytes(b[l5+self.node[11].m_offset:l5+self.node[11].m_offset+self.node[11].m_size])
        except Exception as e:
            print(e)

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

    def write_getsize(self,index:int,text):
        if index ==0:
            if isinstance(text,str):
                self._mobiles = text.encode('utf-8')+b'\x00'
            else:
                raise TypeError(text)
            return len(self._mobiles)
        elif index == 1:
            if isinstance(text,str):
                self._acc_name = text.encode('utf-8')+b'\x00'
            else:
                raise TypeError(text)
            return len(self._acc_name)
        elif index == 2:
            if isinstance(text,str):
                self._message = text.encode('utf_16_le')+b'\x00\x00'
            elif isinstance(text,bytes):
                self._message = text
            else:
                raise TypeError(text)
            return len(self._message)
        elif index == 3:
            if isinstance(text,str):
                self._templateID = bytes(text,encoding='utf-8')+b'\x00'
            else:
                raise TypeError(text)
            return len(self._templateID)
        elif index == 4:
            if isinstance(text,str):
                self._msgtemplate = bytes(text,encoding='utf_16_le')+b'\x00\x00'
            else:
                raise TypeError(text)
            return len(self._msgtemplate)
        elif index == 5:
            if isinstance(text,str):
                self._paramtemplate = bytes(text,encoding='utf-8')+b'\x00'
            else:
                raise TypeError(text)
            return len(self._paramtemplate)
        elif index == 6:
            if isinstance(text,str):
                self._extnumer = text.encode('utf-8')+b'\x00'
            else:
                raise TypeError(text)
            return len(self._extnumer)
        elif index == 7:
            if isinstance(text,str):
                self._sign = bytes(text,encoding='utf_16_le')+b'\x00\x00'
            else:
                raise TypeError(text)
            return len(self._sign)
        elif index == 8:
            if isinstance(text,str):
                self._acc_msgid = bytes(text,encoding='utf-8')+b'\x00'
            else:
                raise TypeError(text)
            return len(self._acc_msgid)
        elif index == 9:
            if isinstance(text,str):
                self._mms_title = bytes(text,encoding='utf_16_le')+b'\x00\x00'
            else:
                raise TypeError(text)
            return len(self._mms_title)
        elif index == 10:
            if isinstance(text,str):
                self._mms_filename = bytes(text,encoding='utf-8')+b'\x00'
            else:
                raise TypeError(text)
            return len(self._mms_filename)
        elif index == 11:
            if isinstance(text,str):
                self._usr_def_id = bytes(text,encoding='utf-8')+b'\x00'
            else:
                raise TypeError(text)
            return len(self._usr_def_id)
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

    @property
    def mobiles(self):
        return self._mobiles.decode('utf-8').replace('\x00','')
    @mobiles.setter
    def mobiles(self,value):
        self.__write_item(SCloudMessage.ECloudMsgItem.ECMI_MOBILE.value[0],value)

    @property
    def acc_name(self):
        return self._acc_name.decode('utf-8').replace('\x00','')
    @acc_name.setter
    def acc_name(self,value):
        self.__write_item(SCloudMessage.ECloudMsgItem.ECMI_ACC_NAME.value[0],value)

    @property
    def message(self):
        return self._message.decode('utf_16_le').replace('\x00','')
    @message.setter
    def message(self,value):
        self.__write_item(SCloudMessage.ECloudMsgItem.ECMI_CONTENT.value[0],value)

    @property
    def templateID(self):
        return self._templateID.decode('utf-8').replace('\x00','')
    @templateID.setter
    def templateID(self,value):
        self.__write_item(SCloudMessage.ECloudMsgItem.ECMI_TEMPLATE_ID.value[0],value)

    @property
    def msgtemplate(self):
        return self._msgtemplate.decode('utf_16_le').replace('\x00','')
    @msgtemplate.setter
    def msgtemplate(self,value):
        self.__write_item(SCloudMessage.ECloudMsgItem.ECMI_MSG_TEMPLATE.value[0],value)

    @property
    def paramtemplate(self):
        return self._paramtemplate.decode('utf_16_le').replace('\x00','')
    @paramtemplate.setter
    def paramtemplate(self,value):
        self.__write_item(SCloudMessage.ECloudMsgItem.ECMI_PARAM_TEMPLATE.value[0],value)

    @property
    def extnumer(self):
        return self._extnumer.decode('utf-8').replace('\x00','')
    @extnumer.setter
    def extnumer(self,value):
        self.__write_item(SCloudMessage.ECloudMsgItem.ECMI_EXT_NUMBER.value[0],value)

    @property
    def sign(self):
        return self._sign.decode('utf_16_le').replace('\x00','')
    @sign.setter
    def sign(self,value):
        self.__write_item(SCloudMessage.ECloudMsgItem.ECMI_SIGN.value[0],value)

    @property
    def acc_msgid(self):
        return self._acc_msgid.decode('utf-8').replace('\x00','')
    @acc_msgid.setter
    def acc_msgid(self,value):
        self.__write_item(SCloudMessage.ECloudMsgItem.ECMI_ACC_MSGID.value[0],value)

    @property
    def mms_title(self):
        return self._mms_title.decode('utf_16_le').replace('\x00','')
    @mms_title.setter
    def mms_title(self,value):
        self.__write_item(SCloudMessage.ECloudMsgItem.ECMI_MMS_TITLE.value[0],value)

    @property
    def mms_filename(self):
        return self._mms_filename.decode('utf-8').replace('\x00','')
    @mms_filename.setter
    def mms_filename(self,value):
        self.__write_item(SCloudMessage.ECloudMsgItem.ECMI_MMS_FILENAME.value[0],value)

    @property
    def usr_def_id(self):
        return self._usr_def_id.decode('utf-8').replace('\x00','')
    @usr_def_id.setter
    def usr_def_id(self,value):
        self.__write_item(SCloudMessage.ECloudMsgItem.ECMI_USER_DEF_ID.value[0],value)


# SMsgSendData                                                  --- HistoryQueue
# SMsgHisRepData                                                --- HistoryQueue
# SMOData                                                       --- HistoryQueue
# SRepNotifyData                                                --- HistoryCenter
# SMsgMTRepData                                                 --- HistoryCenter
# ResourceStateNotify                                           --- MMSPortSend,SMSPortSend
# SDispatchStatistics                                           --- MsgDispatchCenter
# SResComStatistics                                             --- MsgDispatchCenter

MSG_DSP_STC=0x01
MSG_RES_RCV=0x02
MSG_RES_SND=0x03
MSG_HIS_MT=0x81
MSG_HIS_REP=0x82
MSG_HIS_MO=0x83
MSG_HIS_REMT=0x84
MSG_HIS_MTREP = 0x85

class MsgHeader(object):
    __OneByte = struct.Struct("<III")
    def __init__(self):
        self.MessageType = 0
        self.Version     = 0
        self.Length      = 0

    def Value(self):
        try:
            return self.__OneByte.pack(*(
                self.MessageType,
                self.Version,
                self.Length
            ))
        except:
            Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))

    def fromBytes(self,b):
        try:
            data = self.__OneByte.unpack(b)
            self.MessageType = data[0]
            self.Version     = data[1]
            self.Length      = data[2]
        except:
            Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))

    def __len__(self):
        return self.__OneByte.size

class TSMsgSendData(object):
    __OneByte = struct.Struct("<iqddqqiiiihB30s24s16sBiBBiBibi")
    def __init__(self):
        self.productExtendId        =0#// 扩展产品编号
        self.msgId                  =0#// 信息编号
        self.sendedTime             =0#// 发送时间
        self.submitTime             =0#// 提交时间
        self.mobilePhone            =0#// 手机号码
        self.matchId                =0#// 匹配编号
        self.realProductExtendId    =0#// 真实扩展产品编号
        self.resourceId             =0#// 资源编号
        self.chargeQuantity         =0
        self.propertyComponent      =0
        self.sendTimes              =0#// 发送次数
        self.msgType                =0#// 消息类型
        self._accountId              =bytes(30)#// 账号编号
        self._SPNo                   =bytes(24)
        self._clientMsgId            =bytes(16)
        self.sendState              =0#// 发送状态
        self.msgLen                 =0#// 消息的真实长度，含结束\0
        self.SendResultLen          =0#// 含结束\0
        self.TitleLen               =0#// 含结束\0
        self.cycletimes             =0#// 循环次数
        self.Priority               =0#// 消息级别
        self.typeComponentParam     =0#// 综合状态
        self.rmReSendTimes          =0#// 剩余重发次数
        self.repResendTimeOut       =0#// 回执超时时长
        # self.msgContent             = bytes(0)
        # self.sendResultInfo         =bytes(0)
        # self.title                  = bytes(0)
        # self.userDefineId           = bytes(0)
        # self.totalMsgLen            = 0
        # self.totalMsg               = bytes(0)
        # self.sign                   = bytes(0)
    @property
    def accountId(self):
        return self._accountId.decode('utf-8')
    @accountId.setter
    def accountId(self,value:str):
        t = value.encode('utf-8')
        self._accountId = t+bytes(30-len(t))

    @property
    def SPNo(self):
        return self._SPNo.decode('utf-8')
    @SPNo.setter
    def SPNo(self,value:str):
        t = value.encode('utf-8')
        self._SPNo = t+bytes(24-len(t))

    @property
    def clientMsgId(self):
        return self._clientMsgId.decode('utf-8')
    @clientMsgId.setter
    def clientMsgId(self,value:str):
        t = value.encode('utf-8')
        self._clientMsgId = t + bytes(16-len(t))


    def Value(self):
        try:
            return self.__OneByte.pack(*(
                self.productExtendId,
                self.msgId,
                self.sendedTime,
                self.submitTime,
                self.mobilePhone,
                self.matchId,
                self.realProductExtendId,
                self.resourceId,
                self.chargeQuantity,
                self.propertyComponent,
                self.sendTimes,
                self.msgType,
                self._accountId,
                self._SPNo,
                self._clientMsgId,
                self.sendState,
                self.msgLen,
                self.SendResultLen,
                self.TitleLen,
                self.cycletimes,
                self.Priority,
                self.typeComponentParam,
                self.rmReSendTimes,
                self.repResendTimeOut,
            ))
        except:
            Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name,sys._getframe().f_lineno))

    def fromBytes(self,b):
        try:
            data = self.__OneByte.unpack(b)
            self.productExtendId        = data[0]
            self.msgId                  = data[1]
            self.sendedTime             = data[2]
            self.submitTime             = data[3]
            self.mobilePhone            = data[4]
            self.matchId                = data[5]
            self.realProductExtendId    = data[6]
            self.resourceId             = data[7]
            self.chargeQuantity         = data[8]
            self.propertyComponent      = data[9]
            self.sendTimes              = data[10]
            self.msgType                = data[11]
            self._accountId              = data[12]
            self._SPNo                   = data[13]
            self._clientMsgId            = data[14]
            self.sendState              = data[15]
            self.msgLen                 = data[16]
            self.SendResultLen          = data[17]
            self.TitleLen               = data[18]
            self.cycletimes             = data[19]
            self.Priority               = data[20]
            self.typeComponentParam     = data[21]
            self.rmReSendTimes          = data[22]
            self.repResendTimeOut       = data[23]
        except:
            raise Exception("module:{} func:{} line:{} error".format(
                __file__,sys._getframe().f_code.co_name,sys._getframe().f_lineno))

    def __len__(self):
        return self.__OneByte.size

class SMsgSendData(object):
    CType = MSG_HIS_MT
    CVersion = 0x12

    def __init__(self):
        self._head = MsgHeader()
        self._body = TSMsgSendData()
        self._msgContent = bytes(0)
        self._sendResultInfo = bytes(0)
        self._title = bytes(0)
        self._userDefineId = bytes(0)
        self._totalMsgLen = 0
        self._totalMsg = bytes(0)
        self._sign = bytes(0)

    def Value(self):
        values = self._head.Value()+self._body.Value()
        self.__OneByte = struct.Struct("<%ds%ds%ds33si%ds100s" %  (len(self._msgContent),
                                                                  len(self._sendResultInfo),
                                                                  len(self._title),
                                                                  len(self._totalMsg),
                                                                   ))

        values += self.__OneByte.pack(*(self._msgContent,
                                        self._sendResultInfo,
                                        self._title,
                                        self._userDefineId,
                                        self._totalMsgLen,
                                        self._totalMsg,
                                        self._sign))
        return values

    def fromBytes(self,b):
        try:
            b = bytearray(b)
            l1 = len(self._head)
            l2 = len(self._body)
            self._head.fromBytes(b[:l1])
            if self._head.MessageType != self.CType:
                raise Exception("unknown data type:",self._head.MessageType)

            self._body.fromBytes(b[l1:l1+l2])
            l3 = l1 + l2 + self._body.msgLen + self._body.SendResultLen + self._body.TitleLen + 33#totalmsg长度
            totalMsgLen = struct.Struct("i").unpack(b[l3:l3 + 4])[0]
            self.__OneByte = struct.Struct("<%ds%ds%ds33si%ds100s" %(self._body.msgLen,
                                                                     self._body.SendResultLen,
                                                                     self._body.TitleLen,
                                                                     totalMsgLen,))
            data = self.__OneByte.unpack(b[l1+l2:])
            self._msgContent            = data[0]
            self._sendResultInfo        = data[1]
            self._title                 = data[2]
            self._userDefineId          = data[3]
            self._totalMsgLen           = data[4]
            self._totalMsg              = data[5]
            self._sign                  = data[6]
            pass
        except Exception as e:
            print(e)
            raise Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))

    def write_header(self):
        self._head.MessageType = self.CType
        self._head.Version = self.CVersion
        self._head.Length = len(self._head)+len(self._body)+len(self._msgContent)+\
            len(self._sendResultInfo)+len(self._title)+len(self._userDefineId)+4+\
                            len(self._totalMsg)+len(self._sign)

    def clear(self):
        self._msgContent = bytes(0)
        self._sendResultInfo = bytes(0)
        self._title = bytes(0)
        self._userDefineId = bytes(0)
        self._totalMsgLen = 0
        self._totalMsg = bytes(0)
        self._sign = bytes(0)

    @property
    def msgContent(self):
        return self._msgContent.decode('utf_16_le').replace('\x00','')
    @msgContent.setter
    def msgContent(self,value:str):
        if isinstance(value,str):
            self._msgContent = value.encode('utf_16_le')+b'\x00\x00'

    @property
    def sendResultInfo(self):
        return self._sendResultInfo.decode('gbk').replace('\x00','')
    @sendResultInfo.setter
    def sendResultInfo(self,value):
        if isinstance(value,str):
            self._sendResultInfo = value.encode('gbk')+b'\x00'

    @property
    def title(self):
        return self._title.decode('utf_16_le').replace('\x00','')
    @title.setter
    def title(self,value):
        if isinstance(value,str):
            self._title = value.encode('utf_16_le')+b'\x00\x00'

    @property
    def userDefineId(self):
        return self._userDefineId.decode('gbk').replace('\x00','')
    @userDefineId.setter
    def userDefineId(self,value):
        if isinstance(value,str):
            t = value.encode('gbk')
            self._userDefineId = t+bytes(33-len(t))

    @property
    def totalMsgLen(self):
        return self._totalMsgLen
    @totalMsgLen.setter
    def totalMsgLen(self,value:int):
        self._totalMsgLen = value

    @property
    def totalMsg(self):
        return self._totalMsg.decode('utf_16_le').replace('\x00','')
    @totalMsg.setter
    def totalMsg(self,value:str):
        if isinstance(value,str):
            self._totalMsg = value.encode('utf_16_le')+b'\x00\x00'

    @property
    def sign(self):
        return self._sign.decode('utf_16_le').replace('\x00','')
    @sign.setter
    def sign(self,value:str):
        if isinstance(value,str):
            t = value.encode('utf_16_le')
            self._sign = t + bytes(100-len(t))

class TSMsgHisRepData(object):
    __OneByte = struct.Struct("<qqidB64sdiqi")
    def __init__(self):
        self.mobilePhone        =0#; // 手机号码
        self.matchId            =0#; // 匹配编号
        self.resourceId         =0#; // 资源编号
        self._reportTime         =0#; // 消息回执时间
        self.reportState        =0#; // 状态报告是否成功
        self._reportResultInfo   =bytes(64)#; // 状态报告信息
        self._reportLocalTime    =0#; // 状态报告本地接收时间
        self.componentFlg       =0#;
        self.flagRetryTime      =0#; // 上次重试的时间，初始为零。
        self.cycletimes         =0#;

    def Value(self):
        return self.__OneByte.pack(*(
            self.mobilePhone,
            self.matchId,
            self.resourceId,
            self._reportTime,
            self.reportState,
            self._reportResultInfo,
            self._reportLocalTime,
            self.componentFlg,
            self.flagRetryTime,
            self.cycletimes,
        ))

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self.mobilePhone        = data[0]
        self.matchId            = data[1]
        self.resourceId         = data[2]
        self._reportTime        = data[3]
        self.reportState        = data[4]
        self._reportResultInfo  = data[5]
        self._reportLocalTime   = data[6]
        self.componentFlg       = data[7]
        self.flagRetryTime      = data[8]
        self.cycletimes         = data[9]

    def __len__(self):
        return self.__OneByte.size

    @property
    def reportResultInfo(self):
        return self._reportResultInfo.decode('gbk').replace('\x00','')
    @reportResultInfo.setter
    def reportResultInfo(self,value:str):
        t = value.encode('gbk')
        self._reportResultInfo = t + bytes(64 - len(t))

    @property
    def reportTime(self):
        return QtCore.QDateTime.fromTime_t(Datetime_dt(self._reportTime))
    @reportTime.setter
    def reportTime(self,value:QtCore.QDateTime):
        self._reportTime = dt_Datetime(value.toPyDateTime().ctime())

    @property
    def reportLocalTime(self):
        return QtCore.QDateTime.fromTime_t(Datetime_dt(self._reportLocalTime))
    @reportLocalTime.setter
    def reportLocalTime(self,value:QtCore.QDateTime):
        self._reportLocalTime = dt_Datetime(value.toPyDateTime().ctime())

class SMsgHisRepData(object):
    CType = MSG_HIS_REP
    CVersion = 0x10

    def __init__(self):
        self._head = MsgHeader()
        self._body = TSMsgHisRepData()

    def Value(self):
        try:
            return self._head.Value()+self._body.Value()
        except:
            raise Exception("module:{} func:{} line:{} error".format(
                __file__,sys._getframe().f_code.co_name,sys._getframe().f_lineno))

    def fromBytes(self,b):
        try:
            b = bytearray(b)
            l1 = len(self._head)
            l2 = len(self._body)
            self._head.fromBytes(b[:l1])
            if self._head.MessageType != self.CType:
                raise Exception("unknow data type:",self._head.MessageType)
            self._body.fromBytes(b[l1:l1+l2])
        except Exception as e:
            print(e)
            raise Exception("module:{} func:{} line:{} error".format(
                __file__,sys._getframe().f_code.co_name,sys._getframe().f_lineno))

    def write_header(self):
        self._head.MessageType = self.CType
        self._head.Version = self.CVersion
        self._head.Length = len(self._head)+len(self._body)

class SMOData(object):
    __OneByte = struct.Struct("<qq32sdii256sB30s")
    def __init__(self):
        self.msgId              =0#; // 信息编号
        self.mobilePhone        =0#; // 手机号码
        self._SPNo               =bytes(32)#;
        self._MOTime             =0#;
        self.resourceId         =0#; // 资源编号
        self.MOContentLength    =0#;
        self._MOContent          =bytes(256)#; // 此值直接放在消息队列中
        self.msgType            =0#; // 信息类型
        self._accountId          =bytes(30)#;

    def __len__(self):
        return self.__OneByte.size

    @property
    def SPNo(self):
        return self._SPNo.decode('gbk').replace('\x00','')
    @SPNo.setter
    def SPNo(self,value:str):
        t = value.encode('gbk')
        self._SPNo = t + bytes(32-len(t))

    @property
    def MOContent(self):
        return self._MOContent.decode('gbk').replace('\x00','')
    @MOContent.setter
    def MOContent(self, value: str):
        t = value.encode('gbk')
        self._MOContent = t + bytes(256 - len(t))

    @property
    def accountId(self):
        return self._accountId.decode('gbk').replace('\x00','')
    @accountId.setter
    def accountId(self, value: str):
        t = value.encode('gbk')
        self._accountId = t + bytes(30 - len(t))

    @property
    def MOTime(self):
        return QtCore.QDateTime.fromTime_t(Datetime_dt(self._MOTime))
    @MOTime.setter
    def MOTime(self,value:QtCore.QDateTime):
        self._MOTime = dt_Datetime(value.toPyDateTime().ctime())

    def Value(self):
        try:
            return self.__OneByte.pack(*(
                self.msgId,
                self.mobilePhone,
                self._SPNo,
                self._MOTime,
                self.resourceId,
                self.MOContentLength,
                self._MOContent,
                self.msgType,
                self._accountId,
            ))
        except:
            raise Exception("module:{} func:{} line:{} error".format(
                __file__,sys._getframe().f_code.co_name,sys._getframe().f_lineno))

    def fromBytes(self,b):
        #b = bytearray(b)
        try:
            data = self.__OneByte.unpack(b)
            self.msgId              = data[0]
            self.mobilePhone        = data[1]
            self._SPNo              = data[2]
            self._MOTime            = data[3]
            self.resourceId         = data[4]
            self.MOContentLength    = data[5]
            self._MOContent         = data[6]
            self.msgType            = data[7]
            self._accountId         = data[8]
        except:
            raise Exception("module:{} func:{} line:{} error".format(
                __file__,sys._getframe().f_code.co_name,sys._getframe().f_lineno))

class SRepNotifyData(object):
    __OneByte = struct.Struct("<Iq30sqBBdd64s64s24s16sd16sBBi33s")
    def __init__(self):
        self.version                =0#;
        self.msgId                  =0#;
        self._accountId             =bytes(30)#;
        self.mobilePhone            =0#;
        self.sendState              =0#;
        self.reportState            =0#;
        self._sendedTime            =0#;
        self._reportTime            =0#; // 消息回执时间
        self._sendResultInfo        =bytes(64)#;
        self._reportResultInfo      =bytes(64)#;
        self._spno                  =bytes(24)#;
        self._clientMsgId           =bytes(16)#;
        self._reportLocalTime       =0#; // 消息回执本地时间
        self._extendNum             =bytes(16)#; // 扩展号码
        self.pk_total               =0#;
        self.pk_num                 =0#;
        self.combinationVal         =0#;
        self._userDefineId          =bytes(33)#;
        self._extMem                =bytes(31)#;

    def __len__(self):
        return self.__OneByte.size

    @property
    def accountId(self):
        return self._accountId.decode('gbk').replace('\x00','')
    @accountId.setter
    def accountId(self, value: str):
        t = value.encode('gbk')
        self._accountId = t + bytes(30 - len(t))

    @property
    def sendResultInfo(self):
        return self._sendResultInfo.decode('gbk').replace('\x00','')
    @sendResultInfo.setter
    def sendResultInfo(self, value: str):
        t = value.encode('gbk')
        self._sendResultInfo = t + bytes(64 - len(t))

    @property
    def reportResultInfo(self):
        return self._reportResultInfo.decode('gbk').replace('\x00','')
    @reportResultInfo.setter
    def reportResultInfo(self, value: str):
        t = value.encode('gbk')
        self._reportResultInfo = t + bytes(64 - len(t))

    @property
    def spno(self):
        return self._spno.decode('gbk').replace('\x00','')
    @spno.setter
    def spno(self, value: str):
        t = value.encode('gbk')
        self._spno = t + bytes(24 - len(t))

    @property
    def clientMsgId(self):
        return self._clientMsgId.decode('gbk').replace('\x00','')
    @clientMsgId.setter
    def clientMsgId(self, value: str):
        t = value.encode('gbk')
        self._clientMsgId = t + bytes(16 - len(t))

    @property
    def extendNum(self):
        return self._extendNum.decode('gbk').replace('\x00','')
    @extendNum.setter
    def extendNum(self, value: str):
        t = value.encode('gbk')
        self._extendNum = t + bytes(16 - len(t))

    @property
    def userDefineId(self):
        return self._userDefineId.decode('gbk').replace('\x00','')
    @userDefineId.setter
    def userDefineId(self, value: str):
        t = value.encode('gbk')
        self._userDefineId = t + bytes(33 - len(t))

    @property
    def extMem(self):
        return self._extMem.decode('gbk').replace('\x00','')
    @extMem.setter
    def extMem(self, value: str):
        t = value.encode('gbk')
        self._extMem = t + bytes(31 - len(t))

    @property
    def sendedTime(self):
        return QtCore.QDateTime.fromTime_t(Datetime_dt(self._sendedTime))
    @sendedTime.setter
    def sendedTime(self,value:QtCore.QDateTime):
        self._sendedTime = dt_Datetime(value.toPyDateTime().ctime())

    @property
    def reportTime(self):
        return QtCore.QDateTime.fromTime_t(Datetime_dt(self._reportTime))
    @reportTime.setter
    def reportTime(self,value:QtCore.QDateTime):
        self._reportTime = dt_Datetime(value.toPyDateTime().ctime())

    @property
    def reportLocalTime(self):
        return QtCore.QDateTime.fromTime_t(Datetime_dt(self._reportLocalTime))
    @reportLocalTime.setter
    def reportLocalTime(self,value:QtCore.QDateTime):
        self._reportLocalTime = dt_Datetime(value.toPyDateTime().ctime())

    def Value(self):
        try:
            return self.__OneByte.pack(*(
                self.version,
                self.msgId,
                self._accountId,
                self.mobilePhone,
                self.sendState,
                self.reportState,
                self._sendedTime,
                self._reportTime,
                self._sendResultInfo,
                self._reportResultInfo,
                self._spno,
                self._clientMsgId,
                self._reportLocalTime,
                self._extendNum,
                self.pk_total,
                self.pk_num,
                self.combinationVal,
                self._userDefineId,
                #self._extMem
            ))
        except Exception as e:
            print(e)
            raise Exception("module:{} func:{} line:{} error".format(
                __file__,sys._getframe().f_code.co_name,sys._getframe().f_lineno))

    def fromBytes(self,b):
        try:
            data = self.__OneByte.unpack(b)
            self.version            = data[0]
            self.msgId              = data[1]
            self._accountId         = data[2]
            self.mobilePhone        = data[3]
            self.sendState          = data[4]
            self.reportState        = data[5]
            self._sendedTime        = data[6]
            self._reportTime        = data[7]
            self._sendResultInfo    = data[8]
            self._reportResultInfo  = data[9]
            self._spno              = data[10]
            self._clientMsgId       = data[11]
            self._reportLocalTime   = data[12]
            self._extendNum         = data[13]
            self.pk_total           = data[14]
            self.pk_num             = data[15]
            self.combinationVal     = data[16]
            self._userDefineId      = data[17]
            #self._extMem            = data[18]
        except Exception as e:
            print(e)
            raise Exception("module:{} func:{} line:{} error".format(
                __file__,sys._getframe().f_code.co_name,sys._getframe().f_lineno))

class ResourceStateNotify(object):
    __OneByte = struct.Struct("<idBiiiiiii")
    def __init__(self):
        self.ResourceId             =0#; // 资源ID
        self._NotifyTime             =0#; // 报告时间
        self.RunTimeState           =0#; // 资源状态
        self.QueueStock             =0#; // 含义变更为消息队列的积压数量
        self.lastTimeQueueStock     =0#;
        self.reportTimeInterval     =0#;
        self.submitTotal            =0#;
        self.submitFail             =0#;
        self.reportTotal            =0#;
        self.reportFail             =0#;

    def __len__(self):
        return self.__OneByte.size

    @property
    def NotifyTime(self):
        return QtCore.QDateTime.fromTime_t(Datetime_dt(self._NotifyTime))
    @NotifyTime.setter
    def NotifyTime(self,value:QtCore.QDateTime):
        self._NotifyTime = dt_Datetime(value.toPyDateTime().ctime())

    def Value(self):
        try:
            return self.__OneByte.pack(*(
                self.ResourceId,
                self._NotifyTime,
                self.RunTimeState,
                self.QueueStock,
                self.lastTimeQueueStock,
                self.reportTimeInterval,
                self.submitTotal,
                self.submitFail,
                self.reportTotal,
                self.reportFail,
            ))
        except:
            raise Exception("module:{} func:{} line:{} error".format(
                __file__,sys._getframe().f_code.co_name,sys._getframe().f_lineno))

    def fromBytes(self,b):
        try:
            data = self.__OneByte.unpack(b)
            self.ResourceId         = data[0]
            self._NotifyTime         = data[1]
            self.RunTimeState       = data[2]
            self.QueueStock         = data[3]
            self.lastTimeQueueStock = data[4]
            self.reportTimeInterval = data[5]
            self.submitTotal        = data[6]
            self.submitFail         = data[7]
            self.reportTotal        = data[8]
            self.reportFail         = data[9]
        except:
            raise Exception("module:{} func:{} line:{} error".format(
                __file__,sys._getframe().f_code.co_name,sys._getframe().f_lineno))

class SDispatchStatistics(object):
    CType = MSG_DSP_STC
    CVersion = 0x10

    __OneByte = struct.Struct("<iiiihq64s")
    def __init__(self):
        self._head = MsgHeader()
        self.dispatchCenterId   = 0
        self.totalDispatchCnt   = 0
        self.succDispatchCnt    = 0
        self.failDispatchCnt    = 0
        self.cycleTime          = 0
        self.createTime         = 0
        self._extendMem         = bytes(64)

    def Value(self):
        try:
            return self._head.Value()+self.__OneByte.pack(*(
                self.dispatchCenterId,
                self.totalDispatchCnt,
                self.succDispatchCnt,
                self.failDispatchCnt,
                self.cycleTime,
                self.createTime,
                self._extendMem,
            ))
        except:
            raise Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))

    def fromBytes(self,b):
        try:
            b = bytearray(b)
            l1 = len(self._head)
            l2 = self.__OneByte.size
            self._head.fromBytes(b[:l1])
            data = self.__OneByte.unpack(b[l1:l1+l2])
            self.dispatchCenterId   = data[0]
            self.totalDispatchCnt   = data[1]
            self.succDispatchCnt    = data[2]
            self.failDispatchCnt    = data[3]
            self.cycleTime          = data[4]
            self.createTime         = data[5]
            self._extendMem         = data[6]
        except:
            raise Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))

    def write_header(self):
        self._head.MessageType = self.CType
        self._head.Version = self.CVersion
        self._head.Length = len(self._head)+self.__OneByte.size

    @property
    def extendMem(self):
        return self._extendMem.decode('utf-8').replace('\x00','')
    @extendMem.setter
    def extendMem(self,value:str):
        t = value.encode("utf-8")
        self._extendMem = t + bytes(64-len(t))

class SResComStatistics(object):
    CType = 0
    CVersion = 0x10
    __OneByte = struct.Struct("<iiihq64s")
    def __init__(self):
        self._head = MsgHeader()
        self.resourceId     = 0
        self.succCnt        = 0
        self.failCnt        = 0
        self.cycleTime      = 0
        self.createTime     = 0
        self._extendMem      = bytes(64)

    def Value(self):
        try:
            return self._head.Value() + self.__OneByte.pack(*(
                self.resourceId,
                self.succCnt,
                self.failCnt,
                self.cycleTime,
                self.createTime,
                self._extendMem,
            ))
        except:
            raise Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))

    def fromBytes(self,b):
        try:
            b = bytearray(b)
            l1 = len(self._head)
            l2 = self.__OneByte.size
            self._head.fromBytes(b[:l1])
            data = self.__OneByte.unpack(b[l1:l1+l2])
            self.resourceId = data[0]
            self.succCnt    = data[1]
            self.failCnt    = data[2]
            self.cycleTime  = data[3]
            self.createTime = data[4]
            self._extendMem  = data[5]
        except:
            raise Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))


    @property
    def extendMem(self):
        return self._extendMem.decode('utf-8').replace('\x00','')
    @extendMem.setter
    def extendMem(self,value:str):
        t = value.encode("utf-8")
        self._extendMem = t + bytes(64-len(t))




class SResourceState(Structure):
    __OneByte = struct.Struct('<idiiiiiiiiiiiii')
    _fields_ = [
        ('resourceId',c_int),
        ('_reportTime', c_double),
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
        ('state', c_int),
    ]
    _pack_ = 1

    def Value(self):
        return Pack(self)
        pass

    def fromBytes(self, b):
        try:
            data = UnPack(SResourceState,b)
            self.resourceId             = data.resourceId
            self._reportTime             = data._reportTime
            self.statisticsConfig       = data.statisticsConfig
            self.currentStock           = data.currentStock
            self.lastStock              = data.lastStock
            self.reportTimeInterval     = data.reportTimeInterval
            self.submitTotal            = data.submitTotal
            self.currentSubmitSuccess   = data.currentSubmitSuccess
            self.currentSubmitFail      = data.currentSubmitFail
            self.reportTotal            = data.reportTotal
            self.currentReportSuccess   = data.currentReportSuccess
            self.currentReportFail      = data.currentReportFail
            self.moTotal                = data.moTotal
            self.currentMoTotal         = data.currentMoTotal
            self.state                  = data.state
        except Exception as e:
            print(e)
        pass

    @property
    def reportTime(self):
        return QtCore.QDateTime.fromTime_t(Datetime_dt(self._reportTime))
    @reportTime.setter
    def reportTime(self,value):
        self._reportTime = dt_Datetime(value.toPyDateTime().ctime())