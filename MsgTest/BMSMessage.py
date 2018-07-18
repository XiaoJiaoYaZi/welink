from PyQt5 import QtWidgets,QtCore
from UI_SBMSMessage import Ui_SBMSMessage
from UI_SHisSendData import Ui_SHisSendData
from UI_SHisRepData import Ui_SHisRepData
from UI_SRepNotifyData import Ui_SRepNotifyData
from UI_SHisMOData import Ui_SHisMOData
from UI_MoAccBlist import Ui_MoAccBlist
from UI_Monitor import Ui_Monitor
from SMessage import SBmsMessage,SHisSendData,SHisRepData,SRepNotifyData,SHisMOData,MoAccBlist
from MonitorMsgHeader import *
import time
import socket
import struct
from ctypes import *
from configparser import ConfigParser

EBmsMsgFormat={
    0:0,
    1:8
}

m_section  = ["BMSMessage","BMSSHisSendData","BMSSHisRepData","SRepNotifyData","SHisMOData","MoAccBlist",
              'SubmitMonitorMsg','HisPreDealMonitorData','HisCenterMonitorData','SResourceState',
              'SHeartBeat','DispatchMonitorMsg','log']

m_keys = (
    "消息级别",
    "消息编码方式",
    "消息ID",
    "扩展产品",
    "提交的扩展产品",
    "开始发送日期",
    "结束发送日期",
    "开始发送时段",
    "结束发送时段",
    "信息提交时间",
    "计费号码数",
    "消息状态",
    "消息类型",
    "号码个数",
    "提交类型",
    "账户ID",
    "审核ID",
    "提交ip",
    "进入调度中心次数",
    "长短信页数",
    "FlagBits",
    "最后一次资源发送失败",
    "失败类型",
    "失败状态",
    "最后一次调度时间",
    "资源发送次数",
    "发送失败总重发次数",
    "回执失败/超时总重发次数",
    "分包号码的总包数",
    "分包号码的当前包号",
    "电话号码",
    "短信内容",
    "签名",
    "扩展号码",
    "客户自定义参数",
    "彩信标题",
    "彩信存储文件路径"
)
m_keys_HisSendData=(
    '消息编号',
    '账号ID',
    '扩展产品ID',
    '提交产品ID',
    '资源编号',
    '发送时间',
    '提交时间',
    '手机号码',
    '匹配编号',
    '信息总页数',
    '当前页码',
    '计费数',
    '发送次数',
    '消息类型',
    '发送状态',
    '消息级别',
    'FlagBits',
    '发送失败剩余重发次数',
    '剩余回执问题重发次数',
    '信息内容',
    '整信息内容',
    '签名',
    '服务商号',
    '扩展号码',
    '客户自定义id',
    '发送结果内容',
    '标题'
)
m_keys_SHisRepData = (
    "手机号码",
    "匹配编号",
    "资源ID",
    "回执时间",
    "是否成功",
    "flagbits",
    "重新匹配次数",
    "回执内容",
)
m_keys_SRepNotifyData = (
    '消息ID',
    '用户ID',
    '电话号码',
    '发送状态',
    '回执状态',
    '发送时间',
    '回执时间',
    '回执本地时间',
    '信息总页数',
    '信息当前页数',
    'flagbits',
    '发送结果内容',
    '状态报告结果内容',
    '服务商号',
    '客户自定义id',
    '扩展号码',
)
m_keys_SHisMOData = (
    "消息ID",
    "消息类型",
    "用户ID",
    "手机号码",
    "上行时间",
    "资源ID",
    "处理次数",
    "服务商号",
    "上行内容",
)
m_keys_MoAccBlist = (
    "电话号码",
    "账户ID",
    "黑名单级别",
    "Flag",
    "Operator",
    "Remark",
)
m_keys_SubmitMonitor = (
    'succ',
    'fail',
    'fee',
)
m_keys_HisPreDealMonitor = (
    'rcvCnt',
    'perRcvCnt',
    'mtchCnt',
    'sndFldRsndCnt',
    'repFldRsndCnt',
    'repTmoutRsndCnt',
)
m_keys_HisCenterMonitor = (
    'preCnt',
    'rcvMsgCnt',
    'directInstCnt',
    'repMtchCnt',
    'repRtryMtchCnt',
    'repDismtchCnt',
    'moMsgCnt',
)
m_keys_ResouseState = (
    'resid',
    'statisticsConfig',
    'currentStock',
    'lastStock',
    'reportTimeInterval',
    'submitTotal',
    'currentSubmitSuccess',
    'currentSubmitFail',
    'reportTotal',
    'currentReportSuccess',
    'currentReportFail',
    'moTotal',
    'currentMoTotal',
    'state'
)
m_keys_HeartBeat = (
    'timeInterval',
    'stat',
    'alarm_module',
)
m_keys_log = (
    'level',
    'ip',
    'name',
    'msg',
)
m_keys_DisPatchMonitor = (
    '状态',
    '运营商',
    '省份',
)
m_key = [m_keys,m_keys_HisSendData,m_keys_SHisRepData,m_keys_SRepNotifyData,
         m_keys_SHisMOData,m_keys_MoAccBlist,m_keys_SubmitMonitor,m_keys_HisPreDealMonitor,
         m_keys_HisCenterMonitor,m_keys_ResouseState,m_keys_HeartBeat,m_keys_DisPatchMonitor,m_keys_log]

oneday = 24*60*60

def dt_time(time_str = None):
    seconds = time_str.hour*3600 + time_str.minute*60 + time_str.second
    return seconds/oneday
def time_dt(value):
    return time.strftime("%H:%M:%S", time.gmtime(value*oneday))

def dt_Datetime(time_str):
    return time.mktime(time.strptime(time_str))/oneday+25569.333333333332

def Datetime_dt(value):
    return (value-25569.333333333332)*3600*24
    #return time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime((value-25569.333333333332)*3600))

def bytes2int(b):
    if len(b) == 1:
        return struct.Struct('B').unpack(b)[0]
    elif len(b) == 2:
        return struct.Struct('H').unpack(b)[0]
    elif len(b) == 4:
        return struct.Struct('I').unpack(b)[0]
    elif len(b) == 8:
        return struct.Struct('L').unpack(b)[0]
    else:
        raise BufferError

def int2ipbyte(value):
    return struct.Struct('I').pack(value)



