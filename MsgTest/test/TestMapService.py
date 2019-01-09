from ctypes import *
import time

def Pack(ctype_instance):
    return string_at(addressof(ctype_instance),sizeof(ctype_instance))

def UnPack(ctype,buf):
    cstring = create_string_buffer(buf)
    return cast(pointer(cstring),POINTER(ctype)).contents


class SResIdPrdExId(Structure):
    _fields_ = [
        ('nIndex',c_int64),
        ('nForbidArea',c_int64),
        ('bTelecomSet',c_char),
        ('bModifyFlag',c_char),
        ('nResNetType',c_int)
    ]
    _pack_ = 1

    def __len__(self):
        return sizeof(self)

    def __str__(self):
        return '{},{},{},{},{}'.format(self.nIndex,self.nForbidArea,self.bTelecomSet,self.bModifyFlag,self.nResNetType)


class SSMProduct(Structure):
    _fields_ = [
        ('productId',               c_int),
        ('productName',             c_char*51),
        ('defaultProductExtendId',  c_int),
        ('lastTime',                c_int64)
    ]
    _pack_ = 1

    def __str__(self):
        return '{},{},{},{}'.format(self.productId,self.productName.decode('gbk'),self.defaultProductExtendId,self.lastTime)



##############################test productEx###################################################
# import time
# UMCProductEx = cdll.LoadLibrary('D:\\svn\\public\\PubProject\\PublicProMS\\x64\\Debug\\ProductEx.dll')
# ret = UMCProductEx.PrdEx_Init(None)
# data = SSMProduct()
# start = time.process_time()*1000
# ret = UMCProductEx.Prd_Find(1002300,byref(data))
# print('use:{}ms'.format(time.process_time()*1000-start))
# print(ret,data)
# UMCProductEx.PrdEx_UnInit()
#
# print(vars(SSMProduct))
################################################################################################

class SAccountIndex(Structure):
    _fields_ = [
        ('h_content',c_int64),
        ('l_content',c_int64)
    ]
    _pack_ = 1

class SSMAccount(Structure):
    _fields_ = [
    ('accountId',c_char*31),
    ('employeeId',c_int),
    ('superAccountId',c_char*31),
    ('superIdList',c_char*101),
    ('password',c_char*51),
    ('onlyCode',c_char*11),
    ('accountState',c_ubyte),
    ('isSubAccount',c_bool),
    ('clientType',c_ubyte),
    ('accountSign',c_char*31),
    ('submitMode',c_ubyte),
    ('SPNumber',c_char*31),
    ('uploadUrl',c_char*201),
    ('isIpForbidden',c_bool),
    ('ipList',c_char*321),
    ('receiveUrl',c_char*201),
    ('signedCompanyId',c_int),
    ('lastTime',c_int64),
    ('Id',c_int),
    ('availableByte',c_char),
    ('privateKey',c_char*33),
    ('index',SAccountIndex),
    ('propertyComponent',c_int),
    ('dayMobileLimit',c_ubyte),
    ('dayContentLimit',c_int),
    ('forceCheckMaxNo',c_int),
    ('timePeriodMobileLimit',c_int),
    ('timePeriodContentLimit',c_int),
    ('preventComplaintsMobileDayLimitCount',c_int),
    ('rptMqid',c_int),
    ('moMqid',c_int),
    ('data',c_char*15)
    ]

    _pack_ = 1

    def __str__(self):
        return '\n'.join([
        ])

##############################test Account###################################################
UMCAccount = cdll.LoadLibrary('D:\\svn\\public\\PubProject\\PublicProMS\\x64\\Debug\\Account.dll')
ret = UMCAccount.Acc_UpdateInitMaster(None)
data = SSMAccount()
time.sleep(1)
ret = UMCAccount.Acc_Find('0000001'.encode('utf-8'),byref(data))

print('ret:',ret)
UMCAccount.Acc_UnInit()

#############################################################################################

































