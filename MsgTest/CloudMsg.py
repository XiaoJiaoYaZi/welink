from PyQt5 import QtWidgets,QtCore
import time
import socket
from configparser import ConfigParser
from PyUI.UI_SCloudMsg import Ui_CloudMsg
from PyUI.UI_SMsgSendData import Ui_SMsgSendData
from PyUI.UI_SMsgHisRepData import Ui_SMsgHisRepData
from PyUI.UI_SRepNotifyData_Cloud import Ui_SRepNotifyData
from PyUI.UI_Monitor_Cloud import Ui_Monitor_Cloud
from PyUI.UI_SMOData import Ui_SMOData
from PlatformPublicDefine import SCloudMessage,SMsgSendData,SMsgHisRepData,SMOData,SRepNotifyData,ResourceStateNotify,SDispatchStatistics,SResComStatistics,SResourceState
from BMSMessage import dt_Datetime,Datetime_dt,bytes2int,int2ipbyte
import os
import sys


m_section = ['SCloudMsg','MsgSendData','MsgHisRepData','MOData','RepNotifyData','ResourceStateNotify','SDispatchStatistics','SResComStatistics','SResourceState']

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
m_keys_msgsenddata = (
    '扩展产品',
    '信息编号',
    '发送时间',
    '提交时间',
    '手机号码',
    '匹配编号',
    '真实扩展产品编号',
    '计费数',
    '资源编号',
    '组合属性',
    '发送次数',
    '消息类型',
    '账号编号',
    '企业扩展码',
    '客户自定义id',
    '发送状态',
    '消息长度',
    '发送结果长度',
    '标题长度',
    '循环次数',
    '消息级别',
    '综合状态',
    '剩余重发次数',
    '回执超时时长',
    '用户定义id',
    '标题',
    '签名',
    '整包长度',
    '整包内容',
    '发送结果内容',
    '短信内容'
)
m_keys_msghisrepdata = (
    '手机号码',
    '匹配编号',
    '资源编号',
    '消息回执时间',
    '状态报告是否成功',
    '状态报告本地接收时间',
    'Flag',
    '循环次数',
    '状态报告信息',
)
m_keys_modata = (
    '信息编号',
    '手机号码',
    '上行时间',
    '企业扩展号',
    '资源编号',
    '上行消息长度',
    '信息类型',
    '账户id',
    '上行内容',
)
m_keys_repnotifydata = (
    '版本',
    '消息编号',
    '账户id',
    '电话号码',
    '发送状态',
    '报告状态',
    '发送时间',
    '报告时间',
    '企业扩展号',
    '客户自定义消息id',
    '扩展号码',
    '消息回执本地时间',
    '总包数',
    '当前包号',
    '扩展参数',
    '客户自定义id',
    '发送结果',
    '报告结果',
    'extMem',
)
m_keys_resoucestatenotify = (
    '资源id',
    '报告时间',
    '资源状态',
    '队列积压数',
    '最后时间积压数',
    '报告频率',
    '提交总数',
    '提交失败',
    '报告总数',
    '报告失败',
)
m_keys_sdispatchstatistics = (
    '调度id',
    '总调度数',
    '调度成功',
    '调度失败',
    '循环次数',
)
m_keys_srescomstatistics = (
    '资源id',
    '成功数',
    '失败数',
    '循环次数',
)
m_keys_resourcestate = (
    '资源ID',
'报告时间',
'配置值',
'积压数量',
'上次库存值',
'报告时间间隔',
'下行总数',
'当前下行成功数',
'当前下行失败数',
'状态报告总数',
'当前状态报告成功数',
'当前状态报告失败数',
'上行总数',
'当前上行数',
'状态',
)


class MsgBase(QtWidgets.QWidget):
    def __init__(self):
        super(MsgBase,self).__init__()

    def getValue(self):
        pass
    def analyze(self,b):
        pass
    def updatedata(self):
        pass
    def saveConfig(self, filename):
        pass
    def loadConfig(self, filename):
        pass

class CloudMsg(QtWidgets.QWidget,Ui_CloudMsg):
    def __init__(self):
        super(CloudMsg,self).__init__()
        self.setupUi(self)
        self.__data = SCloudMessage()
        self.mobile.textChanged.connect(self.motile_textChanged)
        self.message.textChanged.connect(self.message_textChanged)

    def message_textChanged(self):
        data = self.message.toPlainText()
        if os.path.isfile(data):
            self.MsgContentLen.setText(str(os.path.getsize(data)))
            self.MsgType.setCurrentIndex(1)
            return
        self.MsgContentLen.setText(str(len(data.encode(encoding='utf_16_le')+b'\x00\x00')))

    def motile_textChanged(self):
        data = self.mobile.toPlainText()
        self.MobilesContentLen.setText(str(len(bytes(data,'utf-8')+b'\x00')))
        self.MobilesCount.setText(str(int((len(data)+1)/12)))

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
            self.__data.FixTail.m_old_struct = int(self.m_old_struct.text())
            ##
            self.__data.mobiles = self.mobile.toPlainText()
            self.__data.acc_name = self.acc_name.text()
            if self.__data.FixHead.MsgType == 2:
                filename = self.message.toPlainText()
                if os.path.isfile(filename):
                    f = open(filename,'rb')
                    data = f.read(os.path.getsize(filename))
                    self.__data.message = data
                else:
                    raise Exception('请输入正确的彩信路径')
            else:
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
        except Exception as e:
            print(e)
            print('getValue error')

    def updatedata(self):
        self.__data.FixHead.MsgId +=1
        return self.__data.Value()

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

            with open('config/'+filename+'.ini','w',encoding='gbk') as f:
                config.write(f)
        except Exception as e:
            print(e)
            print('保存配置失败')

    def loadConfig(self,filename):
        try:
            config = ConfigParser()
            config.read(filename,encoding='gbk')
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
        except Exception as e:
            print(e)
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


            #tail
            self.pagetotal.setText(str(self.__data.FixTail.pagetotal))
            self.packagetotal.setText(str(self.__data.FixTail.packagetotal))
            self.typeComponentParam.setText(str(self.__data.FixTail.typeComponentParam))
            self.lastFailResourceId.setText(str(self.__data.FixTail.lastFailResourceId))
            self.failedType.setCurrentIndex(self.__data.FixTail.failedType)
            self.lastDiapatchTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data.FixTail.lastDiapatchTime)))
            self.resourceSendTimes.setText(str(self.__data.FixTail.resourceSendTimes))
            self.auditorId.setText(str(self.__data.FixTail.auditorId))
            self.totalSendTimes.setText(str(self.__data.FixTail.totalSendTimes))
            self.repResendTimeOut.setText(str(self.__data.FixTail.repResendTimeOut))
            self.innerDispatchTimes.setText(str(self.__data.FixTail.innerDispatchTimes))
            self.extComponentParam.setText(str(self.__data.FixTail.extComponentParam))
            self.m_old_struct.setText(str(self.__data.FixTail.m_old_struct))
            ##
            self.mobile.setText(self.__data.mobiles)
            self.acc_name.setText(self.__data.acc_name)
            self.message.setText(self.__data.message)
            self.templateID.setText(self.__data.templateID)
            self.msgtemplate.setText(self.__data.msgtemplate)
            self.paramtemplate.setText(self.__data.paramtemplate)
            self.extnumber.setText(self.__data.extnumer)
            self.sign.setText(self.__data.sign)
            self.acc_msgid.setText(self.__data.acc_msgid)
            self.mms_title.setText(self.__data.mms_title)
            self.mms_path.setText(self.__data.mms_filename)
            self.user_defid.setText(self.__data.usr_def_id)

        except Exception as e:
            print(e)
            print('analyze error')

