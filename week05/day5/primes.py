#Define a function that reads any value
#Define a function that checks if a number is a prime
#Define a function that returns a list of primes from a range(first,last)
#Define a function that saves the list of primes to a text file

def read(prompt):
    return input(prompt)

def isprime(n):
    for e in range(2,n):
        if n%e == 0:
            return False
    return True

def primeslist(first,last):
    primes = []
    for e in range(first,last+1):
        if isprime(e):
            primes.append(e)
    return primes 

def savetofile(mylist,filename):
    file = open(filename,'w+')
    for line in mylist:
        file.write(str(line))
        file.write("\n")
        
def main():
    first = int(read("First = "))
    last = int(read("Last = "))
    primes = primeslist(first,last)
    filename = read("File name: ")
    savetofile(primes,filename)
    
main()
        