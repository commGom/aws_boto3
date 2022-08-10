import boto3

client=boto3.client('s3')

response=client.create_bucket(
    Bucket='cloo-bucket-client',
    ACL="private",
    
    CreateBucketConfiguration={
        'LocationConstraint':'ap-northeast-2'
    }
)

print(response)