class MsgSendData(QtWidgets.QWidget,Ui_SMsgSendData):

    def __init__(self):
        super(MsgSendData,self).__init__()
        self.setupUi(self)
        self.__data = SMsgSendData()
        self.textEdit_sendResultInfo.textChanged.connect(self.textEdit_sendResultInfo_textChanged)
        self.textEdit_msgContent.textChanged.connect(self.textEdit_msgContent_textChanged)
        self.lineEdit_title.textChanged.connect(self.lineEdit_title_textChanged)
        self.textEdit_totalMsg.textChanged.connect(self.textEdit_totalMsg_textChanged)

    def textEdit_sendResultInfo_textChanged(self):
        data = self.textEdit_sendResultInfo.toPlainText()
        self.lineEdit_SendResultLen.setText(str(len(bytes(data,'gbk')+b'\x00')))

    def textEdit_msgContent_textChanged(self):
        data = self.textEdit_msgContent.toPlainText()
        self.lineEdit_msgLen.setText(str(len(bytes(data,'utf_16_le')+b'\x00\x00')))

    def lineEdit_title_textChanged(self):
        data = self.lineEdit_title.text()
        self.lineEdit_TitleLen.setText(str(len(bytes(data,'utf_16_le')+b'\x00\x00')))

    def textEdit_totalMsg_textChanged(self):
        data = self.textEdit_totalMsg.toPlainText()
        self.lineEdit_totalMsgLen.setText(str(len(bytes(data,'utf_16_le')+b'\x00\x00')))

    def getValue(self):
        try:
            self.__data._body.productExtendId       = int(self.lineEdit_productExtendId.text())
            self.__data._body.msgId                 = int(self.lineEdit_msgId.text())
            self.__data._body.sendedTime            = dt_Datetime(self.dateTimeEdit_sendedTime.dateTime().toPyDateTime().ctime())
            self.__data._body.submitTime            = dt_Datetime(self.dateTimeEdit_submitTime.dateTime().toPyDateTime().ctime())
            self.__data._body.mobilePhone           = int(self.lineEdit_mobilePhone.text())
            self.__data._body.matchId               = int(self.lineEdit_matchId.text())
            self.__data._body.realProductExtendId   = int(self.lineEdit_realProductExtendId.text())
            self.__data._body.resourceId            = int(self.lineEdit_resourceId.text())
            self.__data._body.chargeQuantity        = int(self.lineEdit_chargeQuantity.text())
            self.__data._body.propertyComponent     = int(self.lineEdit_propertyComponent.text())
            self.__data._body.sendTimes             = int(self.lineEdit_sendTimes.text())
            self.__data._body.msgType               = int(self.lineEdit_msgType.text())
            self.__data._body.accountId             = self.lineEdit_accountId.text()
            self.__data._body.SPNo                  = self.lineEdit_SPNo.text()
            self.__data._body.clientMsgId           = self.lineEdit_clientMsgId.text()
            self.__data._body.sendState             = int(self.lineEdit_sendState.text())
            self.__data._body.msgLen                = int(self.lineEdit_msgLen.text())
            self.__data._body.SendResultLen         = int(self.lineEdit_SendResultLen.text())
            self.__data._body.TitleLen              = int(self.lineEdit_TitleLen.text())
            self.__data._body.cycletimes            = int(self.lineEdit_cycletimes.text())
            self.__data._body.Priority              = int(self.lineEdit_Priority.text())
            self.__data._body.typeComponentParam    = int(self.lineEdit_typeComponentParam.text())
            self.__data._body.rmReSendTimes         = int(self.lineEdit_rmReSendTimes.text())
            self.__data._body.repResendTimeOut      = int(self.lineEdit_repResendTimeOut.text())

            self.__data.userDefineId        = self.lineEdit_userDefineId.text()
            self.__data.title               = self.lineEdit_title.text()
            self.__data.sign                = self.lineEdit_sign.text()
            self.__data.totalMsgLen         = int(self.lineEdit_totalMsgLen.text())
            self.__data.msgContent          = self.textEdit_msgContent.toPlainText()
            self.__data.sendResultInfo      = self.textEdit_sendResultInfo.toPlainText()
            self.__data.totalMsg            = self.textEdit_totalMsg.toPlainText()

            self.__data.write_header()
            return self.__data.Value()
        except Exception as e:
            print(e)
            raise Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))

    def analyze(self,b):
        try:
            self.__data.fromBytes(b)
            self.__analyze()
        except Exception as e:
            print(e)

    def __analyze(self):
        try:
            self.lineEdit_productExtendId.setText(str(self.__data._body.productExtendId ))
            self.lineEdit_msgId.setText(str(self.__data._body.msgId))
            self.dateTimeEdit_sendedTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data._body.sendedTime)))
            self.dateTimeEdit_submitTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data._body.submitTime)))
            self.lineEdit_mobilePhone.setText(str(self.__data._body.mobilePhone))
            self.lineEdit_matchId.setText(str(self.__data._body.matchId))
            self.lineEdit_realProductExtendId.setText(str(self.__data._body.realProductExtendId))
            self.lineEdit_resourceId.setText(str(self.__data._body.resourceId))
            self.lineEdit_chargeQuantity.setText(str(self.__data._body.chargeQuantity))
            self.lineEdit_propertyComponent.setText(str(self.__data._body.propertyComponent))
            self.lineEdit_sendTimes.setText(str(self.__data._body.sendTimes))
            self.lineEdit_msgType.setText(str(self.__data._body.msgType))
            self.lineEdit_accountId.setText(self.__data._body.accountId)
            self.lineEdit_SPNo.setText(self.__data._body.SPNo)
            self.lineEdit_clientMsgId.setText(self.__data._body.clientMsgId)
            self.lineEdit_sendState.setText(str(self.__data._body.sendState))
            self.lineEdit_msgLen.setText(str(self.__data._body.msgLen))
            self.lineEdit_SendResultLen.setText(str(self.__data._body.SendResultLen))
            self.lineEdit_TitleLen.setText(str(self.__data._body.TitleLen))
            self.lineEdit_cycletimes.setText(str(self.__data._body.cycletimes))
            self.lineEdit_Priority.setText(str(self.__data._body.Priority))
            self.lineEdit_typeComponentParam.setText(str(self.__data._body.typeComponentParam))
            self.lineEdit_rmReSendTimes.setText(str(self.__data._body.rmReSendTimes))
            self.lineEdit_repResendTimeOut.setText(str(self.__data._body.repResendTimeOut))

            self.lineEdit_userDefineId.setText(self.__data.userDefineId)
            self.lineEdit_title.setText(self.__data.title)
            self.lineEdit_sign.setText(self.__data.sign)
            self.lineEdit_totalMsgLen.setText(str(self.__data.totalMsgLen))
            self.textEdit_msgContent.setText(self.__data.msgContent)
            self.textEdit_sendResultInfo.setText(self.__data.sendResultInfo)
            self.textEdit_totalMsg.setText(self.__data.totalMsg)
        except Exception as e:
            print(e)
            raise Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))

    def updatedata(self):
        self.__data._body.msgId +=1
        return self.__data.Value()

    def saveConfig(self, filename):
        try:
            config = ConfigParser()
            config.add_section(m_section[1])

            config.set(m_section[1], m_keys_msgsenddata[0],self.lineEdit_productExtendId.text())
            config.set(m_section[1], m_keys_msgsenddata[1],self.lineEdit_msgId.text())
            config.set(m_section[1], m_keys_msgsenddata[2],self.dateTimeEdit_sendedTime.dateTime().toString())
            config.set(m_section[1], m_keys_msgsenddata[3],self.dateTimeEdit_submitTime.dateTime().toString())
            config.set(m_section[1], m_keys_msgsenddata[4],self.lineEdit_mobilePhone.text())
            config.set(m_section[1], m_keys_msgsenddata[5],self.lineEdit_matchId.text())
            config.set(m_section[1], m_keys_msgsenddata[6],self.lineEdit_realProductExtendId.text())
            config.set(m_section[1], m_keys_msgsenddata[7],self.lineEdit_chargeQuantity.text())
            config.set(m_section[1], m_keys_msgsenddata[8],self.lineEdit_resourceId.text())
            config.set(m_section[1], m_keys_msgsenddata[9],self.lineEdit_propertyComponent.text())
            config.set(m_section[1], m_keys_msgsenddata[10],self.lineEdit_sendTimes.text())
            config.set(m_section[1], m_keys_msgsenddata[11],self.lineEdit_msgType.text())
            config.set(m_section[1], m_keys_msgsenddata[12],self.lineEdit_accountId.text())
            config.set(m_section[1], m_keys_msgsenddata[13],self.lineEdit_SPNo.text())
            config.set(m_section[1], m_keys_msgsenddata[14],self.lineEdit_clientMsgId.text())
            config.set(m_section[1], m_keys_msgsenddata[15],self.lineEdit_sendState.text())
            config.set(m_section[1], m_keys_msgsenddata[16],self.lineEdit_msgLen.text())
            config.set(m_section[1], m_keys_msgsenddata[17],self.lineEdit_SendResultLen.text())
            config.set(m_section[1], m_keys_msgsenddata[18],self.lineEdit_TitleLen.text())
            config.set(m_section[1], m_keys_msgsenddata[19],self.lineEdit_cycletimes.text())
            config.set(m_section[1], m_keys_msgsenddata[20],self.lineEdit_Priority.text())
            config.set(m_section[1], m_keys_msgsenddata[21],self.lineEdit_typeComponentParam.text())
            config.set(m_section[1], m_keys_msgsenddata[22],self.lineEdit_rmReSendTimes.text())
            config.set(m_section[1], m_keys_msgsenddata[23],self.lineEdit_repResendTimeOut.text())
            config.set(m_section[1], m_keys_msgsenddata[24],self.lineEdit_userDefineId.text())
            config.set(m_section[1], m_keys_msgsenddata[25],self.lineEdit_title.text())
            config.set(m_section[1], m_keys_msgsenddata[26],self.lineEdit_sign.text())
            config.set(m_section[1], m_keys_msgsenddata[27],self.lineEdit_totalMsgLen.text())
            config.set(m_section[1], m_keys_msgsenddata[28],self.textEdit_totalMsg.toPlainText())
            config.set(m_section[1], m_keys_msgsenddata[29],self.textEdit_sendResultInfo.toPlainText())
            config.set(m_section[1], m_keys_msgsenddata[30],self.textEdit_msgContent.toPlainText())

            with open('config/'+filename+'.ini','w',encoding='gbk') as f:
                config.write(f)
        except Exception as e:
            print(e)
            print('保存配置失败')

    def loadConfig(self,filename):
        try:
            config = ConfigParser()
            config.read(filename,encoding='gbk')
            if not config.has_section(m_section[1]):
                print(filename,'do not have section',m_section[1])
                return False
            if len(config.items(m_section[1])) != len(m_keys_msgsenddata):
                print(filename,'items error\n allkeys:\n',m_keys_msgsenddata)
                return False

            self.lineEdit_productExtendId.setText(config[m_section[1]][m_keys_msgsenddata[0]])
            self.lineEdit_msgId.setText(config[m_section[1]][m_keys_msgsenddata[1]])
            self.dateTimeEdit_sendedTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[1]][m_keys_msgsenddata[2]]))
            self.dateTimeEdit_submitTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[1]][m_keys_msgsenddata[3]]))
            self.lineEdit_mobilePhone.setText(config[m_section[1]][m_keys_msgsenddata[4]])
            self.lineEdit_matchId.setText(config[m_section[1]][m_keys_msgsenddata[5]])
            self.lineEdit_realProductExtendId.setText(config[m_section[1]][m_keys_msgsenddata[6]])
            self.lineEdit_chargeQuantity.setText(config[m_section[1]][m_keys_msgsenddata[7]])
            self.lineEdit_resourceId.setText(config[m_section[1]][m_keys_msgsenddata[8]])
            self.lineEdit_propertyComponent.setText(config[m_section[1]][m_keys_msgsenddata[9]])
            self.lineEdit_sendTimes.setText(config[m_section[1]][m_keys_msgsenddata[10]])
            self.lineEdit_msgType.setText(config[m_section[1]][m_keys_msgsenddata[11]])
            self.lineEdit_accountId.setText(config[m_section[1]][m_keys_msgsenddata[12]])
            self.lineEdit_SPNo.setText(config[m_section[1]][m_keys_msgsenddata[13]])
            self.lineEdit_clientMsgId.setText(config[m_section[1]][m_keys_msgsenddata[14]])
            self.lineEdit_sendState.setText(config[m_section[1]][m_keys_msgsenddata[15]])
            self.lineEdit_msgLen.setText(config[m_section[1]][m_keys_msgsenddata[16]])
            self.lineEdit_SendResultLen.setText(config[m_section[1]][m_keys_msgsenddata[17]])
            self.lineEdit_TitleLen.setText(config[m_section[1]][m_keys_msgsenddata[18]])
            self.lineEdit_cycletimes.setText(config[m_section[1]][m_keys_msgsenddata[19]])
            self.lineEdit_Priority.setText(config[m_section[1]][m_keys_msgsenddata[20]])
            self.lineEdit_typeComponentParam.setText(config[m_section[1]][m_keys_msgsenddata[21]])
            self.lineEdit_rmReSendTimes.setText(config[m_section[1]][m_keys_msgsenddata[22]])
            self.lineEdit_repResendTimeOut.setText(config[m_section[1]][m_keys_msgsenddata[23]])
            self.lineEdit_userDefineId.setText(config[m_section[1]][m_keys_msgsenddata[24]])
            self.lineEdit_title.setText(config[m_section[1]][m_keys_msgsenddata[25]])
            self.lineEdit_sign.setText(config[m_section[1]][m_keys_msgsenddata[26]])
            self.lineEdit_totalMsgLen.setText(config[m_section[1]][m_keys_msgsenddata[27]])
            self.textEdit_totalMsg.setText(config[m_section[1]][m_keys_msgsenddata[28]])
            self.textEdit_sendResultInfo.setText(config[m_section[1]][m_keys_msgsenddata[29]])
            self.textEdit_msgContent.setText(config[m_section[1]][m_keys_msgsenddata[30]])

        except Exception as e:
            print(e)
            print('加载配置失败')

