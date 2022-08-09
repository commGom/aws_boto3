import boto3

def detach_group(group_name,arn):
    iam=boto3.client('iam')

    response=iam.detach_group_policy(
        GroupName=group_name,
        PolicyArn=arn
    )
    
    print(response)

detach_group("TestGroup","arn:aws:iam::343542922052:policy/pyFullAccess")