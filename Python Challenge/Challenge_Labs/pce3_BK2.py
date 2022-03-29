#!/bin/python3

### Exercise 1 - The Middle Average Algorithm:

import AB_Lib as a


digits = hundreds = {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"} 
base_teens = {10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen", 15 : "fifteen"}
base_tens = {20 : "twenty", 30 : "thirty", 40 : "forty", 50 : "fifty"}

MAX = 3
# hundrced
# hundred and 
# point
# negative

HUNDREDS = 2
TENS = 1
ONES = 0

base = {}
base.update(digits)
base.update(base_teens)
base.update(base_tens)

#base = base_teens + base_tens


hundreds.popitem();         # remove 0 from hundreds
#primary.update(base)      # combine base with primary

def convert_digitsXX(to_convert):
    return_string = ""
   # check for base_teens & base_tens 10, 11, 12, 13, 14, 15, 20, 30, 40, 50
    target = int(to_convert[TENS] + to_convert[ONES])
     
    if target in base:
        return_string += base[target]
    elif to_convert[ONES] == "0":
        return_string += digits[to_convert[TENS]] + "ty "
    elif to_convert[TENS] == "1":
        return_string += digits[to_convert[ONES]] + "teen"
    elif to_convert[ONES] != "0":
        return_string += to_convert[ONES]
        
        if to_convert[TENS] in base_tens:
            return_string = base_tens[to_convert[TENS]] + return_string
        else:
            return_string = digits[to_convert[TENS]] + "ty " + return_string
     
    if to_convert[HUNDREDS] > 0:
         return_string = hundreds[to_convert[HUNDREDS]] +  + return_string

    return return_string

def convert_digits(to_convert):
    

    
    return return_string

def convert_single_digit(to_convert):
    if to_convert in digits:
        return digits[to_convert]

def convert_hundreds(to_convert):
    if to_convert in hundreds:
        return hundreds[to_convert]

def convert_double_digits(to_convert):
    
    if to_convert in base:
        return base[to_convert]
    else:
        # need to derive this part of the number
        s = str(to_convert)
        t = int(to_convert[0])
        o = int(to_convert[1])

        if t >= 6 and t <= 9: # 60 to 90
            if t in digits:
                p1 = digits[t] + "ty"
                p2 = convert_single_digit(o)
                return p1 + p2
        elif t*10 in base_tens: # base numbers cant be derived
            p1 = base_tens[t*10]
            p2 = convert_single_digit(o)
            return p1 + p2 
        elif t == 1:                    # teens
            if o >= 6 and o <= 9:
                p1 = digits[0] + "teen"
                return p1
            
                

def num_to_string(number):
    
    h = r = return_string = ""

    # check for actual number that is base and cannot be derived
    if number in base:
        return base[number]
    
    # split into digits
    number_as_string = str(number)
    
    if number >= 100:
    # check hundreds
        return_string = convert_hundreds(int(number_as_string[0])) + "hundred"

    if number >= 10 and number <= 99:        
        r = convert_double_digits(int(number_as_string[1:3]))
        
    if r != "":
        return_string += "and" + r
    
    return return_string
    # reverse the string
#    number_as_string = number_as_string [::-1]
    
    #return convert_digits(number_as_string)



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