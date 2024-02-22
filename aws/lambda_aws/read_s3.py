import boto3

# Create an S3 client
s3 = boto3.client('s3')


def read_s3_file(bucket_name, file_name):
    try:
        # Get the object from the bucket
        response = s3.get_object(Bucket=bucket_name, Key=file_name)

        # Read the contents of the file
        contents = response['Body'].read().decode('utf-8')

        return contents
    except Exception as e:
        print(f"Error reading file {file_name} from bucket {bucket_name}: {e}")
        return None


# Example usage
bucket_name = 'de2024east1'
file_name = 'Employee_Department.csv'


def lambda_handler(event, context):
    file_contents = read_s3_file(bucket_name, file_name)
    if file_contents:
        print("File contents:")
        print(file_contents)

    return {
        'statusCode': 200,
        'body': file_contents
    }
