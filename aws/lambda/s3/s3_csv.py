import boto3
import csv
s3 = boto3.resource('s3')
ob = s3.Object('dasher-ratings-cleanup', 'AutoReject011122.csv')
body = ob.get()['Body'].read()
reader = csv.DictReader(body.splitlines())
for row in reader:
    print(row)