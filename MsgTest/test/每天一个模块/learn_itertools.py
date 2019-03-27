from itertools import *

# 无限迭代器
#创建一个迭代器，生成从 n 开始的连续整数，如果忽略 n，则从 0 开始计算

for i in count(100,1):
    print(i)
    if i>200:
        break

#把传入的一个序列无限重复下去

n = 0
for i in cycle('123'):
    if n>4:
        break
    print(i)
    n+=1

#创建一个迭代器，重复生成 object，times（如果已提供）指定重复计数，如果未提供 times，将无止尽返回该对象

for i in repeat('123',2):
    print(i)

#但仅生成 sequence 中 function(item) 为 False 的项
for i in filterfalse(lambda x:x>5,[2,3,4,5,6]):
    print(i)


#与 zip 类似，但不同的是它会把最长的 iter 迭代完才结束，其他 iter 如果有缺失值则用 fillvalue 填充
for i in zip_longest('abcd','12',fillvalue='-'):
    print(i)

#对序列 sequence 的每个元素作为 function 的参数列表执行，即 function(*item), 返回执行结果的迭代器。只有当 iterable 生成的项适用于这种调用函数的方式时，此函数才有效
seq = [(1,2),(3,4)]
for i in starmap(lambda x,y:(x,y,x*y),seq):
    print(i)


#创建一个迭代器，只要函数 predicate(item) 为 True，就丢弃 iterable 中的项，如果 predicate 返回 False，就会生成 iterable 中的项和所有后续项。即在条件为false之后的第一次, 返回迭代器中剩下来的项
seq = [ -1, 0, 1, 2, 3, 4, 1, -2]
for i in dropwhile(lambda x:x<1,seq):
    print(i)


#与 dropwhile 相反。创建一个迭代器，生成 iterable 中 predicate(item) 为 True 的项，只要 predicate 计算为 False，迭代就会立即停止
for i in takewhile(lambda x:x<1,seq):
    print(i)


#把一组迭代对象串联起来，形成一个更大的迭代器
for i in chain('123','456'):
    print(i)


#创建一个迭代器，生成多个迭代器集合的笛卡尔积，repeat 参数用于指定重复生成序列的次数
for i in product((1,2),('a','b'),repeat=3):
    print(i)


#返回 iterable 中任意取 r 个元素做排列的元组的迭代器，如果不指定 r，那么序列的长度与 iterable 中的项目数量相同
for i in permutations('abc',r=2):
    print(i)

#与 permutations 类似，但组合不分顺序，即如果 iterable 为 "abc"，r 为 2 时，ab 和 ba 则视为重复，此时只放回 ab.
for i in combinations('abc',2):
    print(i)

#与 combinations 类似，但允许重复值，即如果 iterable 为 "abc"，r 为 2 时，会多出 aa, bb, cc
for i in combinations_with_replacement('abc',2):
    print(i)

#相当于 bool 选取，只有当 selectors 对应位置的元素为 true 时，才保留 data 中相应位置的元素，否则去除
for i in compress('abcdef',[1,0,1]):
    print(i)

#对 iterable 中的元素进行分组。keyfunc 是分组函数，用于对 iterable 的连续项进行分组，如果不指定，则默认对 iterable 中的连续相同项进行分组，返回一个 (key, sub-iterator) 的迭代器
for key,value_iter in groupby('aaabbccaadd'):
    print(key,list(value_iter))

data = ['a','bb','cc','ddd','f']
for key,value_iter in groupby(data,len):
    print(key,list(value_iter))

#切片选择，start 是开始索引，stop 是结束索引，step 是步长，start 和 step 可选
print(list(islice(count(),10)))
print(list(islice(count(),3,10,2)))

#从 iterable 创建 n 个独立的迭代器
print(tee('abcdef'))











