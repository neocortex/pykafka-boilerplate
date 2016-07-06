import time
from pykafka import KafkaClient

client = KafkaClient(zookeeper_hosts='localhost:2181')
topic = client.topics[b'test']
producer = topic.get_producer()

count = 0
while True:
    count += 1
    time.sleep(1)
    print('produced: {}'.format(count))
    producer.produce('msg {}'.format(count).encode())
