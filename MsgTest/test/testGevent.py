import gevent
from gevent.lock import Semaphore
from gevent.pool import *

sem = Semaphore(1)

def f1():
    for i in range(5):
        sem.acquire()
        print('this is {}'.format(i))
        sem.release()
        #gevent.sleep(1)

def f2():
    for i in range(5):
        sem.acquire()
        print('that is {}'.format(i))
        sem.release()

t1 = gevent.spawn(f1)
t2 = gevent.spawn(f2)
gevent.joinall([t1,t2])


import asyncio
import aiofiles


async def Read(f):
    return f.read(10)

async def openfile(filename):
    print("open file {}".format(filename))
    async with aiofiles.open(filename,'r') as f:
        a =  await f.read(500)
        print(a)

async def wait_openfile(filename):
    a = await openfile(filename)
    print("open file ok",a)

async  def main():
    await asyncio.wait([wait_openfile('ascii.txt'),wait_openfile('ascii.txt')])


loop = asyncio.get_event_loop()
loop.run_until_complete(main())