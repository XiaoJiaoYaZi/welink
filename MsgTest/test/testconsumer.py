from collections import namedtuple

from kafka import KafkaConsumer, TopicPartition
import time
import threading
from kafka.errors import *

def cusumer():
    start = time.time()
    n = 0
    _consumer = KafkaConsumer('4.1.1.1.python-test', group_id = 'test1',bootstrap_servers='192.168.18.134:9092', consumer_timeout_ms=1000)
    print(_consumer.partitions_for_topic('4.1.1.1.python-test'))
    #TopicPartition('4.1.1.1.python-test','0')
    #a = namedtuple("_TopicPartition",["_4.1.1.1.python-test", "_0"])
    offset = _consumer.committed(TopicPartition(topic = '4.1.1.1.python-test',partition = 0))
    #_consumer.seek_to_beginning()
    #_consumer.seek_to_beginning(TopicPartition(topic = '4.1.1.1.python-test',partition = 0))
    #_consumer.assign(TopicPartition(topic = '4.1.1.1.python-test',partition = 0))
    print(_consumer.assignment())
    print(_consumer.subscription())
    print(_consumer.beginning_offsets(TopicPartition(topic = '4.1.1.1.python-test',partition = 0)))
    #_consumer.seek(TopicPartition(topic = '4.1.1.1.python-test',partition = 0),offset-1)
    #print(_consumer.position(TopicPartition(topic = '4.1.1.1.python-test',partition = 0)))
    #_consumer.commit()
    return
    while 1:
        try:
            for message in _consumer:
                #yield message
                print(message.value)
                n = n+1
                stop = time.time()
                if stop-start>1:
                    print(n/(stop-start))
                    start = time.time()
                    n=0
            #print('time out')
        except KafkaTimeoutError as e:
            print(e)
        except KafkaError as e:
            print(e)
        finally:
            pass




t1 = threading.Thread(target=cusumer)
t1.start()
# time.sleep(5)
# _consumer._set_consumer_timeout()
# _consumer.close()
