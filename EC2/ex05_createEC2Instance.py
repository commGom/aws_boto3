import boto3
from pprint import pprint

ec2_resource=boto3.resource('ec2')

def create_ec2_instance():
    response=ec2_resource.create_instances(
        ImageId="ami-033b95fb8079dc481",
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='hwpboto3Key',
        SecurityGroups=[
            'boto3Group'
        ]   
    )
    
    pprint(response)
    
AMI_ImageID="ami-020ef1e2f6c2cc6d6"
Instance_Type="t2.micro"
create_ec2_instance()