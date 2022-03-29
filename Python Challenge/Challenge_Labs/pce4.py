#!/bin/python3

### Exercise 4 - The File Encryption Algorithm:

import os

filename = input("File:")
if os.path.isfile(filename):
    print(f"{filename} found")

with open(filename,'r') as file:
    file_text = file.read()
print(file_text)

target = input("Pattern:")
new_text = input("Replacement:")

print (file_text.replace(target, new_text))