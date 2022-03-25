
import csv      #Python module contains functions to manage with CSV files
import pprint   #Python module that enables structured printing

#read a CSV filename from STDIN and map it to a list of dictionaries

#Mapping CSV to a List
filename = input("File: ")              # input() reads a user value from STDIN as string
file = csv.DictReader(open(filename))   # open a file by name using open() and csv.DictReader map the csv it to a file
mylist = []                             # Empty list because of square brackets
for line in file:                       # Read lines (dictionaries) from file until the end of the file 
    mylist.append(line)                 # Add each line (a dictionary to a list)

pp = pprint.PrettyPrinter(indent=2,width=40) #Setup the pprint data width to 40 and indentation to 2 spaces
pp.pprint(mylist)

