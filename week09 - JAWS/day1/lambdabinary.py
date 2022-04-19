import json
import random as r 

#Generate a random list from first to last of size n
def ranlist(first,last,n):
    return r.sample(range(first,last),n)

def binary(decimal):
    list1 = []
    zeros = [0,0,0,0,0,0,0,0]
    while decimal > 0:
        list1.append(int(decimal%2))
        decimal = int(decimal/2)
    reverse = list(reversed(list1))
    binary = zeros[len(reverse):len(zeros)]+reverse
    s = ''.join(map(str,binary))
    return s

def lambda_handler(event, context):
    keys = ranlist(1,1000,3)     
    binaryoctet = {}  

    for key in keys:
        binaryoctet[key] = binary(key) 

    return {
        'statusCode': 200,
        'body': json.dumps(binaryoctet,indent=4)
    }



