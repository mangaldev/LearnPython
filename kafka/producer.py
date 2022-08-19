from kafka import KafkaProducer

# # Follwing https://kafka-python.readthedocs.io/en/master/
producer = KafkaProducer(bootstrap_servers='localhost:29092')
# Async Send
for _ in range(100):
    producer.send('learning_kafka_first_topic', b'Some Random Binary Text')

# Synchronous Send
future = producer.send('beaconfire_topic_9', b'Wait until not send')
future.get(timeout=5)


producer.send('hello', key=b"foo", value=b"bar")

producer.flush()