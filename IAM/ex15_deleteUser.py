import boto3

def delete_user(username):
    iam=boto3.client('iam')
    
    response=iam.delete_user(
        UserName=username
    )
    
    print(response)
    
# delete_user('testuser')
# user list 정규표현식 이용하여 test 포함된 username만 뽑아와서 리스트에 저장한 후 for 반복문 통해서 user 삭제 해보기
# user 삭제하기 위해선 group에 소속되면 안되고, policy도 가지고 있으면 안 되고 access key도 있으면 안 됨.(나중에 고려해서 코드 만들어보기.)
# all_usernames=['testuser','updatedtestuser']
# for user in all_usernames:
#     delete_user(user)

delete_user('updatedtestuser')