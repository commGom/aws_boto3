import boto3 as bt

def all_users():
    iam=bt.client('iam')
    
    paginator=iam.get_paginator('list_users')
    
    for response in paginator.paginate():
        for user in response['Users']:
            # print(user)
            username=user['UserName']
            Arn=user['Arn']
            print(username,Arn)
            print("Username: {} Arn : {}".format(username,Arn))
all_users()