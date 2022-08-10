import boto3

def upload_file(file_name,bucket,object_name=None,args=None):
    s3=boto3.client('s3')
    
    if object_name is None:
        object_name = file_name
    
    s3.upload_file(file_name,bucket,object_name,ExtraArgs=args)
    print('{} has been uploaded to {} bucket'.format(file_name,bucket))
    

bucket_name='cloo-bucketwithboto3'
upload_file('file.txt',bucket_name)


def upload_file_with_resource(file_name,bucket,object_name=None,args=None):
    s3_resource=boto3.resource('s3')
    
    if object_name is None:
        object_name = file_name
    
    s3_resource.meta.client.upload_file(file_name,bucket,object_name,ExtraArgs=args)
    print('{} has been uploaded to {} bucket'.format(file_name,bucket))
    
upload_file_with_resource('file2.txt',bucket_name)