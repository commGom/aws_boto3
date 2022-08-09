import boto3

def create_console_login(user_name):
    iam=boto3.client('iam')

    login_profile=iam.create_login_profile(
        Password='Mypassword@1',
        PasswordResetRequired=False,
        UserName=user_name
    )
    
    print(login_profile)
  
create_console_login('testuser')