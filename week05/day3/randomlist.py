#Generate a random list of size n, where n is from STDIN
#Generate the list from a sample with first and last elements captured from arguments
import random as ran
import sys

n = int(input("N = "))              #size of the random list
first = int(sys.argv[1])                 #first element in the range
last = int(sys.argv[2])                  #last element in the range
 
mylist = ran.sample(range(first,last),n)      
print(mylist)

maximum = 0
for e in mylist:
    if maximum < e:
        maximum = e 
print("Maximum = {}".format(maximum))

print("------------------------------------")

print("Maximum = {}".format(max(mylist)))
print("Minimum = {}".format(min(mylist)))
print("Sum = {}".format(sum(mylist)))
print("Average = {:.2f}".format(sum(mylist)/len(mylist)))