class MsgHisRepData(QtWidgets.QWidget,Ui_SMsgHisRepData):

    def __init__(self):
        super(MsgHisRepData,self).__init__()
        self.setupUi(self)
        self.__data = SMsgHisRepData()

    def getValue(self):
        try:
            self.__data._body.mobilePhone         = int(self.lineEdit_mobilePhone.text())
            self.__data._body.matchId             = int(self.lineEdit_matchId.text())
            self.__data._body.resourceId          = int(self.lineEdit_resourceId.text())
            self.__data._body.reportTime          = self.dateTimeEdit_reportTime.dateTime()
            self.__data._body.reportState         = int(self.lineEdit_reportState.text())
            self.__data._body.reportResultInfo    = self.textEdit.toPlainText()
            self.__data._body.reportLocalTime     = self.dateTimeEdit_reportLocalTime.dateTime()
            self.__data._body.componentFlg        = int(self.lineEdit_componentFlg.text())
            self.__data._body.flagRetryTime       = int(time.time())
            self.__data._body.cycletimes          = int(self.lineEdit_cycletimes.text())
            self.__data.write_header()
            return self.__data.Value()
        except Exception as e:
            print(e)
            raise Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))

    def analyze(self,b):
        try:
            self.__data.fromBytes(b)
            self.__analyze()
        except Exception as e:
            print(e)

    def __analyze(self):
        try:
            self.lineEdit_mobilePhone.setText(str(self.__data._body.mobilePhone))
            self.lineEdit_matchId.setText(str(self.__data._body.matchId))
            self.lineEdit_resourceId.setText(str(self.__data._body.resourceId))
            self.dateTimeEdit_reportTime.setDateTime(self.__data._body.reportTime)
            self.lineEdit_reportState.setText(str(self.__data._body.reportState))
            self.textEdit.setText(self.__data._body.reportResultInfo)
            self.dateTimeEdit_reportLocalTime.setDateTime(self.__data._body.reportLocalTime)
            self.lineEdit_componentFlg.setText(str(self.__data._body.componentFlg))
            self.lineEdit_cycletimes.setText(str(self.__data._body.cycletimes))
        except Exception as e:
            print(e)
            raise Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))

    def updatedata(self):
        self.__data._body.flagRetryTime = int(time.time())
        return self.__data.Value()

    def saveConfig(self, filename):
        try:
            config = ConfigParser()
            config.add_section(m_section[2])

            config.set(m_section[2], m_keys_msghisrepdata[0],self.lineEdit_mobilePhone.text())
            config.set(m_section[2], m_keys_msghisrepdata[1],self.lineEdit_matchId.text())
            config.set(m_section[2], m_keys_msghisrepdata[2],self.lineEdit_resourceId.text())
            config.set(m_section[2], m_keys_msghisrepdata[3],self.dateTimeEdit_reportTime.dateTime().toString())
            config.set(m_section[2], m_keys_msghisrepdata[4],self.lineEdit_reportState.text())
            config.set(m_section[2], m_keys_msghisrepdata[5],self.dateTimeEdit_reportLocalTime.dateTime().toString())
            config.set(m_section[2], m_keys_msghisrepdata[6],self.lineEdit_componentFlg.text())
            config.set(m_section[2], m_keys_msghisrepdata[7],self.lineEdit_cycletimes.text())
            config.set(m_section[2], m_keys_msghisrepdata[8],self.textEdit.toPlainText())
            with open('config/'+filename+'.ini','w',encoding='gbk') as f:
                config.write(f)
        except Exception as e:
            print(e)
            print('保存配置失败')

    def loadConfig(self,filename):
        try:
            config = ConfigParser()
            config.read(filename,encoding='gbk')
            if not config.has_section(m_section[2]):
                print(filename,'do not have section',m_section[2])
                return False
            if len(config.items(m_section[2])) != len(m_keys_msghisrepdata):
                print(filename,'items error\n allkeys:\n',m_keys_msghisrepdata)
                return False

            self.lineEdit_mobilePhone.setText(config[m_section[2]][m_keys_msghisrepdata[0]])
            self.lineEdit_matchId.setText(config[m_section[2]][m_keys_msghisrepdata[1]])
            self.lineEdit_resourceId.setText(config[m_section[2]][m_keys_msghisrepdata[2]])
            self.dateTimeEdit_reportTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[2]][m_keys_msghisrepdata[3]]))
            self.lineEdit_reportState.setText(config[m_section[2]][m_keys_msghisrepdata[4]])
            self.dateTimeEdit_reportLocalTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[2]][m_keys_msghisrepdata[5]]))
            self.lineEdit_componentFlg.setText(config[m_section[2]][m_keys_msghisrepdata[6]])
            self.lineEdit_cycletimes.setText(config[m_section[2]][m_keys_msghisrepdata[7]])
            self.textEdit.setText(config[m_section[2]][m_keys_msghisrepdata[8]])
        except Exception as e:
            print(e)
            print('加载配置失败')

