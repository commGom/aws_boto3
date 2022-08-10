import boto3


def upload_image(image_name):
    s3=boto3.client('s3')
 #   mode=rb -> read mode
    mode='rb'   
    with open(image_name,mode) as f:
        data=f.read()
    
    response=s3.put_object(
        ACL="private",
        Bucket="cloo-bucket",
        Body=data,
        Key=image_name
    )

    print(response)
upload_image('aws_service-block.png')