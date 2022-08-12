import boto3

s3_client=boto3.client('s3')

def delete_policy():
    response=s3_client.delete_bucket_policy(
        Bucket="metrichwpbucket"
    )
    
    print(response)
    
delete_policy()

