import boto3

def list_all_buckets():
    s3=boto3.client('s3')
    
    response=s3.list_buckets()
    
    print(response)
    
    print('Listing All Bukcet Names')
    for bucket in response['Buckets']:
        print(bucket['Name'])
    
list_all_buckets()

def list_all_buckets_with_resource():
    s3_resource=boto3.resource('s3')
    iterator=s3_resource.buckets.all()

    print('Listing All Bukcet Names 2')
    for bucket in iterator:
        print(bucket)
        print(bucket.name)
    
list_all_buckets_with_resource()