class BMSMessage(QtWidgets.QWidget,Ui_SBMSMessage):
    def __init__(self):
        super(BMSMessage,self).__init__()
        self.setupUi(self)
        self.__data = SBmsMessage()

    def getValue(self):
        try:
            self.__data.clear()
            self.__data.SBmsMsgHead.Priority             = int(self.lineEdit_Priority.text())
            self.__data.SBmsMsgHead.MsgFormat            =EBmsMsgFormat[self.comboBox_MsgFormat.currentIndex()]
            self.__data.SBmsMsgHead.MsgId                =int(self.lineEdit_MsgId.text())
            self.__data.SBmsMsgHead.PrdExId              =int(self.lineEdit_PrdExId.text())
            self.__data.SBmsMsgHead.SubmitPrdExId        =int(self.lineEdit_SubmitPrdExId.text())
            self.__data.SBmsMsgHead.StartSendDateTime    =dt_Datetime(self.dateTimeEdit_StartSendDateTime.dateTime().toPyDateTime().ctime())
            self.__data.SBmsMsgHead.EndSendDateTime      =dt_Datetime(self.dateTimeEdit_EndSendDateTime.dateTime().toPyDateTime().ctime())
            self.__data.SBmsMsgHead.StartSendTime        =dt_time(self.timeEdit_StartSendTime.time().toPyTime())
            self.__data.SBmsMsgHead.EndSendTime          =dt_time(self.timeEdit_EndSendTime.time().toPyTime())
            self.__data.SBmsMsgHead.CommitTime           =dt_Datetime(self.dateTimeEdit_CommitTime.dateTime().toPyDateTime().ctime())
            self.__data.SBmsMsgHead.ChargeQuantity       =int(self.lineEdit_ChargeQuantity.text())
            self.__data.SBmsMsgHead.MsgState             =int(self.comboBox_MsgState.currentIndex() + 1)
            self.__data.SBmsMsgHead.MsgType              =int(self.comboBox_MsgState.currentIndex() + 1)
            self.__data.SBmsMsgHead.MobilesCount         =int(self.lineEdit_MobilesCount.text())
            self.__data.SBmsMsgHead.SubmitType           =int(self.comboBox_SubmitType.currentIndex())
            self.__data.SBmsMsgHead.AccId                =int(self.lineEdit_AccId.text())
            self.__data.SBmsMsgHead.AuditorId            =int(self.lineEdit_AuditorId.text())
            self.__data.SBmsMsgHead.CommitIp             =bytes2int(socket.inet_aton(self.lineEdit_CommitIp.text()))
            ##
            self.__data.SBmsMsgTail.InnerDispatchTimes   =int(self.lineEdit_InnerDispatchTimes.text())
            self.__data.SBmsMsgTail.Pagetotal            =int(self.lineEdit_Pagetotal.text())
            self.__data.SBmsMsgTail.FlagBits             =int(self.lineEdit_FlagBits.text())
            self.__data.SBmsMsgTail.LastFailResId        =int(self.lineEdit_LastFailResId.text())
            self.__data.SBmsMsgTail.FailedType           =self.comboBox_FailedType.currentIndex()
            self.__data.SBmsMsgTail.FailedState          =int(self.lineEdit_FailedState.text())
            self.__data.SBmsMsgTail.LastDiapatchTime     =dt_Datetime(self.dateTimeEdit_LastDiapatchTime.dateTime().toPyDateTime().ctime())
            self.__data.SBmsMsgTail.ResSendTimes         =int(self.lineEdit_ResSendTimes.text())
            self.__data.SBmsMsgTail.TotalSndFldResndTimes=int(self.lineEdit_TotalSndFldResndTimes.text())
            self.__data.SBmsMsgTail.TotalRepFldResndTimes=int(self.lineEdit_TotalRepFldResndTimes.text())
            self.__data.SBmsMsgTail.PackageTotal         =int(self.lineEdit_Pagetotal.text())
            self.__data.SBmsMsgTail.PackageNum           =int(self.lineEdit_PackageNum.text())
            ##
            self.__data.write_mobile(self.lineEdit_mobile.text())
            self.__data.write_message(self.textEdit_content.toPlainText())
            self.__data.write_sign(self.lineEdit_sign.text())
            self.__data.write_extnumber(self.lineEdit_extnum.text())
            self.__data.write_acc_msgid(self.lineEdit_accmsgid.text())
            self.__data.write_mms_title(self.lineEdit_title.text())
            self.__data.write_mms_path(self.lineEdit_filepath.text())
            #
            self.__data.write_header()
            return self.__data.Value()
        except:
            print('参数错误')

    def updatedata(self):
        self.__data.SBmsMsgHead.MsgId +=1
        return self.__data.Value()

    def saveConfig(self,filename):
        try:
            config = ConfigParser()
            config.add_section('BMSMessage')
            config.set(m_section[0], m_keys[0], self.lineEdit_Priority.text())
            config.set(m_section[0], m_keys[1], str(self.comboBox_MsgFormat.currentIndex()))
            config.set(m_section[0], m_keys[2], self.lineEdit_MsgId.text())
            config.set(m_section[0], m_keys[3], self.lineEdit_PrdExId.text())
            config.set(m_section[0], m_keys[4], self.lineEdit_SubmitPrdExId.text())
            config.set(m_section[0], m_keys[5], self.dateTimeEdit_StartSendDateTime.dateTime().toString())
            config.set(m_section[0], m_keys[6], self.dateTimeEdit_EndSendDateTime.dateTime().toString())
            config.set(m_section[0], m_keys[7], self.timeEdit_StartSendTime.time().toString())
            config.set(m_section[0], m_keys[8], self.timeEdit_EndSendTime.time().toString())
            config.set(m_section[0], m_keys[9], self.dateTimeEdit_CommitTime.dateTime().toString())
            config.set(m_section[0], m_keys[10], self.lineEdit_ChargeQuantity.text())
            config.set(m_section[0], m_keys[11], str(self.comboBox_MsgState.currentIndex()))
            config.set(m_section[0], m_keys[12], str(self.comboBox_MsgState.currentIndex()))
            config.set(m_section[0], m_keys[13], self.lineEdit_MobilesCount.text())
            config.set(m_section[0], m_keys[14], str(self.comboBox_SubmitType.currentIndex()))
            config.set(m_section[0], m_keys[15], self.lineEdit_AccId.text())
            config.set(m_section[0], m_keys[16], self.lineEdit_AuditorId.text())
            config.set(m_section[0], m_keys[17], self.lineEdit_CommitIp.text())
            config.set(m_section[0], m_keys[18], self.lineEdit_InnerDispatchTimes.text())
            config.set(m_section[0], m_keys[19], self.lineEdit_Pagetotal.text())
            config.set(m_section[0], m_keys[20], self.lineEdit_FlagBits.text())
            config.set(m_section[0], m_keys[21], self.lineEdit_LastFailResId.text())
            config.set(m_section[0], m_keys[22], str(self.comboBox_FailedType.currentIndex()))
            config.set(m_section[0], m_keys[23], self.lineEdit_FailedState.text())
            config.set(m_section[0], m_keys[24], self.dateTimeEdit_LastDiapatchTime.dateTime().toString())
            config.set(m_section[0], m_keys[25], self.lineEdit_ResSendTimes.text())
            config.set(m_section[0], m_keys[26], self.lineEdit_TotalSndFldResndTimes.text())
            config.set(m_section[0], m_keys[27], self.lineEdit_TotalRepFldResndTimes.text())
            config.set(m_section[0], m_keys[28], self.lineEdit_Pagetotal.text())
            config.set(m_section[0], m_keys[29], self.lineEdit_PackageNum.text())
            config.set(m_section[0], m_keys[30], self.lineEdit_mobile.text())
            config.set(m_section[0], m_keys[31], self.textEdit_content.toPlainText())
            config.set(m_section[0], m_keys[32], self.lineEdit_sign.text())
            config.set(m_section[0], m_keys[33], self.lineEdit_extnum.text())
            config.set(m_section[0], m_keys[34], self.lineEdit_accmsgid.text())
            config.set(m_section[0], m_keys[35], self.lineEdit_title.text())
            config.set(m_section[0], m_keys[36], self.lineEdit_filepath.text())


            with open('config/'+filename+'.ini','w',encoding='utf-8') as f:
                config.write(f)
        except:
            print('saveConfig error ',filename)


    def loadConfig(self,filename):
        try:
            config = ConfigParser()
            config.read(filename,encoding='utf-8')
            if not config.has_section(m_section[0]):
                print(filename,'do not have section',m_section[0])
                return False
            if len(config.items(m_section[0])) != len(m_keys):
                print(filename,'items error\n allkeys:\n',m_keys)
                return False
            self.lineEdit_Priority.setText(config[m_section[0]][m_keys[0]])
            self.comboBox_MsgFormat.setCurrentIndex(int(config[m_section[0]][m_keys[1]]))
            self.lineEdit_MsgId.setText(config[m_section[0]][m_keys[2]])
            self.lineEdit_PrdExId.setText(config[m_section[0]][m_keys[3]])
            self.lineEdit_SubmitPrdExId.setText(config[m_section[0]][m_keys[4]])
            self.dateTimeEdit_StartSendDateTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[0]][m_keys[5]]))
            self.dateTimeEdit_EndSendDateTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[0]][m_keys[6]]))
            self.timeEdit_StartSendTime.setTime(QtCore.QTime.fromString(config[m_section[0]][m_keys[7]]))
            self.timeEdit_EndSendTime.setTime(QtCore.QTime.fromString(config[m_section[0]][m_keys[8]]))
            self.dateTimeEdit_CommitTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[0]][m_keys[9]]))
            self.lineEdit_ChargeQuantity.setText(config[m_section[0]][m_keys[10]])
            self.comboBox_MsgState.setCurrentIndex(int(config[m_section[0]][m_keys[11]]))
            self.comboBox_MsgState.setCurrentIndex(int(config[m_section[0]][m_keys[12]]))
            self.lineEdit_MobilesCount.setText(config[m_section[0]][m_keys[13]])
            self.comboBox_SubmitType.setCurrentIndex(int(config[m_section[0]][m_keys[14]]))
            self.lineEdit_AccId.setText(config[m_section[0]][m_keys[15]])
            self.lineEdit_AuditorId.setText(config[m_section[0]][m_keys[16]])
            self.lineEdit_CommitIp.setText(config[m_section[0]][m_keys[17]])
            self.lineEdit_InnerDispatchTimes.setText(config[m_section[0]][m_keys[18]])
            self.lineEdit_Pagetotal.setText(config[m_section[0]][m_keys[19]])
            self.lineEdit_FlagBits.setText(config[m_section[0]][m_keys[20]])
            self.lineEdit_LastFailResId.setText(config[m_section[0]][m_keys[21]])
            self.comboBox_FailedType.setCurrentIndex(int(config[m_section[0]][m_keys[22]]))
            self.lineEdit_FailedState.setText(config[m_section[0]][m_keys[23]])
            self.dateTimeEdit_LastDiapatchTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[0]][m_keys[24]]))
            self.lineEdit_ResSendTimes.setText(config[m_section[0]][m_keys[25]])
            self.lineEdit_TotalSndFldResndTimes.setText(config[m_section[0]][m_keys[26]])
            self.lineEdit_TotalRepFldResndTimes.setText(config[m_section[0]][m_keys[27]])
            self.lineEdit_Pagetotal.setText(config[m_section[0]][m_keys[28]])
            self.lineEdit_PackageNum.setText(config[m_section[0]][m_keys[29]])
            self.lineEdit_mobile.setText(config[m_section[0]][m_keys[30]])
            self.textEdit_content.setText(config[m_section[0]][m_keys[31]])
            self.lineEdit_sign.setText(config[m_section[0]][m_keys[32]])
            self.lineEdit_extnum.setText(config[m_section[0]][m_keys[33]])
            self.lineEdit_accmsgid.setText(config[m_section[0]][m_keys[34]])
            self.lineEdit_title.setText(config[m_section[0]][m_keys[35]])
            self.lineEdit_filepath.setText(config[m_section[0]][m_keys[36]])
        except:
            print('loadConfig error',filename)


    def analyze(self,b):
        self.__data.fromBytes(b)
        self.__analyze()

    def __analyze(self):
        try:

            self.lineEdit_Priority.setText(str(self.__data.SBmsMsgHead.Priority))
            self.comboBox_MsgFormat.setCurrentIndex(self.__data.SBmsMsgHead.MsgFormat)
            self.lineEdit_MsgId.setText(str(self.__data.SBmsMsgHead.MsgId))
            self.lineEdit_PrdExId.setText(str(self.__data.SBmsMsgHead.PrdExId))
            self.lineEdit_SubmitPrdExId.setText(str(self.__data.SBmsMsgHead.SubmitPrdExId))
            self.dateTimeEdit_StartSendDateTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data.SBmsMsgHead.StartSendDateTime)))
            self.dateTimeEdit_EndSendDateTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data.SBmsMsgHead.EndSendDateTime)))
            self.timeEdit_StartSendTime.setTime(QtCore.QTime.fromString(time_dt(self.__data.SBmsMsgHead.StartSendTime)))
            self.timeEdit_EndSendTime.setTime(QtCore.QTime.fromString(time_dt(self.__data.SBmsMsgHead.EndSendTime)))
            self.dateTimeEdit_CommitTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data.SBmsMsgHead.CommitTime)))
            self.lineEdit_ChargeQuantity.setText(str(self.__data.SBmsMsgHead.ChargeQuantity))
            self.comboBox_MsgState.setCurrentIndex(self.__data.SBmsMsgHead.MsgState-1)
            self.comboBox_MsgState.setCurrentIndex(self.__data.SBmsMsgHead.MsgType-1)
            self.lineEdit_MobilesCount.setText(str(self.__data.SBmsMsgHead.MobilesCount))
            self.comboBox_SubmitType.setCurrentIndex(self.__data.SBmsMsgHead.SubmitType)
            self.lineEdit_AccId.setText(str(self.__data.SBmsMsgHead.AccId))
            self.lineEdit_AuditorId.setText(str(self.__data.SBmsMsgHead.AuditorId))
            self.lineEdit_CommitIp.setText(str(socket.inet_ntoa(int2ipbyte(self.__data.SBmsMsgHead.CommitIp))))
            ##
            self.lineEdit_InnerDispatchTimes.setText(str(self.__data.SBmsMsgTail.InnerDispatchTimes ))
            self.lineEdit_Pagetotal.setText(str(self.__data.SBmsMsgTail.Pagetotal))
            self.lineEdit_FlagBits.setText(str(self.__data.SBmsMsgTail.FlagBits))
            self.lineEdit_LastFailResId.setText(str(self.__data.SBmsMsgTail.LastFailResId))
            self.comboBox_FailedType.setCurrentIndex(self.__data.SBmsMsgTail.FailedType)
            self.lineEdit_FailedState.setText(str(self.__data.SBmsMsgTail.FailedState))
            self.dateTimeEdit_LastDiapatchTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data.SBmsMsgTail.LastDiapatchTime)))
            self.lineEdit_ResSendTimes.setText(str(self.__data.SBmsMsgTail.ResSendTimes))
            self.lineEdit_TotalSndFldResndTimes.setText(str(self.__data.SBmsMsgTail.TotalSndFldResndTimes))
            self.lineEdit_TotalRepFldResndTimes.setText(str(self.__data.SBmsMsgTail.TotalRepFldResndTimes))
            self.lineEdit_Pagetotal.setText(str(self.__data.SBmsMsgTail.PackageTotal))
            self.lineEdit_PackageNum.setText(str(self.__data.SBmsMsgTail.PackageNum))

            self.lineEdit_mobile.setText(self.__data.mobiles)
            self.textEdit_content.setText(self.__data.messages)
            self.lineEdit_sign.setText(self.__data.signs)
            self.lineEdit_title.setText(self.__data.titles)
            self.lineEdit_extnum.setText(self.__data.extnumbers)
            self.lineEdit_filepath.setText(self.__data.path)
            self.lineEdit_accmsgid.setText(self.__data.accmsgids)

        except:
            print('__analyze error')

