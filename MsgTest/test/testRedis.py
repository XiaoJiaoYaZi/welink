import redis
from redis.sentinel import Sentinel


from rediscluster import StrictRedisCluster
import sys

def redis_cluster():
    redis_nodes =  [{'host':'10.1.120.112','port':8001,'password':123456},
                    {'host':'10.1.120.111','port':8002,'password':123456},
                    {'host':'10.1.120.85', 'port':8003,'password':123456},
                    {'host':'10.1.120.112','port':9001,'password':123456},
                    {'host':'10.1.120.111','port':9002,'password':123456},
                    {'host':'10.1.120.85', 'port':9003,'password':123456},
                    {'host':'10.1.120.112','port':9101,'password':123456},
                    {'host':'10.1.120.111','port': 9102,'password':123456},
                    {'host':'10.1.120.85', 'port': 9103,'password':123456}
                   ]

    redisconn = StrictRedisCluster(startup_nodes=redis_nodes,password = 123456)


    redisconn.hset("test1","hello",'你好')
    print(redisconn.hget('test1','hello').decode('utf-8'))

redis_cluster()