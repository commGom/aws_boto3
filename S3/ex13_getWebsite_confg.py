import boto3

s3_client=boto3.client('s3')

def get_web_config():
    response=s3_client.get_bucket_website(
        Bucket="metrichwpbucket"
    )
    
    print(response)
    
get_web_config()