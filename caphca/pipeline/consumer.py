import json

import psycopg2

from caphca.etl.consumer import CaphcaConsumer
from caphca.etl.producer import employee_topic_name
from caphca.pipeline.employee import DepartmentEmployee
from caphca.pipeline.producer import topic_name


def persist_employee(msg):
    e = DepartmentEmployee(**(json.loads(msg.value())))
    department_employee = (e.department, e.department_division, e.position_title, e.hire_date, e.salary)
    print(department_employee)
    try:
        conn = psycopg2.connect(
            host="localhost",
            database="postgres",
            user="postgres",
            password="postgres")
        conn.autocommit = True

        # create a cursor
        # cur = conn.cursor()
        # cur.execute(
        #     "insert into  department_employee  (department,department_division,position_title,hire_date,salary)  values (%s,%s,%s,%s, %s) on conflict do nothing",
        #     department_employee)
        # cur.close()
        cur2 = conn.cursor()
        cur2.execute(
            "insert into  department_employee_salary  (department,total_salary)  values (%s,%s) on conflict(department) do update set total_salary = department_employee_salary.total_salary + %s    ",
            (e.department, int(float(e.salary)), int(float(e.salary))))
        conn.commit()
        cur2.close()


    except Exception as e:
        print(e)


if __name__ == '__main__':
    consumer = CaphcaConsumer(group_id="employee_consumer_1112")
    consumer.consume([topic_name], persist_employee)