class BMSSHisSendData(QtWidgets.QWidget,Ui_SHisSendData):
    def __init__(self):
        super(BMSSHisSendData,self).__init__()
        self.setupUi(self)
        self.__data = SHisSendData()

    def getValue(self):
        try:
            self.__data.clear()
            self.__data.Data.msgId              = int(self.lineEdit_msgId.text())
            self.__data.Data.accId              = int(self.lineEdit_accId.text())
            self.__data.Data.prdExId            = int(self.lineEdit_prdExId.text())
            self.__data.Data.submitPrdExid      = int(self.lineEdit_submitPrdExid.text())
            self.__data.Data.sendDateTime       = dt_Datetime(self.dateTimeEdit_sendDateTime.dateTime().toPyDateTime().ctime())
            self.__data.Data.commitDateTime     = dt_Datetime(self.dateTimeEdit_commitDateTime.dateTime().toPyDateTime().ctime())
            self.__data.Data.mobile             = int(self.lineEdit_mobile.text())
            self.__data.Data.matchId            = int(self.lineEdit_matchId.text())
            self.__data.Data.pkTotal            = int(self.lineEdit_pkTotal.text())
            self.__data.Data.pkNum              = int(self.lineEdit_pkNum.text())
            self.__data.Data.chargeQuantity     = int(self.lineEdit_chargeQuantity.text())
            self.__data.Data.sendTimes          = int(self.lineEdit_sendTimes.text())
            self.__data.Data.msgType            = int(self.lineEdit_msgType.text())
            self.__data.Data.sendState          = int(self.lineEdit_sendState.text())
            self.__data.Data.priority           = int(self.lineEdit_priority.text())
            self.__data.Data.flagBits           = int(self.lineEdit_flagBits.text())
            self.__data.Data.rmSndFldRsndTimes  = int(self.lineEdit_rmSndFldRsndTimes.text())
            self.__data.Data.rmRepFldRsndTimes  = int(self.lineEdit_rmRepFldRsndTimes.text())
            self.__data.Data.dealTimes          = int(self.lineEdit_dealTimes.text())
            self.__data.Data.timeStamp          = int(time.time())

            self.__data.write_message(self.textEdit_content_one.toPlainText())
            self.__data.write_whlMsg(self.textEdit_content.toPlainText())
            self.__data.write_sign(self.lineEdit_sign.text())
            self.__data.write_spno(self.lineEdit_spno.text())
            self.__data.write_extnum(self.lineEdit_extnum.text())
            self.__data.write_accmsgid(self.lineEdit_accmsgid.text())
            self.__data.write_sendresult(self.lineEdit_sendresult.text())
            self.__data.write_title(self.lineEdit_title.text())
            self.__data.write_header()

            return self.__data.Value()
        except:
            print('参数错误')

    def updatedata(self):
        try:
            self.__data.Data.msgId +=1
            self.__data.Data.timeStamp = time.time()
            return  self.__data.Value()
        except:
            print('update error')


    def saveConfig(self,filename):
        try:
            config = ConfigParser()
            config.add_section(m_section[1])
            config.set(m_section[1],m_keys_HisSendData[0],self.lineEdit_msgId.text())
            config.set(m_section[1],m_keys_HisSendData[1],self.lineEdit_accId.text())
            config.set(m_section[1],m_keys_HisSendData[2],self.lineEdit_prdExId.text())
            config.set(m_section[1],m_keys_HisSendData[3],self.lineEdit_submitPrdExid.text())
            config.set(m_section[1],m_keys_HisSendData[4],self.dateTimeEdit_sendDateTime.dateTime().toString())
            config.set(m_section[1],m_keys_HisSendData[5],self.dateTimeEdit_commitDateTime.dateTime().toString())
            config.set(m_section[1],m_keys_HisSendData[6],self.lineEdit_mobile.text())
            config.set(m_section[1],m_keys_HisSendData[7],self.lineEdit_matchId.text())
            config.set(m_section[1],m_keys_HisSendData[8],self.lineEdit_pkTotal.text())
            config.set(m_section[1],m_keys_HisSendData[9],self.lineEdit_pkNum.text())
            config.set(m_section[1],m_keys_HisSendData[10],self.lineEdit_chargeQuantity.text())
            config.set(m_section[1],m_keys_HisSendData[11],self.lineEdit_sendTimes.text())
            config.set(m_section[1],m_keys_HisSendData[12],self.lineEdit_msgType.text())
            config.set(m_section[1],m_keys_HisSendData[13],self.lineEdit_sendState.text())
            config.set(m_section[1],m_keys_HisSendData[14],self.lineEdit_priority.text())
            config.set(m_section[1],m_keys_HisSendData[15],self.lineEdit_flagBits.text())
            config.set(m_section[1],m_keys_HisSendData[16],self.lineEdit_rmSndFldRsndTimes.text())
            config.set(m_section[1],m_keys_HisSendData[17],self.lineEdit_rmRepFldRsndTimes.text())
            config.set(m_section[1],m_keys_HisSendData[18],self.lineEdit_dealTimes.text())

            config.set(m_section[1],m_keys_HisSendData[19],self.textEdit_content_one.toPlainText())
            config.set(m_section[1],m_keys_HisSendData[20],self.textEdit_content.toPlainText())
            config.set(m_section[1],m_keys_HisSendData[21],self.lineEdit_sign.text())
            config.set(m_section[1],m_keys_HisSendData[22],self.lineEdit_spno.text())
            config.set(m_section[1],m_keys_HisSendData[23],self.lineEdit_extnum.text())
            config.set(m_section[1],m_keys_HisSendData[24],self.lineEdit_accmsgid.text())
            config.set(m_section[1],m_keys_HisSendData[25],self.lineEdit_sendresult.text())
            config.set(m_section[1],m_keys_HisSendData[26],self.lineEdit_title.text())

            with open('config/'+filename+'.ini','w',encoding='utf-8') as f:
                config.write(f)
        except:
            print('saveConfig error',filename)


    def loadConfig(self,filename):
        try:
            config = ConfigParser()
            config.read(filename,encoding='utf-8')
            if not config.has_section(m_section[1]):
                print(filename,'do not have section',m_section[1])
                return False
            if len(config.items(m_section[1])) != len(m_keys_HisSendData):
                print(filename,'items error\n allkeys:\n',m_keys_HisSendData)
                return False

            self.lineEdit_msgId.setText(config[m_section[1]][m_keys_HisSendData[0]])
            self.lineEdit_accId.setText(config[m_section[1]][m_keys_HisSendData[1]])
            self.lineEdit_prdExId.setText(config[m_section[1]][m_keys_HisSendData[2]])
            self.lineEdit_submitPrdExid.setText(config[m_section[1]][m_keys_HisSendData[3]])
            self.dateTimeEdit_sendDateTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[1]][m_keys_HisSendData[4]]))
            self.dateTimeEdit_commitDateTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[1]][m_keys_HisSendData[5]]))
            self.lineEdit_mobile.setText(config[m_section[1]][m_keys_HisSendData[6]])
            self.lineEdit_matchId.setText(config[m_section[1]][m_keys_HisSendData[7]])
            self.lineEdit_pkTotal.setText(config[m_section[1]][m_keys_HisSendData[8]])
            self.lineEdit_pkNum.setText(config[m_section[1]][m_keys_HisSendData[9]])
            self.lineEdit_chargeQuantity.setText(config[m_section[1]][m_keys_HisSendData[10]])
            self.lineEdit_sendTimes.setText(config[m_section[1]][m_keys_HisSendData[11]])
            self.lineEdit_msgType.setText(config[m_section[1]][m_keys_HisSendData[12]])
            self.lineEdit_sendState.setText(config[m_section[1]][m_keys_HisSendData[13]])
            self.lineEdit_priority.setText(config[m_section[1]][m_keys_HisSendData[14]])
            self.lineEdit_flagBits.setText(config[m_section[1]][m_keys_HisSendData[15]])
            self.lineEdit_rmSndFldRsndTimes.setText(config[m_section[1]][m_keys_HisSendData[16]])
            self.lineEdit_rmRepFldRsndTimes.setText(config[m_section[1]][m_keys_HisSendData[17]])
            self.lineEdit_dealTimes.setText(config[m_section[1]][m_keys_HisSendData[18]])

            self.textEdit_content_one.setText(config[m_section[1]][m_keys_HisSendData[19]])
            self.textEdit_content.setText(config[m_section[1]][m_keys_HisSendData[20]])
            self.lineEdit_sign.setText(config[m_section[1]][m_keys_HisSendData[21]])
            self.lineEdit_spno.setText(config[m_section[1]][m_keys_HisSendData[22]])
            self.lineEdit_extnum.setText(config[m_section[1]][m_keys_HisSendData[23]])
            self.lineEdit_accmsgid.setText(config[m_section[1]][m_keys_HisSendData[24]])
            self.lineEdit_sendresult.setText(config[m_section[1]][m_keys_HisSendData[25]])
            self.lineEdit_title.setText(config[m_section[1]][m_keys_HisSendData[26]])
        except:
            print('loadConfig error',filename)

    def analyze(self,b):
        self.__data.fromBytes(b)
        self.__analyze()

    def __analyze(self):
        self.lineEdit_msgId.setText(str(self.__data.Data.msgId))
        self.lineEdit_accId.setText(str(self.__data.Data.accId  ))
        self.lineEdit_prdExId.setText(str(self.__data.Data.prdExId))
        self.lineEdit_submitPrdExid.setText(str(self.__data.Data.submitPrdExid))
        self.dateTimeEdit_sendDateTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data.Data.sendDateTime)))
        self.dateTimeEdit_commitDateTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data.Data.commitDateTime)))
        self.lineEdit_mobile.setText(str(self.__data.Data.mobile))
        self.lineEdit_matchId.setText(str(self.__data.Data.matchId))
        self.lineEdit_pkTotal.setText(str(self.__data.Data.pkTotal))
        self.lineEdit_pkNum.setText(str(self.__data.Data.pkNum))
        self.lineEdit_chargeQuantity.setText(str(self.__data.Data.chargeQuantity))
        self.lineEdit_sendTimes.setText(str(self.__data.Data.sendTimes))
        self.lineEdit_msgType.setText(str(self.__data.Data.msgType))
        self.lineEdit_sendState.setText(str(int(self.__data.Data.sendState)))
        self.lineEdit_priority.setText(str(self.__data.Data.priority))
        self.lineEdit_flagBits.setText(str(self.__data.Data.flagBits))
        self.lineEdit_rmSndFldRsndTimes.setText(str(self.__data.Data.rmSndFldRsndTimes))
        self.lineEdit_rmRepFldRsndTimes.setText(str(self.__data.Data.rmRepFldRsndTimes))
        self.lineEdit_dealTimes.setText(str(self.__data.Data.dealTimes))

        self.textEdit_content_one.setText(self.__data.message)
        self.textEdit_content.setText(self.__data.whlMsg)
        self.lineEdit_sign.setText(self.__data.sign)
        self.lineEdit_spno.setText(self.__data.spno)
        self.lineEdit_extnum.setText(self.__data.extnum)
        self.lineEdit_accmsgid.setText(self.__data.accmsgid)
        self.lineEdit_sendresult.setText(self.__data.sendresult)
        self.lineEdit_title.setText(self.__data.title)

