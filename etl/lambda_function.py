import json
import boto3


def lambda_handler(event, context):
    print("<<<< Invoking Lambda >>>>>")

    bucketName = event["Records"][0]["s3"]["bucket"]["name"]
    fileName = event["Records"][0]["s3"]["object"]["key"]
    outputPath = 'de-batch-aug2022-result'

    print(bucketName, fileName)

    glue = boto3.client('glue')

    response = glue.start_job_run(
        JobName='spark-cdc',
        Arguments={
            '--s3_target_path_key': fileName,
            '--s3_target_path_bucket': bucketName,
            '--s3_output_path_bucket': outputPath
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
