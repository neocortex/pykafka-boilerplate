from pykafka import KafkaClient
from pykafka.common import OffsetType

if __name__ == '__main__':
    client = KafkaClient(zookeeper_hosts='localhost:2181')
    topic = client.topics[b'test']

    consumer = topic.get_balanced_consumer(
        consumer_group=b'group',
        zookeeper_connect='localhost:2181',
        auto_commit_enable=True,
        auto_commit_interval_ms=2000,
        reset_offset_on_start=False,
        auto_offset_reset=OffsetType.EARLIEST)

    while True:
        message = consumer.consume()
        print('partition_id: {}, offset: {}, value: {}'.format(
            message.partition_id,
            message.offset,
            message.value))
