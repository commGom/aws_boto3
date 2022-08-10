from sys import prefix
import boto3

bucket_name='cloo-bucketwithboto3'

# 현재 bucket에 있는 object 설정 file.txt, file2.txt, myfile.txt
def upload_file_with_resource(file_name,bucket,object_name=None,args=None):
    s3_resource=boto3.resource('s3')
    
    if object_name is None:
        object_name = file_name
    
    s3_resource.meta.client.upload_file(file_name,bucket,object_name,ExtraArgs=args)
    print('{} has been uploaded to {} bucket'.format(file_name,bucket))
    
uploaded_file_list=["file.txt","file2.txt","myfile.txt"]
for uploading_file in uploaded_file_list:
    upload_file_with_resource(uploading_file,bucket_name)

print('All Files have been uploaded.')

def list_files(bucket_name):
    s3_resource=boto3.resource('s3')
    
    s3_bucket=s3_resource.Bucket(bucket_name)
    
    print("Listing Bucket Files or Objects")
    
    # key가 bucket에 저장된 object명 인 듯.
    for obj in s3_bucket.objects.all():
        print(obj.key)

print('bucket에 있는 전체 object 출력')
list_files(bucket_name)

def list_with_filtering(bucket_name,prefix):
    s3_resource=boto3.resource('s3')
    
    s3_bucket=s3_resource.Bucket(bucket_name)
    
    print("Listing Filtered File")
    
    for obj in s3_bucket.objects.filter(Prefix=prefix):
        print(obj.key)

prefix="file"
print("Prefix가 {}인 bucket에 있는 object 출력".format(prefix))    
list_with_filtering(bucket_name,prefix)