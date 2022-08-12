import pandas as pd
import json
from pandas import json_normalize

with open('./hwp-ec2_cpu.json', "r", encoding='utf8') as f:
    contents = f.read() 
    json_data=json.loads(contents)
#print(json.dumps(json_data))
print(len(json_data))
# print((json_data)[0].keys())
# print((json_data)[0]['Type'])
# print((json_data)[1000]['Attributes'])

df=json_normalize(json_data)
df.to_csv("./test.csv")