class MOData(QtWidgets.QWidget,Ui_SMOData):

    def __init__(self):
        super(MOData,self).__init__()
        self.setupUi(self)
        self.__data = SMOData()

    def getValue(self):
        try:
            self.__data.msgId           = int(self.lineEdit_msgId.text())
            self.__data.mobilePhone     = int(self.lineEdit_mobilePhone.text())
            self.__data.SPNo            = self.lineEdit_SPNo.text()
            self.__data.MOTime          = self.dateTimeEdit_MOTime.dateTime()
            self.__data.resourceId      = int(self.lineEdit_resourceId.text())
            self.__data.MOContentLength = int(self.lineEdit_MOContentLength.text())
            self.__data.MOContent       = self.textEdit_MOContent.toPlainText()
            self.__data.msgType         = int(self.lineEdit_msgType.text())
            self.__data.accountId       = self.lineEdit_accountId.text()
            return self.__data.Value()
        except Exception as e:
            print(e)
            raise Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))

    def analyze(self,b):
        try:
            self.__data.fromBytes(b)
            self.__analyze()
        except Exception as e:
            print(e)

    def __analyze(self):
        try:
            self.lineEdit_msgId.setText(str(self.__data.msgId))
            self.lineEdit_mobilePhone.setText(str(self.__data.mobilePhone))
            self.lineEdit_SPNo.setText(self.__data.SPNo)
            self.dateTimeEdit_MOTime.setDateTime(self.__data.MOTime)
            self.lineEdit_resourceId.setText(str(self.__data.resourceId))
            self.lineEdit_MOContentLength.setText(str(self.__data.MOContentLength))
            self.textEdit_MOContent.setText(self.__data.MOContent)
            self.lineEdit_msgType.setText(str(self.__data.msgType))
            self.lineEdit_accountId.setText(self.__data.accountId)
        except Exception as e:
            print(e)
            raise Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))

    def updatedata(self):
        self.__data.msgId += 1
        return self.__data.Value()

    def saveConfig(self, filename):
        try:
            config = ConfigParser()
            config.add_section(m_section[3])

            config.set(m_section[3], m_keys_modata[0],self.lineEdit_msgId.text())
            config.set(m_section[3], m_keys_modata[1],self.lineEdit_mobilePhone.text())
            config.set(m_section[3], m_keys_modata[2],self.dateTimeEdit_MOTime.dateTime().toString())
            config.set(m_section[3], m_keys_modata[3],self.lineEdit_SPNo.text())
            config.set(m_section[3], m_keys_modata[4],self.lineEdit_resourceId.text())
            config.set(m_section[3], m_keys_modata[5],self.lineEdit_MOContentLength.text())
            config.set(m_section[3], m_keys_modata[6],self.lineEdit_msgType.text())
            config.set(m_section[3], m_keys_modata[7],self.lineEdit_accountId.text())
            config.set(m_section[3], m_keys_modata[8],self.textEdit_MOContent.toPlainText())
            
            with open('config/'+filename+'.ini','w',encoding='gbk') as f:
                config.write(f)
        except Exception as e:
            print(e)
            print('保存配置失败')

    def loadConfig(self,filename):
        try:
            config = ConfigParser()
            config.read(filename,encoding='gbk')
            if not config.has_section(m_section[3]):
                print(filename,'do not have section',m_section[3])
                return False
            if len(config.items(m_section[3])) != len(m_keys_modata):
                print(filename,'items error\n allkeys:\n',m_keys_modata)
                return False

            self.lineEdit_msgId.setText(config[m_section[3]][m_keys_modata[0]])
            self.lineEdit_mobilePhone.setText(config[m_section[3]][m_keys_modata[1]])
            self.dateTimeEdit_MOTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[3]][m_keys_modata[2]]))
            self.lineEdit_SPNo.setText(config[m_section[3]][m_keys_modata[3]])
            self.lineEdit_resourceId.setText(config[m_section[3]][m_keys_modata[4]])
            self.lineEdit_MOContentLength.setText(config[m_section[3]][m_keys_modata[5]])
            self.lineEdit_msgType.setText(config[m_section[3]][m_keys_modata[6]])
            self.lineEdit_accountId.setText(config[m_section[3]][m_keys_modata[7]])
            self.textEdit_MOContent.setText(config[m_section[3]][m_keys_modata[8]])

        except Exception as e:
            print(e)
            print('加载配置失败')

