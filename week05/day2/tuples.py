#!/bin/env python3

#Tuple is a collection of data of any type
#Tuple is ordered
#Tuple is indexed
#Tuple is unchangeable
#Tuple allows duplicates

mytuple = ("Tom",30,10.5)           #Once the tuple is created it cannot be changed (Cannot add or delete elements)

print(mytuple)
print(mytuple[0])
print(mytuple[len(mytuple)-1])

tuple2 = tuple(("dollars"))

newtuple = mytuple + tuple2     #joining 2 tuples
print(newtuple)

del mytuple
try:
    print(mytuple)
except NameError:
    print("Tuple does not exist")


