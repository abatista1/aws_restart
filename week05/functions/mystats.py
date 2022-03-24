#Generate a random list from first to last by step with size howmany
#Calculate the min, max, sum of the sample
#Calculate the mean, stdv, variance of that sample
#Display the statistics

import random as ran
import statistics as stat

#General read function
def read(prompt):
    return input(prompt)

#Generate a random list from first to last by step, and howmany
def ranlist(first,last,step,howmany):
    return ran.sample(range(first,last,step),howmany)

#Calculate min,max, sum for any list [*argv is a place-holder for a list]
def calculate(*argv):
    minimum = min(*argv)
    maximum = max(*argv)
    total = sum(*argv)
    return minimum, maximum,total

#Calculate mean, stdv, variance
def stats(*argv):
    me = stat.mean(*argv)
    stdv = stat.stdev(*argv)
    v = stat.variance(*argv)
    return me, stdv, v

def main():
    first = int(read("First = "))
    last = int(read("Last = "))
    step = int(read("Step = "))
    n = int(read("N = ")) #Sample size
    mylist = ranlist(first,last,step,n)
    m, n, t = calculate(mylist)
    mean, stdv, var = stats(mylist)
    print(f'{m} {n} {t}')
    print(f'{mean} {stdv} {var}')
    
main()
    
    
    
    
    
    
    