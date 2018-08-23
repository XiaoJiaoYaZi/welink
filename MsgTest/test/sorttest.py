
##
#时间复杂度 在刚才提到的时间频度中，n称为问题的规模，当n不断变化时，时间频度T(n)也会不断变化。
# 但有时我们想知道它变化时呈现什么规律。为此，我们引入时间复杂度概念。
# 一般情况下，算法中基本操作重复执行的次数是问题规模n的某个函数，
# 用T(n)表示，若有某个辅助函数f(n),使得当n趋近于无穷大时，T（n)/f(n)的极限值为不等于零的常数，
# 则称f(n)是T(n)的同数量级函数。记作T(n)=Ｏ(f(n)),称Ｏ(f(n)) 为算法的渐进时间复杂度，简称时间复杂度。
##
#在各种不同算法中，若算法中语句执行次数为一个常数，则时间复杂度为O(1),另外，在时间频度不相同时，时间复杂度有可能相同，
# 如T(n)=n2+3n+4与T(n)=4n2+2n+1它们的频度不同，但时间复杂度相同，都为O(n2)。 按数量级递增排列，常见的时间复杂度有：
# 常数阶O(1),对数阶O(log2n),线性阶O(n), 线性对数阶O(nlog2n),平方阶O(n2)，立方阶O(n3),...， k次方阶O(nk),指数阶O(2n)。
# 随着问题规模n的不断增大，上述时间复杂度不断增大，算法的执行效率越低。
# 2、空间复杂度 与时间复杂度类似，空间复杂度是指算法在计算机内执行时所需存储空间的度量。
# 记作: S(n)=O(f(n)) 我们一般所讨论的是除正常占用内存开销外的辅助存储单元规模。讨论方法与时间复杂度类似，不再赘述。
#（3）渐进时间复杂度评价算法时间性能 　　主要用算法时间复杂度的数量级(即算法的渐近时间复杂度)评价一个算法的时间性能


#--------------------------冒泡--------------------------
#从0位置开始，相邻的两个数比较，较大的数往后放，第一轮比较完最大的数放在最后面，比较N-1次
#从0开始比较1 ~ N-1 的数，比较次数 N-2次
#总共比较 (N-1) + (N-2) + ... +2+1 时间复杂度为 O(n2)


test = [9,8,7,6,5,4,3,2,1]

def bubbleSort(l):
    if len(l)<=2:
        return
    i = len(l)-1
    while i>0:
        for j in range(i):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
        i = i-1

bubbleSort(test)
print(test)

# --------------------------选择排序--------------------------
#遍历所有数找到最小的，放到0位置
#遍历所有数找到最小的放到1位置
#总共比较 (N-1) + (N-2) + ... +2+1 时间复杂度为 O(n2)

def selectSort(l):
    if len(l)<=2:
        return
    for i in range(len(l)):
        minindex = i
        j = i+1
        while j<len(l):
            if l[j] <l[minindex]:
                minindex = j
            j = j+1

        l[i],l[minindex] = l[minindex],l[i]

test = [9,8,7,6,5,4,3,2,1]
selectSort(test)
print(test)


#--------------------------插入排序--------------------------
#从1位置开始，比较与前面数的大小，如果小于前面的数，则交换位置，直到不再小于为止
#从2位置开始，重复这个过程，直到最后位置为止
#时间复杂度取决于数组的排序情况，当数组基本有序时候，复杂度很低，接近O（n）。
# 当数组完全无序时，每个数都要经过多次移动，复杂度趋近于O（n²）

def insertSort(l):
    if len(l)<=2:
        return
    i=1
    while i<len(l):
        j = i-1
        while j>=0:
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
            j = j-1
        i = i+1

test = [9,8,7,6,5,4,3,2,1]
insertSort(test)
print(test)


#1. 过程类似于插入排序，算是插入排序的一种优化。
#2. 首先，需要确定一个步长k，根据步长，把数组分为N/k部分，每一部分单独排序。
#3. 把步长缩短，继续排序，直到步长为1。
#4. 通过步长，减少了数组需要移动的次数，从而降低了复杂度。
#5. 所以复杂度的高低完全取决于步长的好坏，是一种特别不稳定的算法，也是一种实现简单分析困难的算法。

def shellSort(l):
    if len(l)<2:
        return


