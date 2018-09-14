

#   python调用C的dll说明

from ctypes import *

# 1/ DLL加载

dll = CDLL("*.dll")

# 入参和出参

'''
#pragma pack(1)
struct mystruct(){
    char a;
    int b;
    double c;
    char d[32];
}
#pragma pack(pop)
'''

#for python
class mystruct(Structure):
    _fields_ = [
        ('a',c_char),
        ('b',c_int),
        ('c',c_double),
        ('d',c_char * 32)
    ]
    _pack_=1

# 2 传参
#int double float等基本数据类型可以直接传递
'''
mystruct * test1(char a,int b,double c, char * d){
    mystruct * temp = new mystruct()
    temp->a = a;
    temp->b = b;
    temp->c = c;
    strcpy(temp->d,d,32);
    return temp;
}
'''

#for python
dll.test1.restype  = POINTER(mystruct)
a = 1
b = 2
c = 3.3
d = create_string_buffer('hello'.encode('gbk'),32)
myst = dll.test1(a,b,c,byref(d))

#结构体转换为字节流
data = mystruct()
b = string_at(addressof(data),sizeof(data))
#字节流转换为结构体
b = create_string_buffer(b)#先构造c类型的流对象
data1 = cast(pointer(b),POINTER(mystruct)).contents

#数组
type_int_array_10 = c_int*10#一维
type_int_array_10_10 = type_int_array_10*10 #二维
my_array = type_int_array_10_10()
my_array[0][0] = 1

#回调函数

CMPFUNC = CFUNCTYPE(c_int,c_int)
def pFunc(a,b):
    return a+b

dll.CallBack(CMPFUNC(pFunc))
