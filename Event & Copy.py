import boto3

def lambda_handler(event, context):
    # Extract source bucket and object key from the S3 event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']

    # We have specify the destination bucket...
    destination_bucket = 'tdk-test-2'

    # Initialize the S3 client...
    s3_client = boto3.client('s3')

    # Copying the object from source bucket to destination bucket
    copy_source = {
        'Bucket': source_bucket,
        'Key': object_key
    }
    destination_key = object_key  # You can change the destination key if needed
    s3_client.copy_object(
        CopySource=copy_source,
        Bucket=destination_bucket,
        Key=destination_key
    )

    print(f"Object '{object_key}' copied from '{source_bucket}' to '{destination_bucket}'.")



    # You can also return a response if needed....
    
    return {
        'statusCode': 200,
        'body': 'Copy job completed successfully.'
    }