class BMSSHisRepData(QtWidgets.QWidget,Ui_SHisRepData):
    def __init__(self):
        super(BMSSHisRepData,self).__init__()
        self.setupUi(self)
        self.__data = SHisRepData()

    def getValue(self):
        try:
            self.__data.clear()
            self.__data.Data.mobile         =   int(self.lineEdit_mobile.text())
            self.__data.Data.matchId        =   int(self.lineEdit_matchId.text())
            self.__data.Data.resId          =   int(self.lineEdit_resId.text())
            self.__data.Data.reportDateTime =   dt_Datetime(self.dateTimeEdit.dateTime().toPyDateTime().ctime())
            self.__data.Data.reportState    =   int(self.lineEdit_reportState.text())
            self.__data.Data.flagBits       =   int(self.lineEdit_flagBits.text())
            self.__data.Data.retryTimes     =   int(self.lineEdit_retryTimes.text())
            self.__data.Data.timeStamp      =   int(time.time())

            self.__data.write_repResultInfo(self.textEdit.toPlainText())
            self.__data.write_header()
            return self.__data.Value()
        except:
            print('参数错误')

    def updatedata(self):
        try:
            self.__data.Data.timeStamp = int(time.time())
            return self.__data.Value()
        except:
            print('update error')

    def saveConfig(self,filename):
        try:
            config = ConfigParser()
            config.add_section(m_section[2])
            config.set(m_section[2], m_keys_SHisRepData[0],self.lineEdit_mobile.text())
            config.set(m_section[2], m_keys_SHisRepData[1],self.lineEdit_matchId.text())
            config.set(m_section[2], m_keys_SHisRepData[2],self.lineEdit_resId.text())
            config.set(m_section[2], m_keys_SHisRepData[3],self.dateTimeEdit.dateTime().toString())
            config.set(m_section[2], m_keys_SHisRepData[4],self.lineEdit_reportState.text())
            config.set(m_section[2], m_keys_SHisRepData[5],self.lineEdit_flagBits.text())
            config.set(m_section[2], m_keys_SHisRepData[6],self.lineEdit_retryTimes.text())
            config.set(m_section[2], m_keys_SHisRepData[7],self.textEdit.toPlainText())

            with open('config/'+filename+'.ini','w',encoding='utf-8') as f:
                config.write(f)
        except:
            print('saveConfig error',filename)

    def loadConfig(self,filename):
        try:
            config = ConfigParser()
            config.read(filename,encoding='utf-8')
            if not config.has_section(m_section[2]):
                print(filename,'do not have section',m_section[2])
                return False
            if len(config.items(m_section[2])) != len(m_keys_SHisRepData):
                print(filename,'items error\n allkeys:\n',m_keys_SHisRepData)
                return False

            self.lineEdit_mobile.setText(config[m_section[2]][m_keys_SHisRepData[0]])
            self.lineEdit_matchId.setText(config[m_section[2]][m_keys_SHisRepData[1]])
            self.lineEdit_resId.setText(config[m_section[2]][m_keys_SHisRepData[2]])
            self.dateTimeEdit.setDateTime(QtCore.QDateTime.fromString(config[m_section[2]][m_keys_SHisRepData[3]]))
            self.lineEdit_reportState.setText(config[m_section[2]][m_keys_SHisRepData[4]])
            self.lineEdit_flagBits.setText(config[m_section[2]][m_keys_SHisRepData[5]])
            self.lineEdit_retryTimes.setText(config[m_section[2]][m_keys_SHisRepData[6]])
            self.textEdit.setText(config[m_section[2]][m_keys_SHisRepData[7]])
        except:
            print('loadConfig',filename)
    def analyze(self,b):
        self.__data.fromBytes(b)
        self.__analyze()

    def __analyze(self):
        self.lineEdit_mobile.setText(str(self.__data.Data.mobile))
        self.lineEdit_matchId.setText(str(self.__data.Data.matchId))
        self.lineEdit_resId.setText(str(self.__data.Data.resId))
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data.Data.reportDateTime)))
        self.lineEdit_reportState.setText(str(int(self.__data.Data.reportState)))
        self.lineEdit_flagBits.setText(str(self.__data.Data.flagBits))
        self.lineEdit_retryTimes.setText(str(self.__data.Data.retryTimes))

        self.textEdit.setText(self.__data.repResultInfo)

