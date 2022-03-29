#!/bin/python3

### Exercise 1 - The Middle Average Algorithm:

import AB_Lib as a

number_list = a.read_number_list("Rainfall:")

current_dry = 0
max_dry = 0

for i in number_list:
    if i == 0:
        current_dry += 1
        if current_dry > max_dry:
            max_dry = current_dry
    else:
        current_dry = 0

#print(f"Rainfall list: {number_list}")
print(f"Longest dry spell: {max_dry}")