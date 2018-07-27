from PyQt5 import QtWidgets,QtCore
import time
import socket
import struct
from ctypes import *
from configparser import ConfigParser
from UI_SCloudMsg import Ui_CloudMsg
from PlatformPublicDefine import SCloudMessage
from BMSMessage import dt_time,time_dt,dt_Datetime,Datetime_dt,bytes2int,int2ipbyte


m_section = ['SCloudMsg']

m_keys_cloudmsg = (
    '消息级别',
    'msgid',
    '扩展产品',
    '真实发送扩展产品',
    '开始发送日期',
    '结束发送日期',
    '开始发送时段',
    '结束发送时段',
    '计费号码数',
    '消息状态',
    '信息类型',
    '提交时间',
    '包号',
    '号码内容长度',
    '信息内容长度',
    '号码个数',
    '调度次数',
    '运营商',
    '号码归属省份',
    '号码归属城市',
    '是否定位',
    '已发送次数',
    '调度失败状态',
    '提交接口',
    '模板ID',
    '提交IP',
    '旧消息',
    '信息总页数',
    '信息总包数',
    '信息类型组合值',
    '最后一次资源发送失败id',
    '失败类型',
    '最后一次调度时间',
    '资源发送次数',
    '审核id',
    '发送次数',
    '回执重发的超时时长',
    '进入调度中心次数',
    '扩展组合值',
    '电话号码',
    '提交帐号',
    '短信内容',
    '运营商模板ID',
    '模板内容',
    '模板参数',
    '扩展号码',
    '签名',
    '客户自定义参数',
    '彩信标题',
    '彩信存储文件路径',
    '用户自定义参数',
)

