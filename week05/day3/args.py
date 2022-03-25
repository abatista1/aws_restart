

#Detect the script arguments and apply the following scenarios:
#1- if we have zero arguments print "no arguments"
#2- if we have one argument then print "one argument"
#3- if we have two or more arguments print the argument list

import sys 

length = len(sys.argv)

if length == 1:
    print(sys.argv[0]+" has no argument")
elif length == 2:
    print(sys.argv[0]+" has one argument: "+sys.argv[1])
else:
    print("Argument list: "+str(sys.argv))
    
    