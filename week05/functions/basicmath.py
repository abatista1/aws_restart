#!/bin/env python3
def add(a,b):               #function takes 2 arguments 
    return a+b              #returns a value

#show()                     #Python functions are not hoisted
                            #Cannot call a function about the defintion
                            
def subtract(a,b):
    return a-b

def calculate(a,b):
    return a+b, a-b, a*b, a/b, a%b
                           
def show():                     #function returns no value
    result1 = add(3,4)          #call the add function to use it
    result2 = subtract(6,2)     #calling the subtract function
    print(result1)              #print the returned value from add
    print(result2)              #print the returned value from subtract
    x, y, z, m, n = calculate(4,3)       #multiple return possibility
    print("a + b = {} | a - b = {} | a * b = {} | a / b = {} | a % b = {}".format(x,y,z,m,n))
    
show()                          #calling show will execute the 2 lines of code

# for e in range(1,5):          #reusing show in the loop
#     show()
