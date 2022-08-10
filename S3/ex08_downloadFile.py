import boto3

bucket_name='cloo-bucketwithboto3'
file='file.txt'
def download_file(bucket_name,file):
    s3_resource=boto3.resource('s3')
    
    print(s3_resource)
    s3_object=s3_resource.Object(bucket_name,file)
    
    s3_object.download_file('downloaded.txt')
    
    print('File has been downloaded')
    
download_file(bucket_name,file)

