import json
import random as r 

#Generate a random list from first to last of size n
def ranlist(first,last,n):
    return r.sample(range(first,last),n)
    
def lambda_handler(event, context):
    keys = ranlist(100,1000,3)  
    names = ['Lucy','Alice','Tom']
    record = {}                 
    i=0
    for key in keys:
        record[key] = names[i]    
        i+=1

    return {
        'statusCode': 200,
        'body': json.dumps(record,indent=4)
    }


