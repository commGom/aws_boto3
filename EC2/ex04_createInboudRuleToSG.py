import boto3
from pprint import pprint

ec2_client=boto3.client('ec2')

def create_inbound_rule_to_sg(sg_GroupId,ipPermissions):
    response=ec2_client.authorize_security_group_ingress(
        GroupId=sg_GroupId,
        IpPermissions=ipPermissions
    )
    
    pprint(response)
    
ipPermissions=[
    {
        'IpProtocol':'tcp',
        'FromPort':80,
        "ToPort":80,
        "IpRanges":[{'CidrIp':'0.0.0.0/0','Description':'All IP 80 Allowed'}]
    },
    {
        'IpProtocol':'tcp',
        'FromPort':22,
        "ToPort":22,
        "IpRanges":[{'CidrIp':'0.0.0.0/0','Description':'All IP 22 Allowed'}]
    }
]
sg_GroupId="sg-09b073bfb55712597"

create_inbound_rule_to_sg(sg_GroupId,ipPermissions)