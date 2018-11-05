from pykafka import KafkaClient,Cluster,handlers,simpleconsumer,Topic,broker,ManagedBalancedConsumer
from pykafka.protocol import PartitionOffsetFetchRequest

handler = handlers.ThreadingHandler()
broke = broker.Broker(1,'10.1.63.126',9092,handler,1000,1000)
broke.connect()
groups = broke.list_groups()#只能查询到活着的消费者的描述信息
res = broke.describe_groups([b'10.1.120.111.dispatchcenter',])




cluster = Cluster(hosts='10.1.63.126:9092,10.1.63.127:9092,10.1.63.128:9092',
                  handler=handler,zookeeper_hosts='10.1.63.126:2181,10.1.63.127:2181,10.1.63.128:2181')
print(cluster.get_group_coordinator(b'10.1.120.111.msgstatistics'))
res = cluster.brokers[1].describe_groups([b'10.1.120.111.dispatchcenter',])
group_descriptions = cluster.get_managed_group_descriptions()
descrip = cluster.get_managed_group_descriptions()
topic = cluster.topics[b'10.1.120.111.dispatchcenter']
cluster._get_metadata([b'10.1.120.111.dispatchcenter',])


# client = KafkaClient('10.1.63.126:9092,10.1.63.127:9092,10.1.63.128:9092')
# topic = client.topics[b'10.1.120.111.msgstatistics']
# #topic.get_simplr_consumer('10.1.120.111.msgstatistics',)
# consumer = simpleconsumer.SimpleConsumer(topic,cluster=cluster,consumer_group='10.1.120.111.msgstatistics')
#
#
# offsets = consumer.fetch_offsets()
# print(offsets)