#--------------------------快速排序-------------------------------------
#随机选出一个partition值，把大于partition值的放在它右边，小于它的放在它左边。
#从partition值的左右两边分割，调用自己，开始递归。
#这里有一点优化，因为partition值在数组中可能不止一个，因此返回一个长度为2的数组，
# 代表partition的左右边界，从边界两端进行递归，更加快速。

import random


def quickSorts(l,left,right):
    if left>right:
        return
    r = int(random.random()*(right-left+1)+left)
    l[right],l[r] = l[r],l[right]
    p = partition(l,left,right)
    quickSorts(l,left,p[0]-1)
    quickSorts(l,p[1]+1,right)

def partition(l,left,right):
    less = left-1
    more = right
    while left<more:
        if l[left] < l[right]:
            less = less+1
            l[less],l[left] = l[left],l[less]
            left = left+1
        elif l[left] > l[right]:
            more = more-1
            l[more],l[left] = l[left],l[more]
        else:
            left = left+1

    l[more],l[right] = l[right],l[more]
    #less = less + 1
    value = (less+1,more)
    return value

def quickSort(l):
    if len(l)<2:
        return
    quickSorts(l,0,len(l)-1)

test = [11,23,54,89,64,85,4564,321,4584,55,3654,9,8,7,6,5,4,3,2,1]
quickSort(test)
print(test)


#--------------------------并归排序--------------------------
#需要重点掌握：
#   归并排序的优势很明显，它是稳定排序。同时相对于快排，它占用较多的空间。
#   递归的思想很重要，分治法的应用也很广泛，把大问题分解成小问题一步步解决。
#   递归过程要掌握，递归过程一定要有一个终止条件。
#   压栈的过程，空间的占用要理解。
#   同样有论文级别的算法可以把归并排序的空间省下来，知道就好。ORZ。。。 默认空间复杂度 O（n）。
#过程：
#   把数组分成两部分，分别比较大小，最后合并。
#   递归调用自己。


def merge(l,left,mid,right):
    help = [0]*(right-left+1)
    i=0
    p1=left
    p2=mid+1
    while p1<=mid and p2<=right:
        if l[p1]<l[p2]:
            help[i] = l[p1]
            i=i+1
            p1=p1+1
        else:
            help[i] = l[p2]
            i = i+1
            p2 = p2+1
    while p1<=mid:
        help[i] = l[p1]
        i = i+1
        p1 = p1+1

    while p2<=right:
        help[i] = l[p2]
        i = i+1
        p2 = p2+1

    for j in range(len(help)):
        l[left+j] = help[j]
def mergeSorts(l,left,right):
    if right==left:
        return
    mid = left+((right-left)>>1)
    mergeSorts(l,left,mid)
    mergeSorts(l,mid+1,right)
    merge(l,left,mid,right)
def mergeSort(l):
    if len(l)<2:
        return
    mergeSorts(l,0,len(l)-1)

test = [10,9,8,7,6,5,4,3,2,1]
mergeSort(test)
print(test)

#先拆分
#10,9,8,7,6,5,4,3,2,1
#10,9,8,7,6  5,4,3,2,1
#10,9,8  7,6    5,4,3    2,1
#10,9  8  7  6   5,4  4  2  1

#在组合
#9,10  8  7  6   5,4  4  2  1
#
#8,9,10  7  6   5,4  4  2  1
#
#8,9,10  6,7  5,4  4  2  1
#
#6,7,8,9,10   5,4  4  2  1
#...
#...
#6,7,8,9,10   1,2,3,4,5
#1,2,3,4,5,6,7,8,9,10



#堆排序

#先构造大根或小根树
#将第0个与最后一个交换，重新构造
#将第0个与倒数第二个交换，重新构造
#以此类推
#时间复杂度 N*logN

def makeHead(l,index,size):
    temp = l[index]
    k = 2*index+1#左节点
    while k<size:
        if k<size-1 and l[k]>l[k+1] :
            k =k+1

        if temp >l[k]:
            l[index] = l[k]
            index = k
        else:
            break
        k = 2*k+1

    l[index] = temp

def headSort(l):
    i = int(len(l)/2-1)
    while i>=0:
        makeHead(l,i,len(l))
        i = i-1

    j = len(l)-1
    while j>0:
        l[j],l[0] = l[0],l[j]
        makeHead(l,0,j)

test = [11,7,18,3,5,4,10,9]
#test = [4,6,8,5,9]
headSort(test)
print(test)