class RepNotifyData(QtWidgets.QWidget,Ui_SRepNotifyData):

    def __init__(self):
        super(RepNotifyData,self).__init__()
        self.setupUi(self)
        self.__data = SRepNotifyData()

    def getValue(self):
        try:
            self.__data.version         = int(self.lineEdit_version.text())
            self.__data.msgId           = int(self.lineEdit_msgId.text())
            self.__data.accountId      = self.lineEdit_accountId.text()
            self.__data.mobilePhone     = int(self.lineEdit_mobilePhone.text())
            self.__data.sendState       = int(self.lineEdit_sendState.text())
            self.__data.reportState     = int(self.lineEdit_reportState.text())
            self.__data.sendedTime      = self.dateTimeEdit_sendedTime.dateTime()
            self.__data.reportTime      = self.dateTimeEdit_reportTime.dateTime()
            self.__data.sendResultInfo  = self.textEdit_sendResultInfo.toPlainText()
            self.__data.reportResultInfo= self.textEdit_reportResultInfo.toPlainText()
            self.__data.spno            = self.lineEdit_spno.text()
            self.__data.clientMsgId     = self.lineEdit_clientMsgId.text()
            self.__data.reportLocalTime = self.dateTimeEdit_reportLocalTime.dateTime()
            self.__data.extendNum       = self.lineEdit_extendNum.text()
            self.__data.pk_total        = int(self.lineEdit_pk_total.text())
            self.__data.pk_num          = int(self.lineEdit_pk_num.text())
            self.__data.combinationVal  = int(self.lineEdit_combinationVal.text())
            self.__data.userDefineId    = self.lineEdit_userDefineId.text()
            self.__data.extMem          = self.textEdit_extMem.toPlainText()
            return self.__data.Value()
        except Exception as e:
            print(e)
            raise Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))

    def analyze(self,b):
        try:
            self.__data.fromBytes(b)
            self.__analyze()
        except Exception as e:
            print(e)

    def __analyze(self):
        try:
            self.lineEdit_version.setText(str(self.__data.version))
            self.lineEdit_msgId.setText(str(self.__data.msgId))
            self.lineEdit_accountId.setText(self.__data.accountId)
            self.lineEdit_mobilePhone.setText(str(self.__data.mobilePhone))
            self.lineEdit_sendState.setText(str(self.__data.sendState))
            self.lineEdit_reportState.setText(str(self.__data.reportState))
            self.dateTimeEdit_sendedTime.setDateTime(self.__data.sendedTime)
            self.dateTimeEdit_reportTime.setDateTime(self.__data.reportTime)
            self.textEdit_sendResultInfo.setText(self.__data.sendResultInfo)
            self.textEdit_reportResultInfo.setText(self.__data.reportResultInfo)
            self.lineEdit_spno.setText(self.__data.spno)
            self.lineEdit_clientMsgId.setText(self.__data.clientMsgId)
            self.dateTimeEdit_reportLocalTime.setDateTime(self.__data.reportLocalTime)
            self.lineEdit_extendNum.setText(self.__data.extendNum)
            self.lineEdit_pk_total.setText(str(self.__data.pk_total))
            self.lineEdit_pk_num.setText(str(self.__data.pk_num))
            self.lineEdit_combinationVal.setText(str(self.__data.combinationVal))
            self.lineEdit_userDefineId.setText(str(self.__data.combinationVal))
            self.textEdit_extMem.setText(str(self.__data.extMem))
        except Exception as e:
            print(e)
            raise Exception("module:{} func:{} line:{} error".format(
                __file__, sys._getframe().f_code.co_name, sys._getframe().f_lineno))

    def updatedata(self):
        self.__data.msgId += 1
        return self.__data.Value()

    def saveConfig(self, filename):
        try:
            config = ConfigParser()
            config.add_section(m_section[4])

            config.set(m_section[4], m_keys_repnotifydata[0],self.lineEdit_version.text())
            config.set(m_section[4], m_keys_repnotifydata[1],self.lineEdit_msgId.text())
            config.set(m_section[4], m_keys_repnotifydata[2],self.lineEdit_accountId.text())
            config.set(m_section[4], m_keys_repnotifydata[3],self.lineEdit_mobilePhone.text())
            config.set(m_section[4], m_keys_repnotifydata[4],self.lineEdit_sendState.text())
            config.set(m_section[4], m_keys_repnotifydata[5],self.lineEdit_reportState.text())
            config.set(m_section[4], m_keys_repnotifydata[6],self.dateTimeEdit_sendedTime.dateTime().toString())
            config.set(m_section[4], m_keys_repnotifydata[7],self.dateTimeEdit_reportTime.dateTime().toString())
            config.set(m_section[4], m_keys_repnotifydata[8],self.lineEdit_spno.text())
            config.set(m_section[4], m_keys_repnotifydata[9],self.lineEdit_clientMsgId.text())
            config.set(m_section[4], m_keys_repnotifydata[10],self.lineEdit_extendNum.text())
            config.set(m_section[4], m_keys_repnotifydata[11],self.dateTimeEdit_reportLocalTime.dateTime().toString())
            config.set(m_section[4], m_keys_repnotifydata[12],self.lineEdit_pk_total.text())
            config.set(m_section[4], m_keys_repnotifydata[13],self.lineEdit_pk_num.text())
            config.set(m_section[4], m_keys_repnotifydata[14],self.lineEdit_combinationVal.text())
            config.set(m_section[4], m_keys_repnotifydata[15],self.lineEdit_userDefineId.text())
            config.set(m_section[4], m_keys_repnotifydata[16],self.textEdit_sendResultInfo.toPlainText())
            config.set(m_section[4], m_keys_repnotifydata[17],self.textEdit_reportResultInfo.toPlainText())
            config.set(m_section[4], m_keys_repnotifydata[18],self.textEdit_extMem.toPlainText())
            
            with open('config/'+filename+'.ini','w',encoding='gbk') as f:
                config.write(f)
        except Exception as e:
            print(e)
            print('保存配置失败')

    def loadConfig(self,filename):
        try:
            config = ConfigParser()
            config.read(filename,encoding='gbk')
            if not config.has_section(m_section[4]):
                print(filename,'do not have section',m_section[4])
                return False
            if len(config.items(m_section[4])) != len(m_keys_repnotifydata):
                print(filename,'items error\n allkeys:\n',m_keys_repnotifydata)
                return False

            self.lineEdit_version.setText(config[m_section[4]][m_keys_repnotifydata[0]])
            self.lineEdit_msgId.setText(config[m_section[4]][m_keys_repnotifydata[1]])
            self.lineEdit_accountId.setText(config[m_section[4]][m_keys_repnotifydata[2]])
            self.lineEdit_mobilePhone.setText(config[m_section[4]][m_keys_repnotifydata[3]])
            self.lineEdit_sendState.setText(config[m_section[4]][m_keys_repnotifydata[4]])
            self.lineEdit_reportState.setText(config[m_section[4]][m_keys_repnotifydata[5]])
            self.dateTimeEdit_sendedTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[4]][m_keys_repnotifydata[6]]))
            self.dateTimeEdit_reportTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[4]][m_keys_repnotifydata[7]]))
            self.lineEdit_spno.setText(config[m_section[4]][m_keys_repnotifydata[8]])
            self.lineEdit_clientMsgId.setText(config[m_section[4]][m_keys_repnotifydata[9]])
            self.lineEdit_extendNum.setText(config[m_section[4]][m_keys_repnotifydata[10]])
            self.dateTimeEdit_reportLocalTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[4]][m_keys_repnotifydata[11]]))
            self.lineEdit_pk_total.setText(config[m_section[4]][m_keys_repnotifydata[12]])
            self.lineEdit_pk_num.setText(config[m_section[4]][m_keys_repnotifydata[13]])
            self.lineEdit_combinationVal.setText(config[m_section[4]][m_keys_repnotifydata[14]])
            self.lineEdit_userDefineId.setText(config[m_section[4]][m_keys_repnotifydata[15]])
            self.textEdit_sendResultInfo.setText(config[m_section[4]][m_keys_repnotifydata[16]])
            self.textEdit_reportResultInfo.setText(config[m_section[4]][m_keys_repnotifydata[17]])
            self.textEdit_extMem.setText(config[m_section[4]][m_keys_repnotifydata[18]])

        except Exception as e:
            print(e)
            print('加载配置失败')

