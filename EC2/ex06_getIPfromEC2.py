import boto3

ec2_client=boto3.client('ec2')

def get_ip(instance_id):
    reservations=ec2_client.describe_instances(InstanceIds=[instance_id]).get('Reservations')
    ip_address_list=[]
    for reservation in reservations:
        for instance in reservation['Instances']:
            print(instance.get('PublicIpAddress'))
            ip_address_list.append(instance.get('PublicIpAddress'))
    return ip_address_list

answers=get_ip('i-088d33c72dd167514')    
print(answers)