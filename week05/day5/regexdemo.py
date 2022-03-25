import re

txt = \
"""
^Day05: SysAdmin, Debugging, RegEX in Python
1 - Lesson 1: Using re module from python library
2 - Lesson 2: SysAdmin commands from os Module
OS Module from Python has over 100 functions
3 - Lesson 3: Debugging python scripts$
^ NOTE: Today we will discuss #10 challenge exercises 
25/03/2022 
"""

obj = re.search("\d",txt)
print(obj)

found = re.findall("\d",txt) #Return a list of all single digits found
#print(found)

found = re.findall("\d{2}",txt) #Return a list of 2-digits
#print(found)

found = re.findall("\^",txt) #Return the carrots in the string


found = re.findall("\d{3} | #",txt) #Returns a list of 3 digits and hashes
#print(found)


