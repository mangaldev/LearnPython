import json
import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps([f.name for f in s3.buckets.all()])
    }
