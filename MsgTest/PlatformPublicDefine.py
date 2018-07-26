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
        self.node = []


    PROPERTY_W_ITEM_W(message, ECMI_CONTENT);
    PROPERTY_W_ITEM_COPY_W(message, ECMI_CONTENT);
    PROPERTY_R_ITEM_W(message, ECMI_CONTENT);
    PROPERTY_W_ITEM(mms_content, ECMI_CONTENT);
    PROPERTY_R_ITEM_A(mms_content, ECMI_CONTENT);

    //ECMI_ACC_NAME
    PROPERTY_W_ITEM_A(acc_name, ECMI_ACC_NAME);
    PROPERTY_W_ITEM_COPY_A(acc_name, ECMI_ACC_NAME);
    PROPERTY_R_ITEM_A(acc_name, ECMI_ACC_NAME);

    //ECMI_TEMPLATE_ID
    PROPERTY_W_ITEM_A(templateID, ECMI_TEMPLATE_ID);
    PROPERTY_W_ITEM_COPY_A(templateID, ECMI_TEMPLATE_ID);
    PROPERTY_R_ITEM_A(templateID, ECMI_TEMPLATE_ID);

    //ECMI_MSG_TEMPLATE
    PROPERTY_W_ITEM_W(msgtemplate, ECMI_MSG_TEMPLATE);
    PROPERTY_W_ITEM_COPY_W(msgtemplate, ECMI_MSG_TEMPLATE);
    PROPERTY_R_ITEM_W(msgtemplate, ECMI_MSG_TEMPLATE);
    PROPERTY_R_ITEM_A(msgtemplate, ECMI_MSG_TEMPLATE);

    //ECMI_MOBILE
    PROPERTY_W_ITEM_A(mobile, ECMI_MOBILE);
    PROPERTY_W_ITEM_COPY_A(mobile, ECMI_MOBILE);
    PROPERTY_R_ITEM_A(mobile, ECMI_MOBILE);
    PROPERTY_A_ITEM_A(mobile, ECMI_MOBILE);
    PROPERTY_A_ITEM_A_S(mobile, ECMI_MOBILE);

    //ECMI_SIGN
    PROPERTY_W_ITEM_W(sign, ECMI_SIGN);
    PROPERTY_W_ITEM_COPY_W(sign, ECMI_SIGN);
    PROPERTY_R_ITEM_W(sign, ECMI_SIGN);

    //ECMI_EXT_NUMBER
    PROPERTY_W_ITEM_A(extnumber, ECMI_EXT_NUMBER);
    PROPERTY_W_ITEM_COPY_A(extnumber, ECMI_EXT_NUMBER);
    PROPERTY_R_ITEM_A(extnumber, ECMI_EXT_NUMBER);

#ifdef EXTEND_PARAM
    //ECMI_USER_DEF_ID
    PROPERTY_W_ITEM_A(user_defid, ECMI_USER_DEF_ID);
    PROPERTY_W_ITEM_COPY_A(user_defid, ECMI_USER_DEF_ID);
    PROPERTY_R_ITEM_A(user_defid, ECMI_USER_DEF_ID);
#endif //EXTEND_PARAM

    //ECMI_ACC_MSGID
    PROPERTY_W_ITEM_A(acc_msgid, ECMI_ACC_MSGID);
    PROPERTY_W_ITEM_COPY_A(acc_msgid, ECMI_ACC_MSGID);
    PROPERTY_R_ITEM_A(acc_msgid, ECMI_ACC_MSGID);

    //ECMI_MMS_TITLE
    PROPERTY_W_ITEM_W(mms_title, ECMI_MMS_TITLE);
    PROPERTY_W_ITEM_COPY_W(mms_title, ECMI_MMS_TITLE);
    PROPERTY_R_ITEM_W(mms_title, ECMI_MMS_TITLE);

    //ECMI_MMS_FILENAME
    PROPERTY_W_ITEM_A(mms_path, ECMI_MMS_FILENAME);
    PROPERTY_W_ITEM_COPY_A(mms_path, ECMI_MMS_FILENAME);
    PROPERTY_R_ITEM_A(mms_path, ECMI_MMS_FILENAME);