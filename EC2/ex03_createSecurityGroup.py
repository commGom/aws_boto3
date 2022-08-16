import boto3
from pprint import pprint

ec2_client=boto3.client('ec2')
def create_security_group():
    response=ec2_client.create_security_group(
        Description="This is Desc",
        GroupName="boto3Group",
        VpcId="vpc-06331f6e598d46450"
    )
    
    pprint(response)
    
create_security_group()