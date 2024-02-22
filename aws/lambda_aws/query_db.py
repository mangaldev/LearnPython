import json
import pymysql


def lambda_handler(event, context):
    column = list(event["querystring"].keys())[1]
    value = list(event["querystring"][column]

    conn = pymysql.connect(
        host='batch-dec-2022.cndqkhqvadxm.us-west-1.rds.amazonaws.com',
        user='admin',
        password='beaconfire123',
        db='world'
    )
    cur = conn.cursor()
    result = cur.execute("select * from de2024_rds where PersonID=1")
    print(result)
    return event

