import boto3

def add_user(user_name,group_name):
    iam=boto3.client('iam')
    
    response=iam.add_user_to_group(
        UserName=user_name,
        GroupName=group_name
    )
    
    print(response)
    
add_user('testuser','TestGroup')