class BMSSRepNotifyData(QtWidgets.QWidget,Ui_SRepNotifyData):
    def __init__(self):
        super(BMSSRepNotifyData,self).__init__()
        self.setupUi(self)
        self.__data = SRepNotifyData()

    def getValue(self):
        try:
            self.__data.clear()
            self.__data.Data.msgId              = int(self.lineEdit_msgId.text())
            self.__data.Data.accId              = int(self.lineEdit_accId.text())
            self.__data.Data.mobile             = int(self.lineEdit_mobile.text())
            self.__data.Data.sendState          = int(self.lineEdit_sendState.text())
            self.__data.Data.reportState        = int(self.lineEdit_reportState.text())
            self.__data.Data.sendDateTime       = dt_Datetime(self.dateTimeEdit_sendDateTime.dateTime().toPyDateTime().ctime())
            self.__data.Data.reportDateTime     = dt_Datetime(self.dateTimeEdit_reportDateTime.dateTime().toPyDateTime().ctime())
            self.__data.Data.recvReportDateTime = dt_Datetime(self.dateTimeEdit_recvReportDateTime.dateTime().toPyDateTime().ctime())
            self.__data.Data.pk_total           = int(self.lineEdit_pk_total.text())
            self.__data.Data.pk_num             = int(self.lineEdit_pk_num.text())
            self.__data.Data.flagBits           = int(self.lineEdit_flagBits.text())

            self.__data.write_sendResultInfo(self.textEdit_sendResultInfo.toPlainText())
            self.__data.write_repResultInfo(self.textEdit_repResultInfo.toPlainText())
            self.__data.write_spno(self.lineEdit_spno.text())
            self.__data.write_acc_msgid(self.lineEdit_acc_msgid.text())
            self.__data.write_extnumber(self.lineEdit_extnumber.text())
            self.__data.write_header()

            return self.__data.Value()
        except:
            print('参数错误')

    def updatedata(self):
        try:
            self.__data.Data.msgId +=1
            return self.__data.Value()
        except:
            print('update error')

    def saveConfig(self,filename):
        try:
            config = ConfigParser()
            config.add_section(m_section[3])

            config.set(m_section[3], m_keys_SRepNotifyData[0], self.lineEdit_msgId.text())
            config.set(m_section[3], m_keys_SRepNotifyData[1], self.lineEdit_accId.text())
            config.set(m_section[3], m_keys_SRepNotifyData[2], self.lineEdit_mobile.text())
            config.set(m_section[3], m_keys_SRepNotifyData[3], self.lineEdit_sendState.text())
            config.set(m_section[3], m_keys_SRepNotifyData[4], self.lineEdit_reportState.text())
            config.set(m_section[3], m_keys_SRepNotifyData[5], self.dateTimeEdit_sendDateTime.dateTime().toString())
            config.set(m_section[3], m_keys_SRepNotifyData[6], self.dateTimeEdit_reportDateTime.dateTime().toString())
            config.set(m_section[3], m_keys_SRepNotifyData[7], self.dateTimeEdit_recvReportDateTime.dateTime().toString())
            config.set(m_section[3], m_keys_SRepNotifyData[8], self.lineEdit_pk_total.text())
            config.set(m_section[3], m_keys_SRepNotifyData[9], self.lineEdit_pk_num.text())
            config.set(m_section[3], m_keys_SRepNotifyData[10],self.lineEdit_flagBits.text())

            config.set(m_section[3], m_keys_SRepNotifyData[11],self.textEdit_sendResultInfo.toPlainText())
            config.set(m_section[3], m_keys_SRepNotifyData[12],self.textEdit_repResultInfo.toPlainText())
            config.set(m_section[3], m_keys_SRepNotifyData[13],self.lineEdit_spno.text())
            config.set(m_section[3], m_keys_SRepNotifyData[14],self.lineEdit_acc_msgid.text())
            config.set(m_section[3], m_keys_SRepNotifyData[15],self.lineEdit_extnumber.text())

            with open('config/'+filename+'.ini','w',encoding='utf-8') as f:
                config.write(f)
        except:
            print('saveConfig error',filename)

    def loadConfig(self,filename):
        try:
            config = ConfigParser()
            config.read(filename, encoding='utf-8')
            if not config.has_section(m_section[3]):
                print(filename, 'do not have section', m_section[3])
                return False
            if len(config.items(m_section[3])) != len(m_keys_SRepNotifyData):
                print(filename, 'items error\n allkeys:\n', m_keys_SRepNotifyData)
                return False

            self.lineEdit_msgId.setText(config[m_section[3]][m_keys_SRepNotifyData[0]])
            self.lineEdit_accId.setText(config[m_section[3]][m_keys_SRepNotifyData[1]])
            self.lineEdit_mobile.setText(config[m_section[3]][m_keys_SRepNotifyData[2]])
            self.lineEdit_sendState.setText(config[m_section[3]][m_keys_SRepNotifyData[3]])
            self.lineEdit_reportState.setText(config[m_section[3]][m_keys_SRepNotifyData[4]])
            self.dateTimeEdit_sendDateTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[3]][m_keys_SRepNotifyData[5]]))
            self.dateTimeEdit_reportDateTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[3]][m_keys_SRepNotifyData[6]]))
            self.dateTimeEdit_recvReportDateTime.setDateTime(QtCore.QDateTime.fromString(config[m_section[3]][m_keys_SRepNotifyData[7]]))
            self.lineEdit_pk_total.setText(config[m_section[3]][m_keys_SRepNotifyData[8]])
            self.lineEdit_pk_num.setText(config[m_section[3]][m_keys_SRepNotifyData[9]])
            self.lineEdit_flagBits.setText(config[m_section[3]][m_keys_SRepNotifyData[10]])
            self.textEdit_sendResultInfo.setText(config[m_section[3]][m_keys_SRepNotifyData[11]])
            self.textEdit_repResultInfo.setText(config[m_section[3]][m_keys_SRepNotifyData[12]])
            self.lineEdit_spno.setText(config[m_section[3]][m_keys_SRepNotifyData[13]])
            self.lineEdit_acc_msgid.setText(config[m_section[3]][m_keys_SRepNotifyData[14]])
            self.lineEdit_extnumber.setText(config[m_section[3]][m_keys_SRepNotifyData[15]])
        except:
            print('loadConfig error',filename)

    def analyze(self, b):
        self.__data.fromBytes(b)
        self.__analyze()

    def __analyze(self):

        self.lineEdit_msgId.setText(str(self.__data.Data.msgId  ))
        self.lineEdit_accId.setText(str(self.__data.Data.accId))
        self.lineEdit_mobile.setText(str(self.__data.Data.mobile))
        self.lineEdit_sendState.setText(str(self.__data.Data.sendState))
        self.lineEdit_reportState.setText(str(self.__data.Data.reportState))
        self.dateTimeEdit_sendDateTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data.Data.sendDateTime)))

        self.dateTimeEdit_reportDateTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data.Data.reportDateTime)))
        self.dateTimeEdit_recvReportDateTime.setDateTime(QtCore.QDateTime.fromTime_t(Datetime_dt(self.__data.Data.recvReportDateTime)))
        self.lineEdit_pk_total.setText(str(self.__data.Data.pk_total))
        self.lineEdit_pk_num.setText(str(self.__data.Data.pk_num))
        self.lineEdit_flagBits.setText(str(self.__data.Data.flagBits))

        self.textEdit_sendResultInfo.setText(self.__data.sendResultInfo)
        self.textEdit_repResultInfo.setText(self.__data.repResultInfo)
        self.lineEdit_spno.setText(self.__data.spno)
        self.lineEdit_acc_msgid.setText(self.__data.spno)
        self.lineEdit_extnumber.setText(self.__data.extnumber)

class BMSSHisMOData(QtWidgets.QWidget,Ui_SHisMOData):
    def __init__(self):
        super(BMSSHisMOData,self).__init__()
        self.setupUi(self)
        self.__data = SHisMOData()

    def getValue(self):
        try:
            self.__data.clear()
            self.__data.Data.msgId      = int(self.lineEdit_msgId.text())
            self.__data.Data.msgType    = int(self.lineEdit_msgType.text())
            self.__data.Data.accId      = int(self.lineEdit_accId.text())
            self.__data.Data.mobile     = int(self.lineEdit_mobile.text())
            self.__data.Data.moTime     = dt_Datetime(self.dateTimeEdit.dateTime().toPyDateTime().ctime())
            self.__data.Data.resId      = int(self.lineEdit_resId.text())
            self.__data.Data.timeStamp  = int(time.time())
            self.__data.Data.dealTimes  = int(self.lineEdit_dealTimes.text())

            self.__data.write_MoContent(self.textEdit.toPlainText())
            self.__data.write_SpNum(self.lineEdit_SpNum.text())

            self.__data.write_header()

            return self.__data.Value()
        except:
            print('参数错误')

    def updatedata(self):
        try:
            self.__data.Data.msgId +=1
            self.__data.Data.timeStamp = int(time.time())
            return self.__data.Value()
        except:
            print('update error')

    def saveConfig(self,filename):
        try:
            config = ConfigParser()
            config.add_section(m_section[4])

            config.set(m_section[4], m_keys_SHisMOData[0],self.lineEdit_msgId.text())
            config.set(m_section[4], m_keys_SHisMOData[1],self.lineEdit_msgType.text())
            config.set(m_section[4], m_keys_SHisMOData[2],self.lineEdit_accId.text())
            config.set(m_section[4], m_keys_SHisMOData[3],self.lineEdit_mobile.text())
            config.set(m_section[4], m_keys_SHisMOData[4],self.dateTimeEdit.dateTime().toString())
            config.set(m_section[4], m_keys_SHisMOData[5],self.lineEdit_resId.text())
            config.set(m_section[4], m_keys_SHisMOData[6],self.lineEdit_dealTimes.text())

            config.set(m_section[4], m_keys_SHisMOData[7],self.lineEdit_SpNum.text())
            config.set(m_section[4], m_keys_SHisMOData[8],self.textEdit.toPlainText())

            with open('config/'+filename+'.ini','w',encoding='utf-8') as f:
                config.write(f)
        except:
            print('saveConfig error',filename)

    def loadConfig(self,filename):
        try:
            config = ConfigParser()
            config.read(filename, encoding='utf-8')
            if not config.has_section(m_section[4]):
                print(filename, 'do not have section', m_section[4])
                return False
            if len(config.items(m_section[4])) != len(m_keys_SHisMOData):
                print(filename, 'items error\n allkeys:\n', m_keys_SHisMOData)
                return False

            self.lineEdit_msgId.setText(config[m_section[4]][m_keys_SHisMOData[0]])
            self.lineEdit_msgType.setText(config[m_section[4]][m_keys_SHisMOData[1]])
            self.lineEdit_accId.setText(config[m_section[4]][m_keys_SHisMOData[2]])
            self.lineEdit_mobile.setText(config[m_section[4]][m_keys_SHisMOData[3]])
            self.dateTimeEdit.setDateTime(QtCore.QDateTime.fromString(config[m_section[4]][m_keys_SHisMOData[4]]))
            self.lineEdit_resId.setText(config[m_section[4]][m_keys_SHisMOData[5]])
            self.lineEdit_dealTimes.setText(config[m_section[4]][m_keys_SHisMOData[6]])
            self.lineEdit_SpNum.setText(config[m_section[4]][m_keys_SHisMOData[7]])
            self.textEdit.setText(config[m_section[4]][m_keys_SHisMOData[8]])
        except:
            print('loadConfig error',filename)

    def analyze(self, b):
        self.__data.fromBytes(b)
        self.__analyze()

    def __analyze(self):
        self.lineEdit_msgId.setText(str(self.__data.Data.msgId))
        self.lineEdit_msgType.setText(str(self.__data.Data.msgType))
        self.lineEdit_accId.setText(str(self.__data.Data.accId))
        self.lineEdit_mobile.setText(str(self.__data.Data.mobile))
        self.dateTimeEdit.setDateTime(QtCore.QDateTime.fromMSecsSinceEpoch(Datetime_dt(self.__data.moTime)))
        self.lineEdit_resId.setText(str(self.__data.Data.resId))
        self.lineEdit_dealTimes.setText(str(self.__data.Data.dealTimes))

        self.textEdit.setText(self.__data.MoContent)
        self.lineEdit_SpNum.setText(self.__data.SpNum)


