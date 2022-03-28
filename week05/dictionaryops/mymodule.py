import random as r

#Read function
def read(prompt):
    return input(prompt)

#Generate a random list from first to last of size n
def ranlist(first,last,n):
    return r.sample(range(first,last),n)

#Generate a dynamic dictionary with key{3 digits}-value{STDIN}
def dynamicdictionary(n):
    keys = ranlist(100,1000,n)  #n keys of 3 digits width
    names = {}                  #empty dictionary
    
    for key in keys:
        names[key] = read("Name: ")     #dynamically reading n names 
    return names 

def sort(dictionary):
    for key in sorted(dictionary.keys()):       #sorted function sorts my list
        print("%s - %s "%(key,dictionary[key]))
        
def update(dictionary,key,newvalue):
    dictionary[key] = newvalue          #updates an element by key
    
def delete(dictionary,key):
    del dictionary[key]                 #delete an element by key
    
