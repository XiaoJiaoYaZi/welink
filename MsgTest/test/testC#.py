import clr
import sys

sys.path.append('D:\\svn\\zg\\DirectAD\\LabSys\\CSharpUtils\\Debug')

clr.FindAssembly('D:\\svn\\zg\\DirectAD\\LabSys\\CSharpUtils\\Debug\\CSharpUtils.dll')

clr.AddReference('D:\\svn\\zg\\DirectAD\\LabSys\\CSharpUtils\\Debug\\CSharpUtils.dll')

from CSharpUtils.ConvertUtils import  *
from CSharpUtils.HttpUtil import *

b = BytesConvert()
print(b)
print(b.BytesToInt(b'\x01\x00'))

i = IpUtil()
print(i.Ip_2_Int('127.0.0.1'))
print(hex(2130706434))
print(i.Int_2_Ip(2130706434))