import csv
import json

from confluent_kafka.serialization import StringSerializer
from kafka import KafkaProducer
from caphca.etl.employee import Employee

employee_topic_name = "employee_data_8thFeb"


class CaphcaProducer:

    def __init__(self, host="localhost", port="29092"):
        self.host = host
        self.port = port
        self.producer = KafkaProducer(bootstrap_servers=('%s:%s' % (self.host, self.port)))

    def producer_msg(self, topic_name, key, value):
        self.producer.send(topic=topic_name, key=key, value=value).get(timeout=5)


class CsvReader:
    def read_csv(self, csv_file='../resources/employees.csv'):
        with open(csv_file, newline='') as csvfile:
            rows = []
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                # print(', '.join(row))
                rows.append(row)
            return rows


if __name__ == '__main__':
    reader = CsvReader()
    producer = CaphcaProducer()
    lines = reader.read_csv('../../resources/employees.csv')
    for line in lines[1:]:
        emp = Employee.from_csv_line(line)
        producer.producer_msg(employee_topic_name, key=f"{emp.emp_id}".encode(), value=emp.to_json().encode())
