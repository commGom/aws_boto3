import boto3

# 주의 사항 bucket 안에 object가 삭제되어 있어야 한다.
def delete_bucket(bucket):
    s3=boto3.client('s3')
    
    response=s3.delete_bucket(Bucket=bucket)
    
    print(response)
    print('{} bucket has been deleted'.format(bucket))
    
delete_bucket('cloo-bucket')

# Delete bucket with aws resource
def delete_bucket_with_resource(bucket):
    resource =boto3.resource('s3')

    s3_bucket=resource.Bucket(bucket)
    
    
    s3_bucket.delete()
    
    print('{} bucket has been deleted'.format(bucket))
    
