#!/bin/python3

### Exercise 1 - The Middle Average Algorithm:

import AB_Lib as a


digits = hundreds = {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"} 
unique_teens = {10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen", 15 : "fifteen"}
unique_tens = {20 : "twenty", 30 : "thirty", 40 : "forty", 50 : "fifty"}

MAX = 3
# hundrced
# hundred and 
# point
# negative

HUNDREDS = 2
TENS = 1
ONES = 0

unique = unique_teens + unique_tens


hundreds.popitem();         # remove 0 from hundreds
#primary.update(unique)      # combine unique with primary
def get_tens(number):
    if number 

def convert_digit(to_convert, position):
    digit_string = ""
    

    
    
    
    if len(to_convert) >= position:
        if position = HUNDREDS:
            digit_string += primary[position] + " hundred "
        elif position = TENS:
            
            
            
            
            digit_string += primary[position]
            
            
        d = return primary[number]
    to_convert[position]

def check_unique(to_convert):
    u = primary.update(unique) 
    if

def convert_digits(to_convert):
    return_string = ""
    # check for unique_teens & unique_tens 10, 11, 12, 13, 14, 15, 20, 30, 40, 50
    target = int(to_convert[TENS] + to_convert[ONES])
     
    if target in unique:
        return_string += unique[target]
    elif CONES] == "0":
        return_string += digits[to_convert[TENS]] + "ty "
    elif to_convert[ONES] != "0":
        return_string += to_convert[ONES]
        
        if to_convert[TENS] in unique_tens:
            return_string = unique_tens[to_convert[TENS]] + return_string
        else:
            return_string = digits[to_convert[TENS]] + "ty " + return_string
     
     if to_convert[HUNDREDS] > 0:
         return_string = hundreds[to_convert[HUNDREDS]] +  + return_string
    
             
    else:
        target = int(to_convert[ONES])
    
    
    for i in to_convert:
        converted += convert_digit(to_convert[i], i)
    return converted
    
    converted = convert_digit(to_convert, 1) + convert_digit(to_convert, 2) + convert_digit(to_convert, 3)

def num_to_string(number):

    if number in primary:
        return primary[number]
    
    # split into digits
    number_as_string = str(number)
    
    return convert_digits(number_as_string)



finish = False

while not finish:
    
    value = a.read ("Number: ")
    
    if (value == "-1"):
        finish = True   
    else:
        try:
            value = int(value)
            finish = True
        except ValueError:
            print("Invalid input, please try again!")

print(num_to_string(value))       