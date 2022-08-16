import boto3

def terminate_instance(instace_id):
    ec2_client=boto3.client('ec2')
    
    response=ec2_client.terminate_instances(InstanceIds=[instance_id])

    print(response)
    
instance_id="i-088d33c72dd167514"
terminate_instance(instace_id=instance_id)