class Monitor_Cloud(QtWidgets.QWidget,Ui_Monitor_Cloud):

    def __init__(self):
        super(Monitor_Cloud,self).__init__()
        self.setupUi(self)
        self._init()
        self._initUi()

    def _init(self):
        self.__data = {}
        self.__data['ResourceStateNotify'] = ResourceStateNotify()
        self.__data['SDispatchStatistics'] = SDispatchStatistics()
        self.__data['SResComStatistics'] = SResComStatistics()
        self.__data['SResourceState'] = SResourceState()

        self.__func = {}
        self.__func['ResourceStateNotify'] = self._getValue_0
        self.__func['SDispatchStatistics'] = self._getValue_1
        self.__func['SResComStatistics'] = self._getValue_2
        self.__func['SResourceState'] = self._getValue_3

        self.__func_analy = {}
        self.__func_analy['ResourceStateNotify'] = self._analyze_0
        self.__func_analy['SDispatchStatistics'] = self._analyze_1
        self.__func_analy['SResComStatistics'] = self._analyze_2
        self.__func_analy['SResourceState'] = self._analyze_3

    def _initUi(self):
        self.checkBox.click()
        pass

    def on_checkBox_stateChanged(self,a0):
        if a0 == QtCore.Qt.Checked:
            self.groupBox.setEnabled(bool(a0))
            self.groupBox_2.setEnabled(not bool(a0))
            self.groupBox_3.setEnabled(not bool(a0))
            self.groupBox_4.setEnabled(not bool(a0))
            self.checkBox_2.setChecked(not bool(a0))
            self.checkBox_3.setChecked(not bool(10))
            self.checkBox_4.setChecked(not bool(10))
        else:
            self.groupBox.setEnabled(bool(a0))
            pass

    def on_checkBox_2_stateChanged(self,a0):
        if a0 == QtCore.Qt.Checked:
            self.groupBox_2.setEnabled(bool(a0))
            self.groupBox.setChecked(not bool(a0))
            self.groupBox_3.setEnabled(not bool(a0))
            self.groupBox_4.setEnabled(not bool(a0))
            self.checkBox.setChecked(not bool(a0))
            self.checkBox_3.setChecked(not bool(10))
            self.checkBox_4.setChecked(not bool(10))
        else:
            self.groupBox_2.setEnabled(bool(a0))
            pass

    def on_checkBox_3_stateChanged(self,a0):
        if a0 == QtCore.Qt.Checked:
            self.groupBox_3.setEnabled(bool(a0))
            self.groupBox.setChecked(not bool(a0))
            self.groupBox_2.setEnabled(not bool(a0))
            self.groupBox_4.setEnabled(not bool(a0))
            self.checkBox.setChecked(not bool(a0))
            self.checkBox_2.setChecked(not bool(10))
            self.checkBox_4.setChecked(not bool(10))
        else:
            self.groupBox_3.setEnabled(bool(a0))
            pass

    def on_checkBox_4_stateChanged(self,a0):
        if a0 == QtCore.Qt.Checked:
            self.groupBox_4.setEnabled(bool(a0))
            self.groupBox.setChecked(not bool(a0))
            self.groupBox_2.setEnabled(not bool(a0))
            self.groupBox_3.setEnabled(not bool(a0))
            self.checkBox.setChecked(not bool(a0))
            self.checkBox_2.setChecked(not bool(10))
            self.checkBox_3.setChecked(not bool(10))
        else:
            self.groupBox_4.setEnabled(bool(a0))
            pass

    def _getChecked(self):
        if self.checkBox.isChecked():
            return self.checkBox.text()
        elif self.checkBox_2.isChecked():
            return self.checkBox_2.text()
        elif self.checkBox_3.isChecked():
            return self.checkBox_3.text()
        elif self.checkBox_4.isChecked():
            return self.checkBox_4.text()
        else:
            return ''

    def _getValue_0(self):
        try:
            self.__data['ResourceStateNotify'].ResourceId           = int(self.lineEdit_ResourceId.text())
            self.__data['ResourceStateNotify'].NotifyTime           = self.dateTimeEdit_NotifyTime.dateTime()
            self.__data['ResourceStateNotify'].RunTimeState         = self.comboBox_RunTimeState.currentIndex()+1
            self.__data['ResourceStateNotify'].QueueStock           = int(self.lineEdit_QueueStock.text())
            self.__data['ResourceStateNotify'].lastTimeQueueStock   = int(self.lineEdit_lastTimeQueueStock.text())
            self.__data['ResourceStateNotify'].reportTimeInterval   = int(self.lineEdit_reportTimeInterval.text())
            self.__data['ResourceStateNotify'].submitTotal          = int(self.lineEdit_submitTotal.text())
            self.__data['ResourceStateNotify'].submitFail           = int(self.lineEdit_submitFail.text())
            self.__data['ResourceStateNotify'].reportTotal          = int(self.lineEdit_reportTotal.text())
            self.__data['ResourceStateNotify'].reportFail           = int(self.lineEdit_reportFail.text())
            return self.__data['ResourceStateNotify'].Value()
        except Exception as e:
            print(e)

    def _getValue_1(self):
        try:
            self.__data['SDispatchStatistics'].dispatchCenterId = int(self.lineEdit_dispatchCenterId.text())
            self.__data['SDispatchStatistics'].totalDispatchCnt = int(self.lineEdit_totalDispatchCnt.text())
            self.__data['SDispatchStatistics'].succDispatchCnt  = int(self.lineEdit_succDispatchCnt.text())
            self.__data['SDispatchStatistics'].failDispatchCnt  = int(self.lineEdit_failDispatchCnt.text())
            self.__data['SDispatchStatistics'].cycleTime        = int(self.lineEdit_cycleTime.text())
            self.__data['SDispatchStatistics'].createTime       =  int(time.time())
            self.__data['SDispatchStatistics'].write_header()
            return self.__data['SDispatchStatistics'].Value()
        except Exception as e:
            print(e)

    def _getValue_2(self):
        try:
            self.__data['SResComStatistics'].resourceId = int(self.lineEdit_resourceId.text())
            self.__data['SResComStatistics'].succCnt    = int(self.lineEdit_succCnt.text())
            self.__data['SResComStatistics'].failCnt    = int(self.lineEdit_failCnt.text())
            self.__data['SResComStatistics'].cycleTime  = int(self.lineEdit_cycleTime_2.text())
            self.__data['SResComStatistics'].createTime = int(time.time())
            return self.__data['SResComStatistics'].Value()
        except Exception as e:
            print(e)

    def _getValue_3(self):
        try:
            self.__data['SResourceState'].resourceId            = int(self.lineEdit_resourceId_2.text())
            self.__data['SResourceState'].reportTime            = self.dateTimeEdit_reportTime.dateTime()
            self.__data['SResourceState'].statisticsConfig      = int(self.lineEdit_statisticsConfig.text())
            self.__data['SResourceState'].currentStock          = int(self.lineEdit_currentStock.text())
            self.__data['SResourceState'].lastStock             = int(self.lineEdit_lastStock.text())
            self.__data['SResourceState'].reportTimeInterval    = int(self.lineEdit_reportTimeInterval_2.text())
            self.__data['SResourceState'].submitTotal           = int(self.lineEdit_submitTotal_2.text())
            self.__data['SResourceState'].currentSubmitSuccess  = int(self.lineEdit_currentSubmitSuccess.text())
            self.__data['SResourceState'].currentSubmitFail     = int(self.lineEdit_currentSubmitFail.text())
            self.__data['SResourceState'].reportTotal           = int(self.lineEdit_reportTotal_2.text())
            self.__data['SResourceState'].currentReportSuccess  = int(self.lineEdit_currentReportSuccess.text())
            self.__data['SResourceState'].currentReportFail     = int(self.lineEdit_currentReportFail.text())
            self.__data['SResourceState'].moTotal               = int(self.lineEdit_moTotal.text())
            self.__data['SResourceState'].currentMoTotal        = int(self.lineEdit_currentMoTotal.text())
            self.__data['SResourceState'].state                 = int(self.comboBox_state.currentIndex()+1)
            return self.__data['SResourceState'].Value()
        except Exception as e:
            print(e)


    def getValue(self):
        try:
            return self.__func[self._getChecked()]()
        except Exception as e:
            print(e)

    def _analyze_0(self):
        try:

            self.lineEdit_ResourceId.setText(str(self.__data['ResourceStateNotify'].ResourceId))
            self.dateTimeEdit_NotifyTime.setDateTime(self.__data['ResourceStateNotify'].NotifyTime)
            self.comboBox_RunTimeState.setCurrentIndex(self.__data['ResourceStateNotify'].RunTimeState-1)
            self.lineEdit_QueueStock.setText(str(self.__data['ResourceStateNotify'].QueueStock))
            self.lineEdit_lastTimeQueueStock.setText(str(self.__data['ResourceStateNotify'].lastTimeQueueStock))
            self.lineEdit_reportTimeInterval.setText(str(self.__data['ResourceStateNotify'].reportTimeInterval))
            self.lineEdit_submitTotal.setText(str(self.__data['ResourceStateNotify'].submitTotal))
            self.lineEdit_submitFail.setText(str(self.__data['ResourceStateNotify'].submitFail))
            self.lineEdit_reportTotal.setText(str(self.__data['ResourceStateNotify'].reportTotal))
            self.lineEdit_reportFail.setText(str(self.__data['ResourceStateNotify'].reportFail))
        except Exception as e:
            print(e)

    def _analyze_1(self):
        try:
            self.lineEdit_type.setText(str(self.__data['SDispatchStatistics']._head.MessageType))
            self.lineEdit_ver.setText(str(self.__data['SDispatchStatistics']._head.Version))
            self.lineEdit_len.setText(str(self.__data['SDispatchStatistics']._head.Length))
            self.lineEdit_dispatchCenterId.setText(str(self.__data['SDispatchStatistics'].dispatchCenterId))
            self.lineEdit_totalDispatchCnt.setText(str(self.__data['SDispatchStatistics'].totalDispatchCnt))
            self.lineEdit_failDispatchCnt.setText(str(self.__data['SDispatchStatistics'].failDispatchCnt))
            self.lineEdit_succDispatchCnt.setText(str(self.__data['SDispatchStatistics'].succDispatchCnt))
            self.lineEdit_cycleTime.setText(str(self.__data['SDispatchStatistics'].cycleTime))
        except Exception as e:
            print(e)

    def _analyze_2(self):
        try:
            self.lineEdit_type.setText(str(self.__data['SResComStatistics']._head.MessageType))
            self.lineEdit_ver.setText(str(self.__data['SResComStatistics']._head.Version))
            self.lineEdit_len.setText(str(self.__data['SResComStatistics']._head.Length))
            self.lineEdit_resourceId.setText(str(self.__data['SResComStatistics'].resourceId))
            self.lineEdit_succCnt.setText(str(self.__data['SResComStatistics'].succCnt))
            self.lineEdit_failCnt.setText(str(self.__data['SResComStatistics'].failCnt))
            self.lineEdit_cycleTime_2.setText(str(self.__data['SResComStatistics'].cycleTime))
        except Exception as e:
            print(e)

    def _analyze_3(self):
        try:
            self.lineEdit_type.setText(str(self.__data['SResourceState']._head.MessageType))
            self.lineEdit_ver.setText(str(self.__data['SResourceState']._head.Version))
            self.lineEdit_len.setText(str(self.__data['SResourceState']._head.Length))
            self.lineEdit_resourceId_2.setText(str(self.__data['SResourceState'].resourceId))
            self.dateTimeEdit_reportTime.setDateTime(self.__data['SResourceState'].reportTime)
            self.lineEdit_statisticsConfig.setText(str(self.__data['SResourceState'].statisticsConfig))
            self.lineEdit_currentStock.setText(str(self.__data['SResourceState'].currentStock))
            self.lineEdit_lastStock.setText(str(self.__data['SResourceState'].lastStock))
            self.lineEdit_reportTimeInterval_2.setText(str(self.__data['SResourceState'].reportTimeInterval))
            self.lineEdit_submitTotal_2.setText(str(self.__data['SResourceState'].submitTotal))
            self.lineEdit_currentSubmitSuccess.setText(str(self.__data['SResourceState'].currentSubmitSuccess))
            self.lineEdit_currentSubmitFail.setText(str(self.__data['SResourceState'].currentSubmitFail))
            self.lineEdit_reportTotal_2.setText(str(self.__data['SResourceState'].reportTotal))
            self.lineEdit_currentReportSuccess.setText(str(self.__data['SResourceState'].currentReportSuccess))
            self.lineEdit_currentReportFail.setText(str(self.__data['SResourceState'].currentReportFail))
            self.lineEdit_moTotal.setText(str(self.__data['SResourceState'].moTotal))
            self.lineEdit_currentMoTotal.setText(str(self.__data['SResourceState'].currentMoTotal))
            self.comboBox_state.setCurrentIndex(self.__data['SResourceState'].state-1)
        except Exception as e:
            print(e)

    def analyze(self,b):
        self.__data[self._getChecked()].fromBytes(b)
        self.__func_analy[self._getChecked()]()
        pass

    def updatedata(self):
        try:
            return self.__func[self._getChecked()]()
        except Exception as e:
            print(e)

    def saveConfig(self, filename):
        try:
            config = ConfigParser()
            config.add_section(m_section[5])
            config.set(m_section[5], m_keys_resoucestatenotify[0],self.lineEdit_ResourceId.text())
            config.set(m_section[5], m_keys_resoucestatenotify[1],self.dateTimeEdit_NotifyTime.dateTime().toString())
            config.set(m_section[5], m_keys_resoucestatenotify[2],str(self.comboBox_RunTimeState.currentIndex()))
            config.set(m_section[5], m_keys_resoucestatenotify[3],self.lineEdit_QueueStock.text())
            config.set(m_section[5], m_keys_resoucestatenotify[4],self.lineEdit_lastTimeQueueStock.text())
            config.set(m_section[5], m_keys_resoucestatenotify[5],self.lineEdit_reportTimeInterval.text())
            config.set(m_section[5], m_keys_resoucestatenotify[6],self.lineEdit_submitTotal.text())
            config.set(m_section[5], m_keys_resoucestatenotify[7],self.lineEdit_submitFail.text())
            config.set(m_section[5], m_keys_resoucestatenotify[8],self.lineEdit_reportTotal.text())
            config.set(m_section[5], m_keys_resoucestatenotify[9],self.lineEdit_reportFail.text())

            config.add_section(m_section[6])
            config.set(m_section[6], m_keys_sdispatchstatistics[0],self.lineEdit_dispatchCenterId.text())
            config.set(m_section[6], m_keys_sdispatchstatistics[1],self.lineEdit_totalDispatchCnt.text())
            config.set(m_section[6], m_keys_sdispatchstatistics[2],self.lineEdit_failDispatchCnt.text())
            config.set(m_section[6], m_keys_sdispatchstatistics[3],self.lineEdit_succDispatchCnt.text())
            config.set(m_section[6], m_keys_sdispatchstatistics[4],self.lineEdit_cycleTime.text())

            config.add_section(m_section[7])
            config.set(m_section[7], m_keys_srescomstatistics[0],self.lineEdit_resourceId.text())
            config.set(m_section[7], m_keys_srescomstatistics[1],self.lineEdit_succCnt.text())
            config.set(m_section[7], m_keys_srescomstatistics[2],self.lineEdit_failCnt.text())
            config.set(m_section[7], m_keys_srescomstatistics[3],self.lineEdit_cycleTime_2.text())

            config.add_section(m_section[8])
            config.set(m_section[8],m_keys_resourcestate[0],self.lineEdit_resourceId_2.text())
            config.set(m_section[8],m_keys_resourcestate[1],self.dateTimeEdit_reportTime.dateTime().toString())
            config.set(m_section[8],m_keys_resourcestate[2],self.lineEdit_statisticsConfig.text())
            config.set(m_section[8],m_keys_resourcestate[3],self.lineEdit_currentStock.text())
            config.set(m_section[8],m_keys_resourcestate[4],self.lineEdit_lastStock.text())
            config.set(m_section[8],m_keys_resourcestate[5],self.lineEdit_reportTimeInterval_2.text())
            config.set(m_section[8],m_keys_resourcestate[6],self.lineEdit_submitTotal_2.text())
            config.set(m_section[8],m_keys_resourcestate[7],self.lineEdit_currentSubmitSuccess.text())
            config.set(m_section[8],m_keys_resourcestate[8],self.lineEdit_currentSubmitFail.text())
            config.set(m_section[8],m_keys_resourcestate[9],self.lineEdit_reportTotal_2.text())
            config.set(m_section[8],m_keys_resourcestate[10],self.lineEdit_currentReportSuccess.text())
            config.set(m_section[8],m_keys_resourcestate[11],self.lineEdit_currentReportFail.text())
            config.set(m_section[8],m_keys_resourcestate[12],self.lineEdit_moTotal.text())
            config.set(m_section[8],m_keys_resourcestate[13],self.lineEdit_currentMoTotal.text())
            config.set(m_section[8],m_keys_resourcestate[14],str(self.comboBox_state.currentIndex()))

            with open('config/'+filename+'.ini','w',encoding='gbk') as f:
                config.write(f)
        except Exception as e:
            print(e)
            print('保存配置失败')

    def loadConfig(self,filename):
        try:
            config = ConfigParser()
            config.read(filename,encoding='gbk')
            if not config.has_section(m_section[5]) or not config.has_section(m_section[6]) or not config.has_section(m_section[7]):
                print(filename,'do not have section',m_section[5],m_section[6],m_section[7])
                return False
            # if len(config.items(m_section[0])) != len(m_keys_cloudmsg):
            #     print(filename,'items error\n allkeys:\n',m_keys_cloudmsg)
            #     return False

            self.lineEdit_ResourceId.setText(config[m_section[5]][m_keys_resoucestatenotify[0]])
            self.dateTimeEdit_NotifyTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[5]][m_keys_resoucestatenotify[1]]))
            self.comboBox_RunTimeState.setCurrentIndex(int(config[m_section[5]][m_keys_resoucestatenotify[2]]))
            self.lineEdit_QueueStock.setText(config[m_section[5]][m_keys_resoucestatenotify[3]])
            self.lineEdit_lastTimeQueueStock.setText(config[m_section[5]][m_keys_resoucestatenotify[4]])
            self.lineEdit_reportTimeInterval.setText(config[m_section[5]][m_keys_resoucestatenotify[5]])
            self.lineEdit_submitTotal.setText(config[m_section[5]][m_keys_resoucestatenotify[6]])
            self.lineEdit_submitFail.setText(config[m_section[5]][m_keys_resoucestatenotify[7]])
            self.lineEdit_reportTotal.setText(config[m_section[5]][m_keys_resoucestatenotify[8]])
            self.lineEdit_reportFail.setText(config[m_section[5]][m_keys_resoucestatenotify[9]])

            self.lineEdit_dispatchCenterId.setText(config[m_section[6]][m_keys_sdispatchstatistics[0]])
            self.lineEdit_totalDispatchCnt.setText(config[m_section[6]][m_keys_sdispatchstatistics[1]])
            self.lineEdit_failDispatchCnt.setText(config[m_section[6]][m_keys_sdispatchstatistics[2]])
            self.lineEdit_succDispatchCnt.setText(config[m_section[6]][m_keys_sdispatchstatistics[3]])
            self.lineEdit_cycleTime.setText(config[m_section[6]][m_keys_sdispatchstatistics[4]])

            self.lineEdit_resourceId.setText(config[m_section[7]][m_keys_srescomstatistics[0]])
            self.lineEdit_succCnt.setText(config[m_section[7]][m_keys_srescomstatistics[1]])
            self.lineEdit_failCnt.setText(config[m_section[7]][m_keys_srescomstatistics[2]])
            self.lineEdit_cycleTime_2.setText(config[m_section[7]][m_keys_srescomstatistics[3]])

            self.lineEdit_resourceId_2.setText(config[m_section[8]][m_keys_resourcestate[0]])
            self.dateTimeEdit_reportTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[8]][m_keys_resourcestate[1]]))
            self.lineEdit_statisticsConfig.setText(config[m_section[8]][m_keys_resourcestate[2]])
            self.lineEdit_currentStock.setText(config[m_section[8]][m_keys_resourcestate[3]])
            self.lineEdit_lastStock.setText(config[m_section[8]][m_keys_resourcestate[4]])
            self.lineEdit_reportTimeInterval_2.setText(config[m_section[8]][m_keys_resourcestate[5]])
            self.lineEdit_submitTotal_2.setText(config[m_section[8]][m_keys_resourcestate[6]])
            self.lineEdit_currentSubmitSuccess.setText(config[m_section[8]][m_keys_resourcestate[7]])
            self.lineEdit_currentSubmitFail.setText(config[m_section[8]][m_keys_resourcestate[8]])
            self.lineEdit_reportTotal_2.setText(config[m_section[8]][m_keys_resourcestate[9]])
            self.lineEdit_currentReportSuccess.setText(config[m_section[8]][m_keys_resourcestate[10]])
            self.lineEdit_currentReportFail.setText(config[m_section[8]][m_keys_resourcestate[11]])
            self.lineEdit_moTotal.setText(config[m_section[8]][m_keys_resourcestate[12]])
            self.lineEdit_currentMoTotal.setText(config[m_section[8]][m_keys_resourcestate[13]])
            self.comboBox_state.setCurrentIndex(int(config[m_section[8]][m_keys_resourcestate[14]]))

        except Exception as e:
            print(e)
            print('加载配置失败')