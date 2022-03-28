import csv 
import json 

def read(prompt):
    return input(prompt)

def handler(csvfile):
    file = open(csvfile,'r')
    reader = csv.DictReader(file)
    return reader 

def csvtolist(reader):
    data = []
    for row in reader:
        data.append(row)
    return data 

def savetojson(jsonfile,mydata):
    file = open(jsonfile,'w+')
    file.write(json.dumps(mydata,indent=4))
    file.close()
    
def readfromjson(jsonfile):
    file = open(jsonfile,'r')
    json_obj = json.load(file)
    file.close()
    return json_obj

def showjson(obj):
    print(json.dumps(obj,indent=2))
    
    