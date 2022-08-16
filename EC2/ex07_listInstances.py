import boto3
from pprint import pprint

def get_instances():
    ec2_client=boto3.client('ec2')
    
    reservations=ec2_client.describe_instances().get('Reservations')
    instance_info_list=[]
    for reservation in reservations:
        for instance in reservation['Instances']:
            instance_id=instance['InstanceId']
            instance_type=instance['InstanceType']
            if instance.get('PublicIpAddress'):
                public_ip=instance['PublicIpAddress']
            else:
                public_ip=None
            private_ip=instance['PrivateIpAddress']
            
            instance_info={
                "instance_id":instance_id,
                "instance_type":instance_type,
                "public_ip":public_ip,
                "private_ip":private_ip
            }
            instance_info_list.append(instance_info)
    
    return instance_info_list

answer=get_instances()

pprint(answer)
