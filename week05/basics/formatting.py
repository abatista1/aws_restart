#!/bin/python

name="Tom"
balance=150.90

#print the statement Tom has $balance on the same line

#Method 1
print(name+" has $"+str(balance))

#Method 2
print("%s has $%.3f"%(name,balance))        #we printed the balance at 3 decimal points
print("%20s has $%20.3f"%(name,balance))    #we allocated 20 spaces for the name and 20 spaces for the balance
print("%-20s has $%-20.3f"%(name,balance))  #we changed the printing starting point from right to left

#Method 3
print("{} has ${}".format(name,balance))
print("{} has ${:.4f}".format(name,balance))
print("{} has ${:.4f}".format(name,balance))#we printed the balance at 4 decimal points
print("{1} has ${0}".format(name,balance))  #we swap the order of printing
print("{:>10} has ${:.4f}".format(name,balance))  #printing name from right using the >
print("{:<10} has ${:.4f}".format(name,balance))  #printing name from left using the <
print("{:^10} has ${:.4f}".format(name,balance))  #printing name in the middle using ^
print("{:*^10} has ${:=>15.4f}".format(name,balance)) #printing name in the middle using ^ and replacing spaces by * 
                                                      #we also printing the balance from the right and replaced the spaces with =  