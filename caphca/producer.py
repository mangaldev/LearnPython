from kafka import KafkaProducer

# # Follwing https://kafka-python.readthedocs.io/en/master/
producer = KafkaProducer(bootstrap_servers='localhost:29092')
# Asynchronus(non-blocking)
# Async Send
# for _ in range(100):
#     producer.send('22nd_Aug_Topic', b'Some Random Binary Text')
#
# producer.flush()


#
# # Synchronous Send
for index in range(1):
    # message = f"Producing {index}"
    producer.send('random_topic_2', b'anew messsage ...  ..',b'key-2')
    # print(future.get(10))

producer.flush()
