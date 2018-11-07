from pykafka import KafkaClient,Cluster,handlers,simpleconsumer,Topic,broker,ManagedBalancedConsumer
from pykafka.protocol import PartitionOffsetFetchRequest

handler = handlers.ThreadingHandler()
# broke = broker.Broker(1,'10.1.63.126',9092,handler,1000,1000)
# broke.connect()
# groups = broke.list_groups()#只能查询到活着的消费者的描述信息
# res = broke.describe_groups([b'0.0.0.0.bmsaccount',])
# res = broke.fetch_consumer_group_offsets(b'0.0.0.0.bmsaccount',[PartitionOffsetFetchRequest(b'0.0.0.0.bmsaccount',0)])



cluster = Cluster(hosts='10.1.63.126:9092,10.1.63.127:9092,10.1.63.128:9092',
                  handler=handler)
topic = cluster.topics[b'10.1.120.111.DispatchCenterSave'.lower()]
#topic.get_simplr_consumer('10.1.120.111.msgstatistics',)
consumer = simpleconsumer.SimpleConsumer(topic,cluster=cluster,consumer_group='1.DispatchCenterSave',auto_start=False,
                                         auto_commit_enable=False,)
offsets = consumer.fetch_offsets()
input()

broke = cluster.get_group_coordinator(b'10.1.120.111.msgstatistics')
broke.fetch_consumer_group_offsets(b'10.1.120.111.msgstatistics',[PartitionOffsetFetchRequest(b'10.1.120.111.msgstatistics',0)])
#res = cluster.brokers[1].describe_groups([b'10.1.120.111.dispatchcenter',])


group_descriptions = cluster.get_managed_group_descriptions()
descrip = cluster.get_managed_group_descriptions()
offsets = cluster.get_group_coordinator(b'10.1.120.111.dispatchcenter')
topics = cluster
topic = cluster.topics[b'10.1.120.111.dispatchcenter']
cluster._get_metadata([b'10.1.120.111.dispatchcenter',])

cluster.topics
client = KafkaClient('10.1.63.126:9092,10.1.63.127:9092,10.1.63.128:9092')
topic = client.topics[b'10.1.120.111.msgstatistics']
#topic.get_simplr_consumer('10.1.120.111.msgstatistics',)
consumer = simpleconsumer.SimpleConsumer(topic,cluster=cluster,consumer_group='10.1.120.111.msgstatistics')


offsets = consumer.fetch_offsets()
print(offsets)

