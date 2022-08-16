import boto3
from pprint import pprint 

ec2_client=boto3.client("ec2")
def create_keypair(keyname):
    response=ec2_client.create_key_pair(
        KeyName=keyname,
        KeyType='rsa'
    )
    
    pprint(response)
    # store the pem file
    file=open(keyname+".pem",'w')
    file.write(response['KeyMaterial'])

keyname='hwpboto3Key'
create_keypair(keyname)


