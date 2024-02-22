import json
import boto3

s3 = boto3.resource('s3')


def lambda_handler(event, context):
    log = {"Operation": event["Records"][0]["eventName"].split(":")[-1],
           'File_Name': event["Records"][0]["s3"]["object"]["key"]}
    print(log)
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }