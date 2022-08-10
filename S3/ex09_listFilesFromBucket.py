import boto3
BUCKET_NAME='cloo-bucketwithboto3'
def list_files(BUCKET_NAME):
    s3_resource=boto3.resource('s3')
    
    s3_bucket=s3_resource.Bucket(BUCKET_NAME)
    
    print("Listing Bucket Files or Objects")
    
    # key가 bucket에 저장된 object명 인 듯.
    for obj in s3_bucket.objects.all():
        print(obj.key)
        
list_files(BUCKET_NAME)