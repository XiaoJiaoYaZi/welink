from PyQt5 import QtWidgets,QtCore
import time
import socket
import struct
from ctypes import *
from configparser import ConfigParser
from UI_SCloudMsg import Ui_CloudMsg
from PlatformPublicDefine import SCloudMessage
from BMSMessage import dt_time,time_dt,dt_Datetime,Datetime_dt,bytes2int,int2ipbyte

class CloudMsg(QtWidgets.QWidget,Ui_CloudMsg):
    def __init__(self):
        super(CloudMsg,self).__init__()
        self.setupUi(self)
        self.__data = SCloudMessage()

    def getValue(self):
        try:
            #head
            self.__data.FixHead.Priority = int(self.Priority.text())
            self.__data.FixHead.MsgId = int(self.MsgId.text())
            self.__data.FixHead.ProductExtendId = int(self.ProductExtendId.text())
            self.__data.FixHead.RealProductExtendId = int(self.RealProductExtendId.text())
            self.__data.FixHead.StartSendDateTime = dt_Datetime(self.StartSendDateTime.dateTime().toPyDateTime().ctime())
            self.__data.FixHead.EndSendDateTime = dt_Datetime(self.EndSendDateTime.dateTime().toPyDateTime().ctime())
            self.__data.FixHead.StartSendTime = dt_Datetime(self.StartSendTime.dateTime().toPyDateTime().ctime())
            self.__data.FixHead.EndSendTime = dt_Datetime(self.EndSendTime.dateTime().toPyDateTime().ctime())
            self.__data.FixHead.ChargeQuantity = int(self.ChargeQuantity.text())
            self.__data.FixHead.MsgState = self.MsgState.currentIndex()+1
            self.__data.FixHead.MsgType = self.MsgType.currentIndex()+1
            self.__data.FixHead.CommitTime = dt_Datetime(self.CommitTime.dateTime().toPyDateTime().ctime())
            self.__data.FixHead.Package = int(self.Package.text())
            self.__data.FixHead.MobilesContentLen = int(self.MobilesContentLen.text())
            self.__data.FixHead.MsgContentLen = int(self.MsgContentLen.text())
            self.__data.FixHead.MobilesCount = int(self.MobilesCount.text())
            self.__data.FixHead.DispatchTimes = int(self.DispatchTimes.text())
            self.__data.FixHead.Telcom = self.Telcom.currentIndex()
            self.__data.FixHead.ProvinceId = int(self.ProvinceId.text())
            self.__data.FixHead.CityId = int(self.CityId.text())
            self.__data.FixHead.TPCBChecked = int(self.TPCBChecked.text())
            self.__data.FixHead.SendedTimes = int(self.SendedTimes.text())
            self.__data.FixHead.DispatchFailedState = int(self.DispatchFailedState.text())
            self.__data.FixHead.SubmitType = int(self.SubmitType.text())
            self.__data.FixHead.CloudMsgTemplateID = int(self.Cl)
            self.__data.FixHead.CommitIp = bytes2int(socket.inet_aton(self.CommitIp_2))
            self.__data.FixHead.m_old_struct = int(self.m_old_struct.text())
        except Exception as e:
            print(e)
            print('getVlue error')