class CloudMsg(QtWidgets.QWidget,Ui_CloudMsg):
    def __init__(self):
        super(CloudMsg,self).__init__()
        self.setupUi(self)
        self.__data = SCloudMessage()

    def getValue(self):
        try:
            self.__data.clear()
            #head
            self.__data.FixHead.Priority                = int(self.Priority.text())
            self.__data.FixHead.MsgId                   = int(self.MsgId.text())
            self.__data.FixHead.ProductExtendId         = int(self.ProductExtendId.text())
            self.__data.FixHead.RealProductExtendId     = int(self.RealProductExtendId.text())
            self.__data.FixHead.StartSendDateTime       = dt_Datetime(self.StartSendDateTime.dateTime().toPyDateTime().ctime())
            self.__data.FixHead.EndSendDateTime         = dt_Datetime(self.EndSendDateTime.dateTime().toPyDateTime().ctime())
            self.__data.FixHead.StartSendTime           = dt_Datetime(self.StartSendTime.dateTime().toPyDateTime().ctime())
            self.__data.FixHead.EndSendTime             = dt_Datetime(self.EndSendTime.dateTime().toPyDateTime().ctime())
            self.__data.FixHead.ChargeQuantity          = int(self.ChargeQuantity.text())
            self.__data.FixHead.MsgState                = self.MsgState.currentIndex()+1
            self.__data.FixHead.MsgType                 = self.MsgType.currentIndex()+1
            self.__data.FixHead.CommitTime              = dt_Datetime(self.CommitTime.dateTime().toPyDateTime().ctime())
            self.__data.FixHead.Package                 = int(self.Package.text())
            self.__data.FixHead.MobilesContentLen       = int(self.MobilesContentLen.text())
            self.__data.FixHead.MsgContentLen           = int(self.MsgContentLen.text())
            self.__data.FixHead.MobilesCount            = int(self.MobilesCount.text())
            self.__data.FixHead.DispatchTimes           = int(self.DispatchTimes.text())
            self.__data.FixHead.Telcom                  = self.Telcom.currentIndex()
            self.__data.FixHead.ProvinceId              = int(self.ProvinceId.text())
            self.__data.FixHead.CityId                  = int(self.CityId.text())
            self.__data.FixHead.TPCBChecked             = int(self.TPCBChecked.text())
            self.__data.FixHead.SendedTimes             = int(self.SendedTimes.text())
            self.__data.FixHead.DispatchFailedState     = int(self.DispatchFailedState.text())
            self.__data.FixHead.SubmitType              = int(self.SubmitType.text())
            self.__data.FixHead.CloudMsgTemplateID      = int(self.CloudMsgTemplateID.text())
            self.__data.FixHead.CommitIp                = bytes2int(socket.inet_aton(self.CommitIp.text()))
            self.__data.FixHead.m_old_struct            = int(self.m_old_struct.text())

            #tail
            self.__data.FixTail.pagetotal =             int(self.pagetotal.text())
            self.__data.FixTail.packagetotal =          int(self.packagetotal.text())
            self.__data.FixTail.typeComponentParam =    int(self.typeComponentParam.text())
            self.__data.FixTail.lastFailResourceId =    int(self.lastFailResourceId.text())
            self.__data.FixTail.failedType =            self.failedType.currentIndex()
            self.__data.FixTail.lastDiapatchTime =      dt_Datetime(self.lastDiapatchTime.dateTime().toPyDateTime().ctime())
            self.__data.FixTail.resourceSendTimes =     int(self.resourceSendTimes.text())
            self.__data.FixTail.auditorId =             int(self.auditorId.text())
            self.__data.FixTail.totalSendTimes =        int(self.totalSendTimes.text())
            self.__data.FixTail.repResendTimeOut =      int(self.repResendTimeOut.text())
            self.__data.FixTail.innerDispatchTimes =    int(self.innerDispatchTimes.text())
            self.__data.FixTail.extComponentParam =     int(self.extComponentParam.text())
            ##
            self.__data.mobiles = self.mobile.toPlainText()
            self.__data.acc_name = self.acc_name.text()
            self.__data.message = self.message.toPlainText()
            self.__data.templateID = self.templateID.text()
            self.__data.msgtemplate = self.msgtemplate.toPlainText()
            self.__data.paramtemplate = self.paramtemplate.toPlainText()
            self.__data.extnumer = self.extnumber.text()
            self.__data.sign = self.sign.text()
            self.__data.acc_msgid = self.acc_msgid.text()
            self.__data.mms_title = self.mms_title.text()
            self.__data.mms_filename = self.mms_path.text()
            self.__data.usr_def_id =self.user_defid.text()
            self.__data.write_header()

            return self.__data.Value()
        except:
            print('getValue error')

    def updatedata(self):
        self.__data.FixHead.MsgId +=1

    def saveConfig(self, filename):
        try:
            config = ConfigParser()
            config.add_section(m_section[0])

            config.set(m_section[0], m_keys_cloudmsg[0],self.Priority.text())
            config.set(m_section[0], m_keys_cloudmsg[1],self.MsgId.text())
            config.set(m_section[0], m_keys_cloudmsg[2],self.ProductExtendId.text())
            config.set(m_section[0], m_keys_cloudmsg[3],self.RealProductExtendId.text())
            config.set(m_section[0], m_keys_cloudmsg[4],self.StartSendDateTime.dateTime().toString())
            config.set(m_section[0], m_keys_cloudmsg[5],self.EndSendDateTime.dateTime().toString())
            config.set(m_section[0], m_keys_cloudmsg[6],self.StartSendTime.dateTime().toString())
            config.set(m_section[0], m_keys_cloudmsg[7],self.EndSendTime.dateTime().toString())
            config.set(m_section[0], m_keys_cloudmsg[8],self.ChargeQuantity.text())
            config.set(m_section[0], m_keys_cloudmsg[9],str(self.MsgState.currentIndex()))
            config.set(m_section[0], m_keys_cloudmsg[10],str(self.MsgType.currentIndex()))
            config.set(m_section[0], m_keys_cloudmsg[11],self.CommitTime.dateTime().toString())
            config.set(m_section[0], m_keys_cloudmsg[12],self.Package.text())
            config.set(m_section[0], m_keys_cloudmsg[13],self.MobilesContentLen.text())
            config.set(m_section[0], m_keys_cloudmsg[14],self.MsgContentLen.text())
            config.set(m_section[0], m_keys_cloudmsg[15],self.MobilesCount.text())
            config.set(m_section[0], m_keys_cloudmsg[16],self.DispatchTimes.text())
            config.set(m_section[0], m_keys_cloudmsg[17],str(self.Telcom.currentIndex()))
            config.set(m_section[0], m_keys_cloudmsg[18],self.ProvinceId.text())
            config.set(m_section[0], m_keys_cloudmsg[19],self.CityId.text())
            config.set(m_section[0], m_keys_cloudmsg[20],self.TPCBChecked.text())
            config.set(m_section[0], m_keys_cloudmsg[21],self.SendedTimes.text())
            config.set(m_section[0], m_keys_cloudmsg[22],self.DispatchFailedState.text())
            config.set(m_section[0], m_keys_cloudmsg[23],self.SubmitType.text())
            config.set(m_section[0], m_keys_cloudmsg[24],self.CloudMsgTemplateID.text())
            config.set(m_section[0], m_keys_cloudmsg[25],self.CommitIp.text())
            config.set(m_section[0], m_keys_cloudmsg[26],self.m_old_struct.text())

            config.set(m_section[0], m_keys_cloudmsg[27],self.pagetotal.text())
            config.set(m_section[0], m_keys_cloudmsg[28],self.packagetotal.text())
            config.set(m_section[0], m_keys_cloudmsg[29],self.typeComponentParam.text())
            config.set(m_section[0], m_keys_cloudmsg[30],self.lastFailResourceId.text())
            config.set(m_section[0], m_keys_cloudmsg[31],str(self.failedType.currentIndex()))
            config.set(m_section[0], m_keys_cloudmsg[32],self.lastDiapatchTime.dateTime().toString())
            config.set(m_section[0], m_keys_cloudmsg[33],self.resourceSendTimes.text())
            config.set(m_section[0], m_keys_cloudmsg[34],self.auditorId.text())
            config.set(m_section[0], m_keys_cloudmsg[35],self.totalSendTimes.text())
            config.set(m_section[0], m_keys_cloudmsg[36],self.repResendTimeOut.text())
            config.set(m_section[0], m_keys_cloudmsg[37],self.innerDispatchTimes.text())
            config.set(m_section[0], m_keys_cloudmsg[38],self.extComponentParam.text())

            config.set(m_section[0], m_keys_cloudmsg[39],self.mobile.toPlainText())
            config.set(m_section[0], m_keys_cloudmsg[40],self.acc_name.text())
            config.set(m_section[0], m_keys_cloudmsg[41],self.message.toPlainText())
            config.set(m_section[0], m_keys_cloudmsg[42],self.templateID.text())
            config.set(m_section[0], m_keys_cloudmsg[43],self.msgtemplate.toPlainText())
            config.set(m_section[0], m_keys_cloudmsg[44],self.paramtemplate.toPlainText())
            config.set(m_section[0], m_keys_cloudmsg[45],self.extnumber.text())
            config.set(m_section[0], m_keys_cloudmsg[46],self.sign.text())
            config.set(m_section[0], m_keys_cloudmsg[47],self.acc_msgid.text())
            config.set(m_section[0], m_keys_cloudmsg[48],self.mms_title.text())
            config.set(m_section[0], m_keys_cloudmsg[49],self.mms_path.text())
            config.set(m_section[0], m_keys_cloudmsg[50],self.user_defid.text())

            with open('config/'+filename+'.ini','w',encoding='utf-8') as f:
                config.write(f)
        except:
            print('保存配置失败')

    def loadConfig(self,filename):
        try:
            config = ConfigParser()
            config.read(filename,encoding='utf-8')
            if not config.has_section(m_section[0]):
                print(filename,'do not have section',m_section[0])
                return False
            if len(config.items(m_section[0])) != len(m_keys_cloudmsg):
                print(filename,'items error\n allkeys:\n',m_keys_cloudmsg)
                return False
            self.Priority.setText(config[m_section[0]][m_keys_cloudmsg[0]])
            self.MsgId.setText(config[m_section[0]][m_keys_cloudmsg[1]])
            self.ProductExtendId.setText(config[m_section[0]][m_keys_cloudmsg[2]])
            self.RealProductExtendId.setText(config[m_section[0]][m_keys_cloudmsg[3]])
            self.StartSendDateTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[0]][m_keys_cloudmsg[4]]))
            self.EndSendDateTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[0]][m_keys_cloudmsg[5]]))
            self.StartSendTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[0]][m_keys_cloudmsg[6]]))
            self.EndSendTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[0]][m_keys_cloudmsg[7]]))
            self.ChargeQuantity.setText(config[m_section[0]][m_keys_cloudmsg[8]])
            self.MsgState.setCurrentIndex(int(config[m_section[0]][m_keys_cloudmsg[9]]))
            self.MsgType.setCurrentIndex(int(config[m_section[0]][m_keys_cloudmsg[10]]))
            self.CommitTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[0]][m_keys_cloudmsg[11]]))
            self.Package.setText(config[m_section[0]][m_keys_cloudmsg[12]])
            self.MobilesContentLen.setText(config[m_section[0]][m_keys_cloudmsg[13]])
            self.MsgContentLen.setText(config[m_section[0]][m_keys_cloudmsg[14]])
            self.MobilesCount.setText(config[m_section[0]][m_keys_cloudmsg[15]])
            self.DispatchTimes.setText(config[m_section[0]][m_keys_cloudmsg[16]])
            self.Telcom.setCurrentIndex(int(config[m_section[0]][m_keys_cloudmsg[17]]))
            self.ProvinceId.setText(config[m_section[0]][m_keys_cloudmsg[18]])
            self.CityId.setText(config[m_section[0]][m_keys_cloudmsg[19]])
            self.TPCBChecked.setText(config[m_section[0]][m_keys_cloudmsg[20]])
            self.SendedTimes.setText(config[m_section[0]][m_keys_cloudmsg[21]])
            self.DispatchFailedState.setText(config[m_section[0]][m_keys_cloudmsg[22]])
            self.SubmitType.setText(config[m_section[0]][m_keys_cloudmsg[23]])
            self.CloudMsgTemplateID.setText(config[m_section[0]][m_keys_cloudmsg[24]])
            self.CommitIp.setText(config[m_section[0]][m_keys_cloudmsg[25]])
            self.m_old_struct.setText(config[m_section[0]][m_keys_cloudmsg[26]])

            # tail
            self.pagetotal.setText(config[m_section[0]][m_keys_cloudmsg[27]])
            self.packagetotal.setText(config[m_section[0]][m_keys_cloudmsg[28]])
            self.typeComponentParam.setText(config[m_section[0]][m_keys_cloudmsg[29]])
            self.lastFailResourceId.setText(config[m_section[0]][m_keys_cloudmsg[30]])
            self.failedType.setCurrentIndex(int(config[m_section[0]][m_keys_cloudmsg[31]]))
            self.lastDiapatchTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[0]][m_keys_cloudmsg[32]]))
            self.resourceSendTimes.setText(config[m_section[0]][m_keys_cloudmsg[33]])
            self.auditorId.setText(config[m_section[0]][m_keys_cloudmsg[34]])
            self.totalSendTimes.setText(config[m_section[0]][m_keys_cloudmsg[35]])
            self.repResendTimeOut.setText(config[m_section[0]][m_keys_cloudmsg[36]])
            self.innerDispatchTimes.setText(config[m_section[0]][m_keys_cloudmsg[37]])
            self.extComponentParam.setText(config[m_section[0]][m_keys_cloudmsg[38]])
            ##
            self.mobile.setText(config[m_section[0]][m_keys_cloudmsg[39]])
            self.acc_name.setText(config[m_section[0]][m_keys_cloudmsg[40]])
            self.message.setText(config[m_section[0]][m_keys_cloudmsg[41]])
            self.templateID.setText(config[m_section[0]][m_keys_cloudmsg[42]])
            self.msgtemplate.setText(config[m_section[0]][m_keys_cloudmsg[43]])
            self.paramtemplate.setText(config[m_section[0]][m_keys_cloudmsg[44]])
            self.extnumber.setText(config[m_section[0]][m_keys_cloudmsg[45]])
            self.sign.setText(config[m_section[0]][m_keys_cloudmsg[46]])
            self.acc_msgid.setText(config[m_section[0]][m_keys_cloudmsg[47]])
            self.mms_title.setText(config[m_section[0]][m_keys_cloudmsg[48]])
            self.mms_path.setText(config[m_section[0]][m_keys_cloudmsg[49]])
            self.user_defid.setText(config[m_section[0]][m_keys_cloudmsg[50]])
        except:
            print('加载配置失败')

    def analyze(self,b):
        self.__data.fromBytes(b)
        self.__analyze()

    def __analyze(self):
        try:
            #head
            self.Priority.setText(str(self.__data.FixHead.Priority))
            self.MsgId.setText(str(self.__data.FixHead.MsgId))
            self.ProductExtendId.setText(str(self.__data.FixHead.ProductExtendId))
            self.RealProductExtendId.setText(str(self.__data.FixHead.RealProductExtendId))
            self.StartSendDateTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data.FixHead.StartSendDateTime)))
            self.EndSendDateTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data.FixHead.EndSendDateTime)))
            self.StartSendTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data.FixHead.StartSendTime)))
            self.EndSendTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data.FixHead.EndSendTime)))
            self.ChargeQuantity.setText(str(self.__data.FixHead.ChargeQuantity))
            self.MsgState.setCurrentIndex(self.__data.FixHead.MsgState-1)
            self.MsgType.setCurrentIndex(self.__data.FixHead.MsgType-1)
            self.CommitTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data.FixHead.CommitTime)))
            self.Package.setText(str(self.__data.FixHead.Package))
            self.MobilesContentLen.setText(str(self.__data.FixHead.MobilesContentLen))
            self.MsgContentLen.setText(str(self.__data.FixHead.MsgContentLen))
            self.MobilesCount.setText(str(self.__data.FixHead.MobilesCount))
            self.DispatchTimes.setText(str(self.__data.FixHead.DispatchTimes))
            self.Telcom.setCurrentIndex(self.__data.FixHead.Telcom)
            self.ProvinceId.setText(str(self.__data.FixHead.ProvinceId))
            self.CityId.setText(str(self.__data.FixHead.CityId))
            self.TPCBChecked.setText(str(self.__data.FixHead.TPCBChecked))
            self.SendedTimes.setText(str(self.__data.FixHead.SendedTimes))
            self.DispatchFailedState.setText(str(self.__data.FixHead.DispatchFailedState))
            self.SubmitType.setText(str(self.__data.FixHead.SubmitType))
            self.CloudMsgTemplateID.setText(str(self.__data.FixHead.CloudMsgTemplateID))
            self.CommitIp.setText(str(socket.inet_ntoa(int2ipbyte(self.__data.FixHead.CommitIp))))
            self.m_old_struct.setText(str(self.__data.FixHead.m_old_struct))

            #tail
            self.pagetotal.setText(str(self.__data.FixTail.pagetotal))
            self.packagetotal.setText(str(self.__data.FixTail.packagetotal))
            self.typeComponentParam.setText(str(self.__data.FixTail.typeComponentParam))
            self.lastFailResourceId.setText(str(self.__data.FixTail.lastFailResourceId))
            self.failedType.setCurrentIndex(self.failedType)
            self.lastDiapatchTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data.FixTail.lastDiapatchTime)))
            self.resourceSendTimes.setText(str(self.__data.FixTail.resourceSendTimes))
            self.auditorId.setText(str(self.__data.FixTail.auditorId))
            self.totalSendTimes.setText(str(self.__data.FixTail.totalSendTimes))
            self.repResendTimeOut.setText(str(self.__data.FixTail.repResendTimeOut))
            self.innerDispatchTimes.setText(str(self.__data.FixTail.innerDispatchTimes))
            self.extComponentParam.setText(str(self.__data.FixTail.extComponentParam))
            ##
            self.mobile.setText(self.__data.mobiles)
            self.acc_name.setText(self.__data.acc_name)
            self.message.setText(self.__data.message)
            self.templateID.setText(self.__data.templateID)
            self.msgtemplate.setText(self.__data.msgtemplate)
            self.extnumber.setText(self.__data.extnumer)
            self.sign.setText(self.__data.sign)
            self.acc_msgid.setText(self.__data.acc_msgid)
            self.mms_title.setText(self.__data.mms_title)
            self.mms_path.setText(self.__data.mms_filename)
            self.user_defid.setText(self.__data.usr_def_id)

        except:
            print('analyze error')
