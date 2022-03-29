#!/bin/python3

### Exercise 1 - The Middle Average Algorithm:

import AB_Lib as a

number_list = a.read_integer_list("Enter an integer:")

if len(number_list) >= 3:
    number_list.remove(min(number_list))
    number_list.remove(max(number_list))
    
    middle_average = a.avg(number_list)
    print(f"Number list: {number_list}")
    print(f"Middle average = {middle_average}")
else:
    print(f"Not enough values to do calculation")

