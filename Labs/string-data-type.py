#!/bin/python
myString = "This is a string"
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

name = input("What is your name? ")
print(name)

colour = input("What is your favorite colour?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like {} {}!".format(name,colour,animal))
