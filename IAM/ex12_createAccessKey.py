import boto3

def create_access(user_name):
    iam=boto3.client("iam")
    
    response=iam.create_access_key(
        UserName=user_name
    )
    
    print(response)
    
create_access('testuser')