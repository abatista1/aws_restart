#Determine and print the power 3 of a range 1, 10

from math import factorial

for e in range(1,10):
    print("{:8} ---> {:8} ---> {:8}".format(e,pow(e,3), factorial(e)))
    
   