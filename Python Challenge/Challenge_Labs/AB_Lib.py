#!/bin/python3

#AB_Lib
#library of commo0n functions to use in the challenge lab

# read a user input
def read(prompt="Enter a value:"):
    return input(prompt)

# read a list of numbers
def read_number_list(prompt, stop="-1", range_min="", range_max="", int_only = False):
    finish = False
    number_list = []
    
    while not finish:
        value = read(prompt)
        
        if (value == stop):
            finish = True
        else:
            try:
                if (int_only):
                    number_list.append(int(value))
                else:
                    number_list.append(float(value))
            except ValueError:
                print("Invalid input, please try again!")     
    return number_list

# read a list of integers
def read_integer_list(prompt, stop="-1", range_min="", range_max=""):
    return read_number_list(prompt, stop, range_min, range_max, True)

# calculate the average
def avg(number_list):
    if (len(number_list) >= 1):
        return sum(number_list)/len(number_list)