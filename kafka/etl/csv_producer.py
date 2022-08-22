from kafka import KafkaProducer

class Producer:
    producer = None

    def create_producer(self):
        producer = KafkaProducer(bootstrap_servers='localhost:29092')

    def producer_msg(self, msg):
        self.producer.send(msg, b'Some Random Binary Text').get(timeout=5)
