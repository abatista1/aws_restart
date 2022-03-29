#!/bin/python3

### Exercise 3 - The Number to Words Algorithm:

# the numbers in the dictionarys cannot be derived but can be used to derive compund numbers
digits = hundreds = {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"} 
base_teens = {10 : "ten", 11 : "eleven", 12 : "twelve", 13 : "thirteen", 15 : "fifteen"}
base_tens = {20 : "twenty", 30 : "thirty", 40 : "forty", 50 : "fifty"}

base = {}                   # create a single dictionary to search for numbers that dont need to be derived
base.update(digits)
base.update(base_teens)
base.update(base_tens)
hundreds.pop(0);            # remove 0 from hundreds

def convert_single_digit(to_convert):
    if to_convert in digits:
        return digits[to_convert]

def convert_hundreds(to_convert):
    if to_convert in hundreds:
        return hundreds[to_convert]

def derive_digits(to_convert):                  # should be just 2 digits now
    r1 = r2 = ""

    s = str(to_convert)                         # convert to string
    tens = int(s[0])                            # get tens digit
    ones = int(s[1])                            # get ones digit

    if tens >= 6 and tens <= 9:                 # 60 to 90 - these can be derived
        if tens in digits:
            r1 = digits[tens] + "ty"           # use digit + 'ty'
            if ones != 0:                           # could possibly get a 0 here as second digit, ie. 60, ignore it - sixty is the complete word
                r2 = convert_single_digit(ones)
            return r1 + " " + r2
    elif tens*10 in base_tens:                  # base numbers cant be derived, should be in the dict
        r1 = base_tens[tens*10]                 # 
        r2 = convert_single_digit(ones)         # if this far then o should not be 0, ie. 10, 20, 30, 40, 50 should have been handled earlier
        return r1 + " " + r2 
    elif tens == 1:                             # teens not in dict, can be derived
        if ones == 4 or (ones >= 6 and ones <= 9):
            r1 = digits[ones] + "teen"             # add "teen" ie. "six" + "teen"
            return r1

def convert_double_digits(to_convert):

    if to_convert == 0:
        return ""
    elif to_convert in base:
        return base[to_convert]
    else:
        # need to derive this part of the number
        return derive_digits(to_convert)

def num_to_string(number):
    
    last_2_digits = return_string = ""

    # check for actual number that is in base dict and cannot be derived
    if number in base:
        return base[number]
    
    # not a number in base dict, derive number from digits
    number_as_string = str(number)      # split into digits
    
    if number >= 100:                   # check hundreds
        return_string = convert_hundreds(int(number_as_string[0])) + " hundred"     # convert the value in the hundreds position
        last_2_digits = convert_double_digits(int(number_as_string[1:3]))           # get the last 2 digits (tens and ones) then convert them
        if last_2_digits != "":
            return_string += " and " + last_2_digits

    if number >= 10 and number <= 99:        
        return_string = convert_double_digits(int(number_as_string[0:2]))

    return return_string

#main loop
while True:
    valid_input = False
    value = input ("Number: ")
    
    if (value == "-1"):
        print("Done")
        break
    else:
        try:                            # let python check if the number is the correct type
            value = int(value)
            if value >= 0 and value <= 999:
                valid_input = True
        except ValueError:
            #print("Invalid input, please try again!")
            pass
    
    if valid_input:
        print(num_to_string(value))
    else:
        print("Invalid input, expecting a number between -1 and 999 - please try again!")
        
        