import boto3

def detach_policy_from_user(username,policy_arn):
    iam=boto3.client('iam')

    response=iam.detach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )
    
    print(response)
    
username='testuser'
policy_arn='arn:aws:iam::343542922052:policy/pyFullAccess'

detach_policy_from_user(username,policy_arn)