

#KMP算法详解
#参考地址
#https://www.cnblogs.com/lojunren/p/3865234.html


def getNext(pattern:list,next:list,pattern_len:int):
    i = 0
    j = -1
    next[0] = -1
    while i<pattern_len - 1:
        if j==-1 or pattern[i]==pattern[j]:
            i = i+1
            j = j+1
            if pattern[i]!=pattern[j]:
                next[i] = j
            else:
                next[i] = next[j]
        else:
            j = next[j]

def match(src,pattern):
    src_index = 0
    pattern_index = 0
    src_len = len(src)
    pattern_len = len(pattern)

    _next = [0]*pattern_len
    getNext(pattern,_next,pattern_len)
    print(_next)
    while pattern_index < pattern_len and src_index < src_len:
        if pattern_index == -1 or src[src_index] == pattern[pattern_index]:
            src_index = src_index + 1
            pattern_index = pattern_index + 1
        else:
            pattern_index = _next[pattern_index]

    if pattern_index >= pattern_len:
        return True
    else:
        return False


# region Description
class Test(object):
    a = None

    @classmethod
    def func(cls):
        pass
# endregion


if __name__ == '__main__':
    src  = "BBC AAAABCDAB ABCDABCDABDE"
    pattern = "AAAAB"
    res = match(src,pattern)
    print(res)
    import pandas as np
    with open('data.csv','w') as f:
        data = np.DataFrame([['12','123'],['23',23],['123','123'],['123','123']]).T
        print(data)
        data.to_csv(f, mode='a', header=False, index=False)