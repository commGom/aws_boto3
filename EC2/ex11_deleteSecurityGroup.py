import boto3
from pprint import pprint

def delete_security_group():
    ec2_client=boto3.client('ec2')
    
    response=ec2_client.delete_security_group(
        GroupId='sg-09b073bfb55712597'
    )
    
    print(response)
    
delete_security_group()