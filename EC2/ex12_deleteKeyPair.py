import boto3

def delete_key_pair():
    ec2_client=boto3.client('ec2')
    
    response=ec2_client.delete_key_pair(
        KeyName='hwpboto3Key'
    )
    
    print(response)
    
delete_key_pair()