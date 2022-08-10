import boto3

# delete all objects in s3_bucket
def clean_up(s3_bucket):
    
    for s3_object in s3_bucket.objects.all():
        print(s3_object)
        # print('{} will be deleted'.format(s3_object))
        s3_object.delete()
        
#   delete bucket versioning
def delete_bucket_versioning(s3_bucket):
    for s3_object_ver in s3_bucket.object_versions.all():
        print(s3_object_ver) 
        s3_object_ver.delete()
    
           
def delete_non_empty_bucket(bucket):
    
    s3_resource=boto3.resource('s3')
    
    s3_bucket=s3_resource.Bucket(bucket)
    
    clean_up(s3_bucket)
    
    delete_bucket_versioning(s3_bucket)
    
    print("S3 bucket cleaned")

    s3_bucket.delete()
    
    print("The bucket has been deleted")
    
# bucket_name="cloo-bucket" 
# bucket_name="cloo-bucket-client"   
bucket_name="cloo-bucketwithboto3"
delete_non_empty_bucket(bucket_name)
