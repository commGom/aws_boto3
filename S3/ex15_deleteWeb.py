import boto3

s3_client=boto3.client('s3')

def delete_website_from_bucket():
    response=s3_client.delete_bucket_website(
        Bucket="metrichwpbucket"
    )
    
    print(response)
    
delete_website_from_bucket()