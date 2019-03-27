import asyncio

async def foo():
    print('这是协程')
    return '返回值'

# region 协程调用协程
async def main():
    print('主协程')
    print('等待1完成')
    ret1 = await result1()
    print(ret1)
    print("等待result2协程运行")
    ret2 = await result2(ret1)
    print(ret2)
    return (ret1, ret2)

async def result1():
    print("这是result1协程")
    return "result1"

async def result2(arg):
    print("这是result2协程")
    return "result2接收了一个参数,{}".format(arg)
# endregion

# region 协程调用普通函数
import functools

def callback(args,loop,kwargs = 'default'):
    print('普通函数做为回调函数,获取参数:{},{},time:{}'.format(args,kwargs,loop.time()))

# <editor-fold desc="call_soon">
async def main1(loop):
    print('注册callback')
    loop.call_soon(callback,1)
    wrapped = functools.partial(callback,kwargs = 'not default')
    loop.call_soon(wrapped,2)
    await asyncio.sleep(1)
# </editor-fold>

# <editor-fold desc="call_later">
async def main2(loop):
    print('注册callback')
    loop.call_later(1,callback,1)
    wrapped = functools.partial(callback,kwargs = 'not default')
    loop.call_later(0.5,wrapped,2)
    await asyncio.sleep(1)
# </editor-fold>


# <editor-fold desc="call_at">
async def main3(loop):
    now = loop.time()
    print('当前内部时间:{}'.format(now))
    print('注册callback')
    loop.call_at(now+0.1,callback,1,loop)
    wrapped = functools.partial(callback,kwargs = 'not default')
    loop.call_at(now+0.2,wrapped,2,loop)
    await asyncio.sleep(1)
# </editor-fold>
# endregion

#Future
# region Future
def future_foo(future,result):
    print("此时future的状态:{}".format(future))
    print("设置future的结果:{}".format(result))
    future.set_result(result)
    print("此时future的状态:{}".format(future))

async def future_main(loop):
    all_done = asyncio.Future()
    print('调用函数获取future对象')
    loop.call_soon(future_foo,all_done,'the result')

    result = await all_done
    print('获取future结果：{}'.format(result))

def future_callback(future,n):
    print('{}:future done:{}'.format(n,future.result()))

async def register_callbacks(all_done:asyncio.Future):
    print('注册callback到future对象')
    all_done.add_done_callback(functools.partial(future_callback,n=1))
    all_done.add_done_callback(functools.partial(future_callback, n=2))

async def future_main1():
    all_done = asyncio.Future()
    await register_callbacks(all_done)
    print('设置future结果')
    all_done.set_result('the result')
# endregion



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # <editor-fold desc="loop">
    try:
        print('协程开始运行')
        _print = future_main1()
        print('进入事件循环')
        result = loop.run_until_complete(_print)
        print('协程返回值:{}'.format(result))
    finally:
        print('关闭协程事件')
        loop.close()
    # </editor-fold>
