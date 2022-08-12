import boto3

def copy_object_to_s3():
    s3=boto3.resource('s3')
    
    # Bucket : 원본출처S3 버킷이름, Key : 버킷 안에 있는 원본 파일 이름
    copy_source={
        'Bucket':"hwpnewbucket",
        'Key':'test.json'
    }
    
    #  s3.meta.client.copy(copysource, 버킷대상, object Key-파일명)
    response=s3.meta.client.copy(copy_source,'metrichwpbucket','dir/copied.json')
    
    print(response)
    
copy_object_to_s3()