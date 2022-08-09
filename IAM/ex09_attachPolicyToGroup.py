import boto3

def attach_policy_to_group(policy_arn,group_name):
    iam=boto3.client('iam')
    
    response=iam.attach_group_policy(
        GroupName=group_name,
        PolicyArn=policy_arn
    )
    
    print(response)

pyFullAccessArn="arn:aws:iam::343542922052:policy/pyFullAccess"    
attach_policy_to_group(pyFullAccessArn,"TestGroup")