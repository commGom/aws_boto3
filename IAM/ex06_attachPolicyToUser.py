import boto3

# Policy를 가지고 있지 않은 User에게 Policy를 부여할 것이다. ex) testuser
# ex04에서 만들었던, pyFullAccess 의 정책을 적용시킬 것이다. Arn = arn:aws:iam::343542922052:policy/pyFullAccess

def attach_policy(policy_arn,username):
    iam=boto3.client('iam')
    
    response=iam.attach_user_policy(
        UserName=username,
        PolicyArn=policy_arn
    )
    
    print(response)
    
attach_policy('arn:aws:iam::343542922052:policy/pyFullAccess','testuser')