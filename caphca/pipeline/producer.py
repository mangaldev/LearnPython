import csv
import json
from datetime import datetime

from confluent_kafka.serialization import StringSerializer
from kafka import KafkaProducer
from caphca.etl.employee import Employee
from caphca.etl.producer import CsvReader, CaphcaProducer
from caphca.pipeline.employee import DepartmentEmployee

topic_name = "employee_department_pipeline"

if __name__ == '__main__':
    reader = CsvReader()
    producer = CaphcaProducer()
    lines = reader.read_csv('../../resources/Employee_Salaries_1.csv')
    for line in lines[1:]:
        emp = DepartmentEmployee.from_csv_line(line)
        if emp.filter():
            producer.producer_msg(topic_name, key=f"{emp}".encode(), value=emp.to_json().encode())
