import struct
from enum import Enum

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


class DispatchFixedHead(object):
    __OneByte = struct.Struct("<BQIIddddiBBdHIIIIbbhbBBBIIb")
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
        self.m_old_struct           =0

    def Value(self):
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
            self.m_old_struct,
        ))

    def fromBytes(self,b):
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
        self.MsgType                = data[11]
        self.CommitTime             = data[12]
        self.Package                = data[13]
        self.MobilesContentLen      = data[14]
        self.MsgContentLen          = data[15]
        self.MobilesCount           = data[16]
        self.DispatchTimes          = data[17]
        self.Telcom                 = data[18]
        self.ProvinceId             = data[19]
        self.CityId                 = data[20]
        self.TPCBChecked            = data[21]
        self.SendedTimes            = data[22]
        self.DispatchFailedState    = data[23]
        self.SubmitType             = data[24]
        self.CloudMsgTemplateID     = data[25]
        self.CommitIp               = data[26]
        self.m_old_struct           = data[27]

    def __len__(self):
        return self.__OneByte.size


class DispatchFixedTail(object):
    __OneByte = struct.Struct('<BHiiBdHiBiii')
    def __init__(self):
        self.pagetotalself          =0
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

    def Value(self):
        return self.__OneByte.pack(*(
            self.pagetotalself,
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
        ))

    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self.pagetotalself          = data[0]
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

    def __len__(self):
        return self.__OneByte.size

class Node(object):
    __OneByte = struct.Struct("<II")
    def __init__(self):
        self.m_offset = 0
        self.m_size = 0
    def Value(self):
        return self.__OneByte.pack(*(self.m_offset,self.m_size))


    def fromBytes(self,b):
        data = self.__OneByte.unpack(b)
        self.m_offset = data[0]
        self.m_size = data[1]

    def __len__(self):
        return self.__OneByte.size


