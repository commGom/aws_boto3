import boto3

def stop_instance(instance_id):
    ec2_client=boto3.client('ec2')
    
    response=ec2_client.stop_instances(InstanceIds=[instance_id])
    
    print(response)
    
stop_instance("i-088d33c72dd167514")