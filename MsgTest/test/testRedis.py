import random

import redis
from redis.sentinel import Sentinel


from rediscluster import StrictRedisCluster
import sys
map_key = 'test_key'
#max_value = 1902160000000000000
max_value = 19029900000000000000
def redis_cluster():
    redis_nodes =  [{'host':'10.1.63.126','port':8001,'password':123456},
                    {'host':'10.1.63.127','port':8002,'password':123456},
                    {'host':'10.1.63.128','port':8003,'password':123456}
                   ]

    redisconn = StrictRedisCluster(startup_nodes=redis_nodes)

    cursor_cur = 0
    #cursor_cur = redisconn.hscan(map_key, cursor_cur, '*', 1000)
    keys = []
    while True:
        cursor_cur,result = redisconn.hscan(map_key,cursor_cur,'*',1000)
        for key in result.keys():
            value = int(key.decode('utf-8'))
            if value < max_value:
                keys.append(key)
        if cursor_cur == 0:
            break

    redisconn.hdel(map_key,*tuple(keys))
    #print(ret)
redis_cluster()

def makedata():
    redis_nodes =  [{'host':'10.1.63.126','port':8001,'password':123456},
                    {'host':'10.1.63.127','port':8002,'password':123456},
                    {'host':'10.1.63.128','port':8003,'password':123456}
                   ]

    redisconn = StrictRedisCluster(startup_nodes=redis_nodes)


    n = 0
    for i in range(80000):
        date = random.randint(1,17)
        value = '1902'+str(date)+ '00000' + '%06d' % (i,) + '01'
        if 0 == redisconn.hset(map_key,value,'2019-02-28 00:00:00 1'):
            print('hset error')
        if i%10000 == 0:
            print(i)
#makedata()