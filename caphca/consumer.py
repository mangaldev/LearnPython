import sys

from confluent_kafka import Consumer, KafkaError, KafkaException

# Following https://docs.confluent.io/kafka-clients/python/current/overview.html
conf = {'bootstrap.servers': 'localhost:29092',
        'group.id': "foo2",
        'enable.auto.commit': False,
        'auto.offset.reset': 'earliest'}


consumer = Consumer(conf)

def msg_process(msg):
    print(msg.value())

def basic_consume_loop(consumer, topics):
    try:
        consumer.subscribe(topics)
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                print("Couldn't find a single message...")
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    # End of partition event
                    sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                     (msg.topic(), msg.partition(), msg.offset()))
                elif msg.error():
                    raise KafkaException(msg.error())
            else:
                msg_process(msg)
    finally:
        # Close down consumer to commit final offsets.
        consumer.close()

basic_consume_loop(consumer,["random_topic_2"])
