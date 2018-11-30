from collections import ChainMap,Counter,deque,defaultdict
import os,argparse

dict1 = {'a':1,'b':2}
dict2 = {'a':3,'c':2}

#拼接字典
chain_dict = ChainMap(dict1,dict2,dict())
print(chain_dict['a'])
dict1.update(dict2)#deep copy
print(dict1)
dict2['c'] = 6
print(dict1)
print(chain_dict)


#统计出现次数
cnt = Counter('abcdeabcdabcaba')
print(cnt)
print(cnt.most_common(1))
print('.'.join(sorted(cnt.elements())))
print(cnt.items())
for elem in 'shazi':
    cnt[elem] +=1
print(cnt)

cnt1 = Counter('adadsfas')
cnt.update(cnt1)#deep copy
print(cnt)
cnt1['a']+=1
print(cnt)


#线程安全的双端队列
d = deque('123')
for i in d:
    print(i)

d.append('4')
d.appendleft('0')
d.insert(1,'1')
print(d)
print(d.pop())

import queue
q = queue.Queue()#非线程安全的双端队列


#defaultdict 提供可指定value的dict

d = defaultdict(list)
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
for k,v in s:
    d[k].append(v)
print(d)


#nametuple



#orderedDoct
from collections import OrderedDict
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
d = OrderedDict(sorted(d.items(),key = lambda t:t[0]))
print(d)
d = OrderedDict(sorted(d.items(),key = lambda t:t[1]))
print(d)
d = OrderedDict(sorted(d.items(),key = lambda t:len(t[0])))
print(d)


from collections import UserDict,UserString

import functools


@functools.lru_cache(maxsize=3)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print([fib(n) for n in range(4)])
print(fib.cache_info())


#泛型方法
@functools.singledispatch
def fun(arg,verbose = False):
    if verbose:
        print('Let me just say:',end=' ')
    print(arg)
#重载方法
@fun.register(int)
def _(arg,verbose = False):
    if verbose:
        print('accept int param:',end=' ')
    print(arg)

fun('123',True)
fun(123,True)


import selectors
import socket

sel = selectors.DefaultSelector()




