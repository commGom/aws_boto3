import boto3

'''
def create_access(user_name):
    iam=boto3.client("iam")
    
    response=iam.create_access_key(
        UserName=user_name
    )
    
    print(response)
    
create_access('testuser')
'''

def update_access():
    iam=boto3.client('iam')
    response=iam.update_access_key(
        AccessKeyId='AKIAU77GA7NCLZUTJE5O',
        Status="Inactive",
        UserName='testuser'
    )
    print(response)

update_access()
    