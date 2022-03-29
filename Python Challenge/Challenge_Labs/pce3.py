#!/bin/python3

### Exercise 3 - The Number to Words Algorithm:


digits = hundreds = {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"} 
base_teens = {10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen", 15 : "fifteen"}
base_tens = {20 : "twenty", 30 : "thirty", 40 : "forty", 50 : "fifty"}

base = {}
base.update(digits)
base.update(base_teens)
base.update(base_tens)
hundreds.pop(0);        # remove 0 from hundreds

def convert_single_digit(to_convert):
    if to_convert in digits:
        return digits[to_convert]

def convert_hundreds(to_convert):
    if to_convert in hundreds:
        return hundreds[to_convert]

def convert_double_digits(to_convert):
    p1 = p2 = ""
    
    if to_convert == 0:
        return ""
    elif to_convert in base:
        return base[to_convert]
    else:
        # need to derive this part of the number
        s = str(to_convert)                     # convert to string
        t = int(s[0])                           # get tens digit
        o = int(s[1])                           # get ones digit

        if t >= 6 and t <= 9:                   # 60 to 90 - these can be derived
            if t in digits:
                p1 = digits[t] + "ty"           # use digit + 'ty'
                if o != 0:  
                    p2 = convert_single_digit(o)
                return p1 + " " + p2
        elif t*10 in base_tens:                 # base numbers cant be derived, should be in the dict
            p1 = base_tens[t*10]                # 
            p2 = convert_single_digit(o)        # if this far then o should not be 0, ie. 10, 20, 30, 40, 50 should have been handled earlier
            return p1 + " " + p2 
        elif t == 1:                            # teens not in dict, can be derived
            if o >= 6 and o <= 9:
                p1 = digits[0] + "teen"
                return p1

def num_to_string(number):
    
    rem = return_string = ""

    # check for actual number that is in base and cannot be derived
    if number in base:
        return base[number]
    
    # not a number in base dict, derive number from digits
    number_as_string = str(number)      # split into digits
    
    if number >= 100:
    # check hundreds
        return_string = convert_hundreds(int(number_as_string[0])) + " hundred"
        rem = convert_double_digits(int(number_as_string[1:3]))
        if rem != "":
            return_string += " and " + rem

    if number >= 10 and number <= 99:        
        return_string = convert_double_digits(int(number_as_string[0:2]))

    return return_string

#main loop
finish = False

while not finish:
    
    value = input ("Number: ")
    
    if (value == "-1"):
        finish = True   
    else:
        try:
            value = int(value)
        except ValueError:
            print("Invalid input, please try again!")

        print(num_to_string(value))       