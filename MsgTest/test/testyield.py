
def consumer():
    r = ''
    while True:
        n = yield r#停留在此处，n接收send的值，r为send的返回值
        if not n:
            return ''
        print('[consumer] consuming %s...' % n)
        r = '200 ok'

def producer(c):
    c.send(None)#激活生成器
    n = 0
    while n<5:
        n = n+1
        print('[producer] producing %s...' %n)
        r = c.send(n)
        print('[producer] conuming return:%s' % r)

    c.close()

def fib(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n = n+1
    return 'done'

def htest():
    i=1
    while i<4:
        n = yield i
        if i == 3:
            return 100
        i += 1

def itest():
    val = yield from htest()
    print(val)



if __name__ == '__main__':
    n = fib(10)
    for n1 in n:
        print(n1)

    c = consumer()
    producer(c)

    t = itest()
    t.send(None)
    j =0
    while j<3:
        j +=1
        try:
            t.send(j)
        except StopIteration as e:
            print(e)