#!/bin/python

s = "Goanna Restart 2022 - Python"

l = len(s)                          #we determine the length of string s
print(s[0])                         #accessing the first character in s
print(s[l-1])                       #accessing the last character in s
print(s[7:15])                      #printing substring from character at index 7 until charcater at index 14
print(s[7:])                        #printing substring from index 7 until the end of s

print(s.lower())                    #converting s to lower case
print(s.upper())                    #converting s to upper case
print(s.count("a"))                 #counting how many 'a'in s
print(s.replace("a","A"))           #replacing "a" with "A" in s
print(s.replace("Python","Java"))   #replacing a substring with another in s
print(s.find("P"))                  #finds the index of "P"
print(s.find("2022"))               #finds the starting index of the substring
print(s.isalpha())                  #checking if s is made of letters only
print(s.isdigit())                  #checking if s is made of numbers only
print(s.isalnum())                  #checking if s is made of numbers and letters
