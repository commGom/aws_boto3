import boto3

AWS_REGION = "us-east-1"

client = boto3.client('cloudwatch', region_name=AWS_REGION)

response = client.list_metrics()
print(response)
for each_metric in response['Metrics']:
    print(each_metric)