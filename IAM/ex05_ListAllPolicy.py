import boto3

def list_policies():
    iam=boto3.client('iam')

    paginator=iam.get_paginator('list_policies')
    # Scope="AWS" 로 하면 전체 policy 목록, Local로 한 경우 custom하게 만든 policy 목록만 보여준다.
    for response in paginator.paginate(Scope="Local"):
        for policy in response['Policies']:
            policy_name=policy['PolicyName']
            Arn=policy['Arn']

            print('Policy Name : {} Arn : {}'.format(policy_name,Arn))

list_policies()