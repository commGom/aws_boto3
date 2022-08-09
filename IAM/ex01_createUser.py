import boto3 as bt

def create_user(username):
    iam=bt.client('iam')
    response=iam.create_user(UserName=username)
    print(response)
    
create_user('testuser')