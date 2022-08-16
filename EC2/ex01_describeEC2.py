from pydoc import describe
import boto3
import json
from pprint import pprint

ec2_client=boto3.client('ec2')

def describe_instances():
    response=ec2_client.describe_instances()
    
    pprint(response)
    print(type(response))
    save_as_jsonfile(response,"test")
    
    list_of_instanceids(response)
    
def save_as_jsonfile(data,filename,file_path="./"):
    
    with open(file_path+filename+".json","w",encoding="euc-kr") as f:
        json.dump(data,f,default=str)
        
def list_of_instanceids(response):
    ec2_infos=response["Reservations"]
    ec2_instance_ids=[]
    for ec2_info in ec2_infos:
        # ec2=ec2_info["Instances"][0]["InstanceId"]
        for ec2 in ec2_info["Instances"]:
            if ec2.get("InstanceId"):
                print(ec2["InstanceId"])
                ec2_instance_ids.append(ec2["InstanceId"])
    print(len(ec2_instance_ids))
describe_instances()