import boto3

def detachUserFromGroup(UserName,GroupName):
    iam=boto3.resource('iam')
    
    group=iam.Group(GroupName)
    
    response=group.remove_user(
        UserName=UserName
    )
    
    print(response)
    
detachUserFromGroup('testuser','TestGroup')