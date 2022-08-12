import boto3


def delete_object_from_s3(key):
    s3=boto3.client('s3')
    
    response=s3.delete_object(
        Bucket="metrichwpbucket",
        Key=key
    )
    
    print(response)

# objects=['test.json','copied.json','file/copied.json']    
# for obj in objects: 
#     delete_object_from_s3(obj)

# delete_object_from_s3('folder/*') -> 이건 안 됨!!

def delete_multiple_file():
    s3=boto3.client('s3')
    
    response=s3.delete_objects(
        Bucket="metrichwpbucket",
        Delete={
            'Objects':[
                {'Key':'folder/file1.txt'},
                {'Key':'folder/file2.txt'},
                {'Key':'folder/file3.txt'}
            ]
        }
    )
    
    print(response)
    
# delete_multiple_file()