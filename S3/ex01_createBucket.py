import boto3

def create_bucket(bucket_name):
    s3=boto3.client('s3')
    
    # ACL='private' -> No one can access
    # ACL='public-read' -> owner get full control of read
    # ACL='public-read-write -> full control of read and write
    response=s3.create_bucket(
        Bucket=bucket_name,
        ACL="private",
    )   
        # create_bucket()함수의 매개변수로
        # CreateBucketConfiguration={
        #     'LocationConstraint':'east-us-1'
        # }
        # east-us-1 은 default라 작성할 필요 없음 (다른 지역은 작성해주어야함?)
    print(response)
    

bucket_name='cloo-bucketwithboto3'
create_bucket(bucket_name)