class BMSMoAccBlist(QtWidgets.QWidget,Ui_MoAccBlist):
    def __init__(self):
        super(BMSMoAccBlist,self).__init__()
        self.setupUi(self)
        self.__data = MoAccBlist()

    def getValue(self):
        try:
            self.__data.clear()
            self.__data.Data.mobile = int(self.lineEdit_mobile.text())
            self.__data.Data.accid  = int(self.lineEdit_accid.text())
            self.__data.Data.level  = int(self.lineEdit_level.text())
            self.__data.Data.flag   = int(self.lineEdit_flag.text())

            self.__data.write_operator(self.lineEdit_opertor.text())
            self.__data.write_remark(  self.lineEdit_remark.text())
            self.__data.write_header()
            return self.__data.Value()
        except:
            print('参数错误')

    def updatedata(self):
        try:
            return self.__data.Value()
        except:
            print('update error')

    def saveConfig(self,filename):
        try:
            config = ConfigParser()
            config.add_section(m_section[5])

            config.set(m_section[5],m_keys_MoAccBlist[0],self.lineEdit_mobile.text())
            config.set(m_section[5],m_keys_MoAccBlist[1],self.lineEdit_accid.text())
            config.set(m_section[5],m_keys_MoAccBlist[2],self.lineEdit_level.text())
            config.set(m_section[5],m_keys_MoAccBlist[3],self.lineEdit_flag.text())
            config.set(m_section[5],m_keys_MoAccBlist[4],self.lineEdit_opertor.text())
            config.set(m_section[5],m_keys_MoAccBlist[5],self.lineEdit_remark.text())

            with open(filename,'w',encoding='utf-8') as f:
                config.write(f)
        except:
            print('saveConfig error',filename)

    def loadConfig(self,filename):
        try:
            config = ConfigParser()
            config.read(filename, encoding='utf-8')
            if not config.has_section(m_section[5]):
                print(filename, 'do not have section', m_section[5])
                return False
            if len(config.items(m_section[5])) != len(m_keys_MoAccBlist):
                print(filename, 'items error\n allkeys:\n', m_keys_MoAccBlist)
                return False

            self.lineEdit_mobile.setText(config[m_section[5]][m_keys_MoAccBlist[0]])
            self.lineEdit_accid.setText(config[m_section[5]][m_keys_MoAccBlist[1]])
            self.lineEdit_level.setText(config[m_section[5]][m_keys_MoAccBlist[2]])
            self.lineEdit_flag.setText(config[m_section[5]][m_keys_MoAccBlist[3]])
            self.lineEdit_opertor.setText(config[m_section[5]][m_keys_MoAccBlist[4]])
            self.lineEdit_remark.setText(config[m_section[5]][m_keys_MoAccBlist[5]])
        except:
            print('loadConfig error',filename)

    def analyze(self, b):
        self.__data.fromBytes(b)

    def __analyze(self):
        self.lineEdit_mobile.setText(str(self.__data.Data.mobile))
        self.lineEdit_accid.setText(str(self.__data.Data.accid))
        self.lineEdit_level.setText(str(self.__data.Data.level))
        self.lineEdit_flag.setText(str(self.__data.Data.flag))

        self.lineEdit_opertor.setText(self.__data.operator)
        self.lineEdit_remark.setText(self.__data.remark)


