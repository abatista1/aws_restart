#Dictionary is a collection of data in form of: key-value
#Dictionary is unordered
#Dictionary is index
#Dictionary is changeable
#Dictionary does not allow duplicates

import pprint as pp

mydictionary = {
    "name":"Tom",
    "age": 30,
    "role":"admin",
    "ID":123456
}

print(mydictionary)
print(mydictionary["role"])
pp.pprint(mydictionary,width=10)

for key in mydictionary.keys():
    print("%s - %s"%(key,mydictionary[key]))

del mydictionary["role"]
print(mydictionary)

del mydictionary
try:
    print(mydictionary)
except NameError:
    print("Dictionary has been deleted !!!")
    

    
    