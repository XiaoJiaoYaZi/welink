
import win32com.client

import os



# qinfo =win32com.client.Dispatch("MSMQ.MSMQQueueInfo")
# computer_name = os.getenv('COMPUTERNAME')
#
# qinfo.FormatName ="direct=os:."+"\\PRIVATE$\\test"
#
# queue =qinfo.Open(1 ,0)   # Open a ref to queue to read(1)
#
# msg =queue.Receive()
#
# print ("Label:" ,msg.Label)
#
# print ("Body :" ,msg.Body)
#
# queue.Close()

import sys
def test():
    print("module:{} func:{} line:{} error".format(__file__,sys._getframe().f_code.co_name,sys._getframe().f_lineno))
test()


from ctypes import *

def callFunc(body,len):
    print('python call back')
    s = string_at(body,len)
    print(s)
    print(body,len)


def testmsmq():
    dll = CDLL('D:\\users\\welink\\documents\\visual studio 2015\\Projects\\Testkafka\\x64\\Debug\\MSMQMoudle.dll')
    ret = dll.API_CreateSender('direct=OS:.\\private$\\receiveMsg'.encode('gbk'))
    print(ret)
    #ret = dll.API_Send('hello'.encode('gbk')+bytes(10),len('hello')+10)
    print(ret)

    ret = dll.API_CreateReceiver('direct=OS:.\\private$\\receiveMsg'.encode('gbk'))
    print(ret)


    CMPFUNC = CFUNCTYPE(None,c_void_p,c_int64)
    cmp_func = CMPFUNC(callFunc)
    #ret = dll.API_StartReceive(cmp_func)

    buf = create_string_buffer(100)
    size = c_int64(sizeof(buf))
    #size.value = sizeof(buf)
    ret = dll.API_RecvOne(pointer(buf),byref(size))
    print(buf.value)
    print(size.value)
    print(ret)
    ret = dll.API_CloseSender()
    print('API_CloseSender:',ret)
    ret = dll.API_CloseReceiver()
    print('API_CloseReceiver:',ret)
    input('---')



testmsmq()