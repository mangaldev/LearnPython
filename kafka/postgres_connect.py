# connection to postgres
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="postgres")

# create a cursor
cur = conn.cursor()
print('PostgreSQL database version:')

cur.execute("select * from employees")

print(cur.fetchone())

cur.close()