class SCloudMessage(object):
    impl_type = 0
    impl_version = 1
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

        self._mobiles = ''
        self._acc_name = ''
        self._message = ''
        self._templateID = ''
        self._msgtemplate = ''
        self._extnumer = ''
        self._sign = ''
        self._acc_msgid = ''
        self._mms_title = ''
        self._mms_filename = ''
        self._usr_def_id = ''

        self.msgheader._item_count = self.ECloudMsgItem.EBMI_ITEM_COUNT.value
        self.msgheader._offset = len(self.msgheader)+len(self.FixHead)+len(self.FixTail)

    def Value(self):
        l = 0
        for i in range(self.ECloudMsgItem.EBMI_ITEM_COUNT.value):
            l+=self.node[i].m_size
        self.__OneByte = struct.Struct("<%ds" %(l,))
        #定长
        value = self.msgheader.Value()+self.FixHead.Value()+self.FixTail.Value()
        #动长node
        for i in range(self.ECloudMsgItem.EBMI_ITEM_COUNT.value):
            value += self.node[i].Value()
        #动长
        value +=self.__OneByte.pack(*(
                            self._mobiles,
                            self._acc_name,
                            self._message,
                            self._templateID,
                            self._msgtemplate,
                            self._extnumer,
                            self._sign,
                            self._acc_msgid,
                            self._mms_title,
                            self._mms_filename,
                            self._usr_def_id,))
        return value

    def fromBytes(self,b):
        b = bytearray(b)
        l1 = len(self.msgheader)
        l2 = len(self.FixHead)
        l3 = len(self.FixTail)
        l4 = len(self.node[0])
        l5 = self.msgheader._offset+7*l4
        self.msgheader.fromBytes(b[:l1])
        self.FixHead.fromBytes(b[l1:l1+l2])
        self.FixTail.fromBytes(b[l1+l2:l1+l2+l3])
        for i in range(self.msgheader._item_count):
            self.node[i].fromBytes(b[l1+l2+l3+i*l4:l1+l2+l3+(i+1)*l4])
        self._mobiles           = bytes(b[l5 + self.node[0].m_offset:l5 + self.node[0].m_offset + self.node[0].m_size])
        self._acc_name          = bytes(b[l5+self.node[1].m_offset:l5+self.node[1].m_offset+self.node[1].m_size])
        self._message           = bytes(b[l5+self.node[2].m_offset:l5+self.node[2].m_offset+self.node[2].m_size])
        self._templateID        = bytes(b[l5+self.node[3].m_offset:l5+self.node[3].m_offset+self.node[3].m_size])
        self._msgtemplate       = bytes(b[l5+self.node[4].m_offset:l5+self.node[4].m_offset+self.node[4].m_size])
        self._extnumer          = bytes(b[l5+self.node[5].m_offset:l5+self.node[5].m_offset+self.node[5].m_size])
        self._sign              = bytes(b[l5+self.node[6].m_offset:l5+self.node[6].m_offset+self.node[6].m_size])
        self._acc_msgid         = bytes(b[l5+self.node[7].m_offset:l5+self.node[7].m_offset+self.node[7].m_size])
        self._mms_title         = bytes(b[l5+self.node[8].m_offset:l5+self.node[8].m_offset+self.node[8].m_size])
        self._mms_filename      = bytes(b[l5+self.node[9].m_offset:l5+self.node[9].m_offset+self.node[9].m_size])
        self._usr_def_id        = bytes(b[l5+self.node[10].m_offset:l5+self.node[10].m_offset+self.node[10].m_size])

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

    def write_getsize(self,index,text):
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
            else:
                raise TypeError(text)
            return len(self._message)
        elif index == 3:
            if isinstance(text,str):
                self._templateID = bytes(text,encoding='utf-8')+b'\x00'
            else:
                raise TypeError(text)
            return len(self._templateID)+1
        elif index == 4:
            if isinstance(text,str):
                self._msgtemplate = bytes(text,encoding='utf-8')+b'\x00'
            else:
                raise TypeError(text)
            return len(self._msgtemplate)
        elif index == 5:
            if isinstance(text,str):
                self._extnumer = text.encode('utf-8')+b'\x00'
            else:
                raise TypeError(text)
            return len(self._extnumer)
        elif index == 6:
            if isinstance(text,str):
                self._sign = bytes(text,encoding='utf_16_le')+b'\x00\x00'
            else:
                raise TypeError(text)
            return len(self._sign)
        elif index == 7:
            if isinstance(text,str):
                self._acc_msgid = bytes(text,encoding='utf-8')+b'\x00'
            else:
                raise TypeError(text)
            return len(self._acc_msgid)
        elif index == 8:
            if isinstance(text,str):
                self._mms_title = bytes(text,encoding='utf_16_le')+b'\x00\x00'
            else:
                raise TypeError(text)
            return len(self._mms_title)
        elif index == 9:
            if isinstance(text,str):
                self._mms_filename = bytes(text,encoding='utf-8')+b'\x00'
            else:
                raise TypeError(text)
            return len(self._mms_filename)
        elif index == 10:
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
        return self._mobiles
    @mobiles.setter
    def mobiles(self,value):
        self.__write_item(self.ECloudMsgItem.ECMI_MOBILE.value,value)

    @property
    def acc_name(self):
        return self._acc_name
    @acc_name.setter
    def acc_name(self,value):
        self.__write_item(self.ECloudMsgItem.ECMI_ACC_NAME.value,value)

    @property
    def message(self):
        return self._message
    @message.setter
    def message(self,value):
        self.__write_item(self.ECloudMsgItem.ECMI_ITEM_COUNT.value,value)

    @property
    def templateID(self):
        return self._templateID
    @templateID.setter
    def templateID(self,value):
        self.__write_item(self.ECloudMsgItem.ECMI_TEMPLATE_ID.value,value)

    @property
    def msgtemplate(self):
        return self._msgtemplate
    @msgtemplate.setter
    def msgtemplate(self,value):
        self.__write_item(self.ECloudMsgItem.ECMI_MSG_TEMPLATE.value,value)

    @property
    def extnumer(self):
        return self._extnumer
    @extnumer.setter
    def extnumer(self,value):
        self.__write_item(self.ECloudMsgItem.ECMI_EXT_NUMBER.value,value)

    @property
    def sign(self):
        return self._sign
    @sign.setter
    def sign(self,value):
        self.__write_item(self.ECloudMsgItem.ECMI_SIGN.value,value)

    @property
    def acc_msgid(self):
        return self._acc_msgid
    @acc_msgid.setter
    def acc_msgid(self,value):
        self.__write_item(self.ECloudMsgItem.ECMI_ACC_MSGID.value,value)

    @property
    def mms_title(self):
        return self._mms_title
    @mms_title.setter
    def mms_title(self,value):
        self.__write_item(self.ECloudMsgItem.ECMI_MMS_TITLE.value,value)

    @property
    def mms_filename(self):
        return self.mms_filename
    @mms_filename.setter
    def mms_filename(self,value):
        self.__write_item(self.ECloudMsgItem.ECMI_MMS_FILENAME.value,value)

    @property
    def usr_def_id(self):
        return self._usr_def_id
    @usr_def_id.setter
    def usr_def_id(self,value):
        self.__write_item(self.ECloudMsgItem.ECMI_USER_DEF_ID.value,value)



