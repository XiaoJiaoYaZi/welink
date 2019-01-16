import time
import datetime
from PyQt5 import QtCore
import socket

oneday = 24*60*60

def dt_time(time_str = None):
    seconds = time_str.hour*3600 + time_str.minute*60 + time_str.second
    return seconds/oneday
def time_dt(value):
    return time.strftime("%H:%M:%S", time.gmtime(value*oneday))

def dt_Datetime(time_str):
    return time.mktime(time.strptime(time_str))/oneday+25569.333333333332

def dt_Datetime_1970_local(value):
    return datetime.datetime.fromtimestamp(value).strftime('%Y-%m-%d %H:%M:%S:%f')

def dt_Datetime_utc(value):
    return datetime.datetime.utcfromtimestamp(value).strftime('%Y-%m-%d %H:%M:%S:%f')

def Datetime_dt(value):
    return QtCore.QDateTime.fromTime_t((value-25569.333333333332)*3600*24).toString("yyyy-MM-dd hh:mm:ss")

def Datetime_dt_1970(value):
    return QtCore.QDateTime.fromTime_t(value).toString("yyyy-MM-dd hh:mm:ss")

def ip_int2str(n:int):
    if n>0xffffffff:
        raise ValueError('n out of range')
    return socket.inet_ntoa(n.to_bytes(4,'little'))