class BMSMonitor(QtWidgets.QWidget,Ui_Monitor):
    def __init__(self):
        super(BMSMonitor,self).__init__()
        self.setupUi(self)
        self._initUI()
        self._init()

    def _initUI(self):
        self.checkBox_SubmitMonitorMsg.setChecked(True)
        self.groupBox_submit.setEnabled(True)
        self.groupBox_ResState.setEnabled(False)
        self.groupBox_HeartBeat.setEnabled(False)
        self.groupBox_log.setEnabled(False)
        self.groupBox_Hispre.setEnabled(False)
        self.groupBox_HisCenter.setEnabled(False)
        self.groupBox_2.setEnabled(False)
        pass

    def _init(self):
        self.__data = {}
        self.__data['SubmitMonitorMsg'] = SubmitMonitorMsg()
        self.__data['HisPreDealMonitorData'] = HisPreDealMonitorData()
        self.__data['HisCenterMonitorData'] = HisCenterMonitorData()
        self.__data['SResourceState'] = SResourceState()
        self.__data['SHeartBeat'] = SHeartBeat()
        self.__data['log'] = log_struct()
        self.__data['DispatchMonitorMsg'] = DispatchMonitorMsg()

        self.get_func = {}
        self.get_func['SHeartBeat'] = self.__get_SHeartBeat
        self.get_func['log'] = self.__get_log
        self.get_func['DispatchMonitorMsg'] = self.__get_DispatchMonitorMsg
        self.get_func['SResourceState'] = self.__get_SResourceState
        self.get_func['HisCenterMonitorData'] = self.__get_HisCenterMonitorData
        self.get_func['HisPreDealMonitorData'] = self.__get_HisPreDealMonitorData
        self.get_func['SubmitMonitorMsg'] = self.__get_SubmitMonitorMsg

    def on_checkBox_SubmitMonitorMsg_stateChanged(self,a0):
        if a0 == QtCore.Qt.Checked:
            self.groupBox_submit.setEnabled(bool(a0))
            self.checkBox_DispatchMonitorMsg.setChecked(not bool(a0))
            self.checkBox_HisCenterMonitor.setChecked(not bool(a0))
            self.checkBox_HisPreDealMonitorData.setChecked(not bool(a0))
            self.checkBox_log.setChecked(not bool(a0))
            self.checkBox_SHeartBeat.setChecked(not bool(a0))
            self.checkBox_SResourceState.setChecked(not bool(a0))
        else:
            self.groupBox_submit.setEnabled(bool(a0))
            pass

    def on_checkBox_DispatchMonitorMsg_stateChanged(self,a0):
        if a0 == QtCore.Qt.Checked:
            self.groupBox_2.setEnabled(bool(a0))
            self.checkBox_SubmitMonitorMsg.setChecked(not bool(a0))
            self.checkBox_HisCenterMonitor.setChecked(not bool(a0))
            self.checkBox_HisPreDealMonitorData.setChecked(not bool(a0))
            self.checkBox_log.setChecked(not bool(a0))
            self.checkBox_SHeartBeat.setChecked(not bool(a0))
            self.checkBox_SResourceState.setChecked(not bool(a0))
        else:
            self.groupBox_2.setEnabled(bool(a0))
            pass

    def on_checkBox_HisCenterMonitor_stateChanged(self,a0):
        if a0 == QtCore.Qt.Checked:
            self.groupBox_HisCenter.setEnabled(bool(a0))
            self.checkBox_SubmitMonitorMsg.setChecked(not bool(a0))
            self.checkBox_DispatchMonitorMsg.setChecked(not bool(a0))
            self.checkBox_HisPreDealMonitorData.setChecked(not bool(a0))
            self.checkBox_log.setChecked(not bool(a0))
            self.checkBox_SHeartBeat.setChecked(not bool(a0))
            self.checkBox_SResourceState.setChecked(not bool(a0))
        else:
            self.groupBox_HisCenter.setEnabled(bool(a0))

    def on_checkBox_HisPreDealMonitorData_stateChanged(self,a0):
        if a0 == QtCore.Qt.Checked:
            self.groupBox_Hispre.setEnabled(bool(a0))
            self.checkBox_SubmitMonitorMsg.setChecked(not bool(a0))
            self.checkBox_DispatchMonitorMsg.setChecked(not bool(a0))
            self.checkBox_HisCenterMonitor.setChecked(not bool(a0))
            self.checkBox_log.setChecked(not bool(a0))
            self.checkBox_SHeartBeat.setChecked(not bool(a0))
            self.checkBox_SResourceState.setChecked(not bool(a0))
        else:
            self.groupBox_Hispre.setEnabled(bool(a0))

    def on_checkBox_log_stateChanged(self,a0):
        if a0 == QtCore.Qt.Checked:
            self.groupBox_log.setEnabled(bool(a0))
            self.checkBox_SubmitMonitorMsg.setChecked(not bool(a0))
            self.checkBox_DispatchMonitorMsg.setChecked(not bool(a0))
            self.checkBox_HisCenterMonitor.setChecked(not bool(a0))
            self.checkBox_HisPreDealMonitorData.setChecked(not bool(a0))
            self.checkBox_SHeartBeat.setChecked(not bool(a0))
            self.checkBox_SResourceState.setChecked(not bool(a0))
        else:
            self.groupBox_log.setEnabled(bool(a0))

    def on_checkBox_SHeartBeat_stateChanged(self,a0):
        if a0 == QtCore.Qt.Checked:
            self.groupBox_HeartBeat.setEnabled(bool(a0))
            self.checkBox_SubmitMonitorMsg.setChecked(not bool(a0))
            self.checkBox_DispatchMonitorMsg.setChecked(not bool(a0))
            self.checkBox_HisCenterMonitor.setChecked(not bool(a0))
            self.checkBox_HisPreDealMonitorData.setChecked(not bool(a0))
            self.checkBox_log.setChecked(not bool(a0))
            self.checkBox_SResourceState.setChecked(not bool(a0))
        else:
            self.groupBox_HeartBeat.setEnabled(bool(a0))

    def on_checkBox_SResourceState_stateChanged(self,a0):
        if a0 == QtCore.Qt.Checked:
            self.groupBox_ResState.setEnabled(bool(a0))
            self.checkBox_SubmitMonitorMsg.setChecked(not bool(a0))
            self.checkBox_DispatchMonitorMsg.setChecked(not bool(a0))
            self.checkBox_HisCenterMonitor.setChecked(not bool(a0))
            self.checkBox_HisPreDealMonitorData.setChecked(not bool(a0))
            self.checkBox_log.setChecked(not bool(a0))
            self.checkBox_SHeartBeat.setChecked(not bool(a0))
        else:
            self.groupBox_ResState.setEnabled(bool(a0))

    def getChecked(self):
        if self.checkBox_SHeartBeat.isChecked():
            return self.checkBox_SHeartBeat.text()
        elif self.checkBox_log.isChecked():
            return self.checkBox_log.text()
        elif self.checkBox_HisPreDealMonitorData.isChecked():
            return self.checkBox_HisPreDealMonitorData.text()
        elif self.checkBox_HisCenterMonitor.isChecked():
            return self.checkBox_HisCenterMonitor.text()
        elif self.checkBox_DispatchMonitorMsg.isChecked():
            return self.checkBox_DispatchMonitorMsg.text()
        elif self.checkBox_SubmitMonitorMsg.isChecked():
            return self.checkBox_SubmitMonitorMsg.text()
        elif self.checkBox_SResourceState.isChecked():
            return self.checkBox_SResourceState.text()
        else:
            return ''

    def __get_SHeartBeat(self):
        self.__data['SHeartBeat'].clear()
        self.__data['SHeartBeat'].define.timeInterval   = int(self.lineEdit_timeInterval.text())
        self.__data['SHeartBeat'].define.alarmTime      = int(time.time())
        self.__data['SHeartBeat'].define.stat           = int(self.lineEdit_stat.text())
        self.__data['SHeartBeat'].write_alarm_module(self.lineEdit_alarm_module.text())
        self.__data['SHeartBeat'].write_header()

    def __setSHeartBeat(self):
        self.lineEdit_timeInterval.setText(str(self.__data['SHeartBeat'].define.timeInterval))
        self.lineEdit_stat.setText(str(self.__data['SHeartBeat'].define.stat))
        self.lineEdit_alarm_module.setText(self.__data['SHeartBeat'].module)

    def __saveConfig_HeartBeat(self,config):
        if isinstance(config,ConfigParser):
            config.add_section(m_section[10])
            config.set(m_section[10], m_keys_HeartBeat[0], self.lineEdit_timeInterval.text())
            config.set(m_section[10], m_keys_HeartBeat[1], self.lineEdit_stat.text())
            config.set(m_section[10], m_keys_HeartBeat[2], self.lineEdit_alarm_module.text())

    def __loadConfig_HeartBeat(self,config):
        if isinstance(config,ConfigParser):
            self.lineEdit_timeInterval.setText(config[m_section[10]][m_keys_HeartBeat[0]])
            self.lineEdit_stat.setText(config[m_section[10]][m_keys_HeartBeat[1]])
            self.lineEdit_alarm_module.setText(config[m_section[10]][m_keys_HeartBeat[2]])

    def __get_log(self):
        self.__data['log'].clear()
        self.__data['log'].define.level = int(self.lineEdit_level.text())
        self.__data['log'].define.ip    = bytes2int(socket.inet_aton(self.lineEdit_ip.text()))
        self.__data['log'].define.time  = int(time.time())

        self.__data['log'].write_name(self.lineEdit_name.text())
        self.__data['log'].write_msg(self.lineEdit_msg.text())
        self.__data['log'].write_header()

    def __set_log(self):
        self.lineEdit_level.setText(str(self.__data['log'].define.level))
        self.lineEdit_ip.setText(str(socket.inet_ntoa(int2ipbyte(self.__data['log'].define.ip))))
        self.lineEdit_name.setText(self.__data['log'].names)
        self.lineEdit_msg.setText(self.__data['log'].msgs)

    def __saveConfig_log(self,config):
        if isinstance(config,ConfigParser):
            config.add_section(m_section[12])
            config.set(m_section[12], m_keys_log[0], self.lineEdit_level.text())
            config.set(m_section[12], m_keys_log[1], self.lineEdit_ip.text())
            config.set(m_section[12], m_keys_log[2], self.lineEdit_name.text())
            config.set(m_section[12], m_keys_log[3], self.lineEdit_msg.text())

    def __loadConfig_log(self,config):
        if isinstance(config,ConfigParser):
            self.lineEdit_level.setText(config[m_section[12]][m_keys_log[0]])
            self.lineEdit_ip.setText(config[m_section[12]][m_keys_log[1]])
            self.lineEdit_name.setText(config[m_section[12]][m_keys_log[2]])
            self.lineEdit_msg.setText(config[m_section[12]][m_keys_log[3]])

    def __get_DispatchMonitorMsg(self):
        self.__data['DispatchMonitorMsg'].clear()
        self.__data['DispatchMonitorMsg'].baseheader._id = int(self.lineEdit_id.text())
        self.__data['DispatchMonitorMsg'].baseheader._time = int(time.time())
        self.__data['DispatchMonitorMsg'].baseheader._period = int(self.lineEdit_period.text())
        for i in range(32):
            self.__data['DispatchMonitorMsg'].define.dispatch_states[i] = int(
                self.tableWidget_dispatch.item(i,1).text())
        for i in range(8):
            self.__data['DispatchMonitorMsg'].define.dispatch_telcom[i] = int(
                self.tableWidget_dispatch.item(i, 3).text())
        for i in range(36):
            self.__data['DispatchMonitorMsg'].define.dispatch_province[i] = int(
                self.tableWidget_dispatch.item(i, 5).text())
        self.__data['DispatchMonitorMsg'].write_header()

    def __set_DispatchMonitorMsg(self):

        pass

    def __saveConfig_DispatchMonitor(self,config):
        if isinstance(config,ConfigParser):
            config.add_section(m_section[11])
            data = dict()
            for i in range(32):
                data[i] = int(self.tableWidget_dispatch.item(i, 1).text())
            config.set(m_section[11],m_keys_DisPatchMonitor[0],str(data))
            data.clear()

            for i in range(8):
                data[i] = int(self.tableWidget_dispatch.item(i, 3).text())
            config.set(m_section[11],m_keys_DisPatchMonitor[1],str(data))
            data.clear()

            for i in range(36):
                data[i] = int(self.tableWidget_dispatch.item(i, 5).text())

            config.set(m_section[11],m_keys_DisPatchMonitor[2],str(data))

    def __loadConfig_DispatchMonitor(self,config):
        if isinstance(config,ConfigParser):
            data = config[m_section[11]][m_keys_DisPatchMonitor[0]]
            data = data[1:-1].split(',')
            for i in range(32):
                self.tableWidget_dispatch.item(i,1).setText(data[i].split(":")[1])

            data = config[m_section[11]][m_keys_DisPatchMonitor[1]]
            data = data[1: -1].split(',')

            for i in range(8):
                self.tableWidget_dispatch.item(i,3).setText(data[i].split(":")[1])

            data = config[m_section[11]][m_keys_DisPatchMonitor[2]]
            data = data[1: -1].split(',')

            for i in range(36):
                self.tableWidget_dispatch.item(i,5).setText(data[i].split(":")[1])

    def __get_SResourceState(self):
        self.__data['SResourceState'].clear()
        self.__data['SResourceState'].baseheader._id                = int(self.lineEdit_id.text())
        self.__data['SResourceState'].baseheader._time              = int(time.time())
        self.__data['SResourceState'].baseheader._period            = int(self.lineEdit_period.text())
        self.__data['SResourceState'].define.resourceId             = int(self.lineEdit_resid.text())
        self.__data['SResourceState'].define.reportTime             = int(time.time())
        self.__data['SResourceState'].define.statisticsConfig       = int(self.lineEdit_statisticsConfig.text())
        self.__data['SResourceState'].define.currentStock           = int(self.lineEdit_currentStock.text())
        self.__data['SResourceState'].define.lastStock              = int(self.lineEdit_lastStock.text())
        self.__data['SResourceState'].define.reportTimeInterval     = int(self.lineEdit_reportTimeInterval.text())
        self.__data['SResourceState'].define.submitTotal            = int(self.lineEdit_submitTotal.text())
        self.__data['SResourceState'].define.currentSubmitSuccess   = int(self.lineEdit_currentSubmitSuccess.text())
        self.__data['SResourceState'].define.currentSubmitFail      = int(self.lineEdit_currentSubmitFail.text())
        self.__data['SResourceState'].define.reportTotal            = int(self.lineEdit_reportTotal.text())
        self.__data['SResourceState'].define.currentReportSuccess   = int(self.lineEdit_currentReportSuccess.text())
        self.__data['SResourceState'].define.currentReportFail      = int(self.lineEdit_currentReportFail.text())
        self.__data['SResourceState'].define.moTotal                = int(self.lineEdit_moTotal.text())
        self.__data['SResourceState'].define.currentMoTotal         = int(self.lineEdit_currentMoTotal.text())
        self.__data['SResourceState'].define.state                  = int(self.lineEdit_state.text())

        self.__data['SResourceState'].write_header()

    def __saveConfig_Res(self,config):
        if isinstance(config,ConfigParser):
            config.add_section(m_section[9])
            config.set(m_section[9],m_keys_ResouseState[0],self.lineEdit_resid.text())
            config.set(m_section[9],m_keys_ResouseState[1],self.lineEdit_statisticsConfig.text())
            config.set(m_section[9],m_keys_ResouseState[2],self.lineEdit_currentStock.text())
            config.set(m_section[9],m_keys_ResouseState[3],self.lineEdit_lastStock.text())
            config.set(m_section[9],m_keys_ResouseState[4],self.lineEdit_reportTimeInterval.text())
            config.set(m_section[9],m_keys_ResouseState[5],self.lineEdit_submitTotal.text())
            config.set(m_section[9],m_keys_ResouseState[6],self.lineEdit_currentSubmitSuccess.text())
            config.set(m_section[9],m_keys_ResouseState[7],self.lineEdit_currentSubmitFail.text())
            config.set(m_section[9],m_keys_ResouseState[8],self.lineEdit_reportTotal.text())
            config.set(m_section[9],m_keys_ResouseState[9],self.lineEdit_currentReportSuccess.text())
            config.set(m_section[9],m_keys_ResouseState[10],self.lineEdit_currentReportFail.text())
            config.set(m_section[9],m_keys_ResouseState[11],self.lineEdit_moTotal.text())
            config.set(m_section[9],m_keys_ResouseState[12],self.lineEdit_currentMoTotal.text())
            config.set(m_section[9],m_keys_ResouseState[13],self.lineEdit_state.text())

    def __loadConfig_Res(self,config):
        if isinstance(config,ConfigParser):
            self.lineEdit_resid.setText(config[m_section[9]][m_keys_ResouseState[0]])
            self.lineEdit_statisticsConfig.setText(config[m_section[9]][m_keys_ResouseState[1]])
            self.lineEdit_currentStock.setText(config[m_section[9]][m_keys_ResouseState[2]])
            self.lineEdit_lastStock.setText(config[m_section[9]][m_keys_ResouseState[3]])
            self.lineEdit_reportTimeInterval.setText(config[m_section[9]][m_keys_ResouseState[4]])
            self.lineEdit_submitTotal.setText(config[m_section[9]][m_keys_ResouseState[5]])
            self.lineEdit_currentSubmitSuccess.setText(config[m_section[9]][m_keys_ResouseState[6]])
            self.lineEdit_currentSubmitFail.setText(config[m_section[9]][m_keys_ResouseState[7]])
            self.lineEdit_reportTotal.setText(config[m_section[9]][m_keys_ResouseState[8]])
            self.lineEdit_currentReportSuccess.setText(config[m_section[9]][m_keys_ResouseState[9]])
            self.lineEdit_currentReportFail.setText(config[m_section[9]][m_keys_ResouseState[10]])
            self.lineEdit_moTotal.setText(config[m_section[9]][m_keys_ResouseState[11]])
            self.lineEdit_currentMoTotal.setText(config[m_section[9]][m_keys_ResouseState[12]])
            self.lineEdit_state.setText(config[m_section[9]][m_keys_ResouseState[13]])

    def __get_HisCenterMonitorData(self):
        self.__data['HisCenterMonitorData'].clear()
        self.__data['HisCenterMonitorData'].baseheader._id = int(self.lineEdit_id.text())
        self.__data['HisCenterMonitorData'].baseheader._time = int(time.time())
        self.__data['HisCenterMonitorData'].baseheader._period = int(self.lineEdit_period.text())
        self.__data['HisCenterMonitorData'].define.preCnt           =int(self.lineEdit_preCnt.text())
        self.__data['HisCenterMonitorData'].define.rcvMsgCnt        =int(self.lineEdit_rcvMsgCnt.text())
        self.__data['HisCenterMonitorData'].define.directInstCnt    =int(self.lineEdit_directInstCnt.text())
        self.__data['HisCenterMonitorData'].define.repMtchCnt       =int(self.lineEdit_repMtchCnt.text())
        self.__data['HisCenterMonitorData'].define.repRtryMtchCnt   =int(self.lineEdit_repRtryMtchCnt.text())
        self.__data['HisCenterMonitorData'].define.repDismtchCnt    =int(self.lineEdit_repDismtchCnt.text())
        self.__data['HisCenterMonitorData'].define.moMsgCnt         =int(self.lineEdit_moMsgCnt.text())

        self.__data['HisCenterMonitorData'].write_header()

    def __saveConfig_HisCenter(self,config):
        if isinstance(config,ConfigParser):
            config.add_section(m_section[8])
            config.set(m_section[8],m_keys_HisCenterMonitor[0],self.lineEdit_preCnt.text())
            config.set(m_section[8],m_keys_HisCenterMonitor[1],self.lineEdit_rcvMsgCnt.text())
            config.set(m_section[8],m_keys_HisCenterMonitor[2],self.lineEdit_directInstCnt.text())
            config.set(m_section[8],m_keys_HisCenterMonitor[3],self.lineEdit_repMtchCnt.text())
            config.set(m_section[8],m_keys_HisCenterMonitor[4],self.lineEdit_repRtryMtchCnt.text())
            config.set(m_section[8],m_keys_HisCenterMonitor[5],self.lineEdit_repDismtchCnt.text())
            config.set(m_section[8],m_keys_HisCenterMonitor[6],self.lineEdit_moMsgCnt.text())

    def __loadConfig_HisCenter(self,config):
        if isinstance(config,ConfigParser):
            self.lineEdit_preCnt.setText(config[m_section[8]][m_keys_HisCenterMonitor[0]])
            self.lineEdit_rcvMsgCnt.setText(config[m_section[8]][m_keys_HisCenterMonitor[1]])
            self.lineEdit_directInstCnt.setText(config[m_section[8]][m_keys_HisCenterMonitor[2]])
            self.lineEdit_repMtchCnt.setText(config[m_section[8]][m_keys_HisCenterMonitor[3]])
            self.lineEdit_repRtryMtchCnt.setText(config[m_section[8]][m_keys_HisCenterMonitor[4]])
            self.lineEdit_repDismtchCnt.setText(config[m_section[8]][m_keys_HisCenterMonitor[5]])
            self.lineEdit_moMsgCnt.setText(config[m_section[8]][m_keys_HisCenterMonitor[6]])

    def __get_HisPreDealMonitorData(self):
        self.__data['HisPreDealMonitorData'].clear()
        self.__data['HisPreDealMonitorData'].baseheader._id = int(self.lineEdit_id.text())
        self.__data['HisPreDealMonitorData'].baseheader._time = int(time.time())
        self.__data['HisPreDealMonitorData'].baseheader._period = int(self.lineEdit_period.text())
        self.__data['HisPreDealMonitorData'].define.rcvCnt          =int(self.lineEdit_recCnt.text())
        self.__data['HisPreDealMonitorData'].define.perRcvCnt       =int(self.lineEdit_perRcvCnt.text())
        self.__data['HisPreDealMonitorData'].define.mtchCnt         =int(self.lineEdit_mtcnCnt.text())
        self.__data['HisPreDealMonitorData'].define.sndFldRsndCnt   =int(self.lineEdit_sndFldRsndCnt.text())
        self.__data['HisPreDealMonitorData'].define.repFldRsndCnt   =int(self.lineEdit_repFldRsndCnt.text())
        self.__data['HisPreDealMonitorData'].define.repTmoutRsndCnt =int(self.lineEdit_repTmoutRsndCnt.text())

        self.__data['HisPreDealMonitorData'].write_header()

    def __saveConfig_HisPre(self,config):
        if isinstance(config,ConfigParser):
            config.add_section(m_section[7])
            config.set(m_section[7],m_keys_HisPreDealMonitor[0],self.lineEdit_recCnt.text())
            config.set(m_section[7],m_keys_HisPreDealMonitor[1],self.lineEdit_perRcvCnt.text())
            config.set(m_section[7],m_keys_HisPreDealMonitor[2],self.lineEdit_mtcnCnt.text())
            config.set(m_section[7],m_keys_HisPreDealMonitor[3],self.lineEdit_sndFldRsndCnt.text())
            config.set(m_section[7],m_keys_HisPreDealMonitor[4],self.lineEdit_repFldRsndCnt.text())
            config.set(m_section[7],m_keys_HisPreDealMonitor[5],self.lineEdit_repTmoutRsndCnt.text())

    def __loadConfig_HisPre(self,config):
        if isinstance(config,ConfigParser):
            self.lineEdit_recCnt.setText(config[m_section[7]][m_keys_HisPreDealMonitor[0]])
            self.lineEdit_perRcvCnt.setText(config[m_section[7]][m_keys_HisPreDealMonitor[1]])
            self.lineEdit_mtcnCnt.setText(config[m_section[7]][m_keys_HisPreDealMonitor[2]])
            self.lineEdit_sndFldRsndCnt.setText(config[m_section[7]][m_keys_HisPreDealMonitor[3]])
            self.lineEdit_repFldRsndCnt.setText(config[m_section[7]][m_keys_HisPreDealMonitor[4]])
            self.lineEdit_repTmoutRsndCnt.setText(config[m_section[7]][m_keys_HisPreDealMonitor[5]])

    def __get_SubmitMonitorMsg(self):
        self.__data['SubmitMonitorMsg'].clear()
        self.__data['SubmitMonitorMsg'].baseheader._id      = int(self.lineEdit_id.text())
        self.__data['SubmitMonitorMsg'].baseheader._time    = int(time.time())
        self.__data['SubmitMonitorMsg'].baseheader._period  = int(self.lineEdit_period.text())

        self.__data['SubmitMonitorMsg'].define._succ        = int(self.lineEdit_succ.text())
        self.__data['SubmitMonitorMsg'].define._fail        = int(self.lineEdit_fail.text())
        self.__data['SubmitMonitorMsg'].define._succ_fee    = int(self.lineEdit_fee.text())

        self.__data['SubmitMonitorMsg'].write_header()

    def __saveConfig_SubMit(self,config):
        if isinstance(config,ConfigParser):
            config.add_section(m_section[6])
            config.set(m_section[6],m_keys_SubmitMonitor[0],self.lineEdit_succ.text())
            config.set(m_section[6],m_keys_SubmitMonitor[1],self.lineEdit_fail.text())
            config.set(m_section[6],m_keys_SubmitMonitor[2],self.lineEdit_fee.text())

    def __loadConfig_SubMit(self,config):
        if isinstance(config,ConfigParser):
            self.lineEdit_succ.setText(config[m_section[6]][m_keys_SubmitMonitor[0]])
            self.lineEdit_fail.setText(config[m_section[6]][m_keys_SubmitMonitor[1]])
            self.lineEdit_fee.setText(config[m_section[6]][m_keys_SubmitMonitor[2]])

    def __getValue(self):
        self.get_func[self.getChecked()]()

    def updatedata(self):
        return self.__data[self.getChecked()].Value()

    def getValue(self):
        try:
            self.__getValue()
        except:
            print('error')
        return self.__data[self.getChecked()].Value()
        pass


    def saveConfig(self,filename):
        try:
            config = ConfigParser()
            self.__saveConfig_DispatchMonitor(config)
            self.__saveConfig_HeartBeat(config)
            self.__saveConfig_HisCenter(config)
            self.__saveConfig_HisPre(config)
            self.__saveConfig_log(config)
            self.__saveConfig_Res(config)
            self.__saveConfig_SubMit(config)

            with open('config/'+filename+'.ini','w',encoding='utf-8') as f:
                config.write(f)
        except:
            print('saveConfig error',filename)
        pass

    def loadConfig(self,filename):
        try:
            config = ConfigParser()
            config.read(filename, encoding='utf-8')
            for s in range(6,12):
                if not config.has_section(m_section[s]):
                    print(filename, 'do not have section', m_section[s])
                    return False
                if len(config.items(m_section[s])) != len(m_key[s]):
                    print(filename, 'items error\n allkeys:\n', m_key[s])
                    return False
            self.__loadConfig_DispatchMonitor(config)
            self.__loadConfig_HeartBeat(config)
            self.__loadConfig_HisCenter(config)
            self.__loadConfig_HisPre(config)
            self.__loadConfig_log(config)
            self.__loadConfig_Res(config)

        except:
            print('load config error')

    def analyze(self,b):
        self.__data[self.getChecked()].fromBytes(b)
        pass