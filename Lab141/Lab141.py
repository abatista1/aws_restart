#!/bin/python3

min = 1
max = 250
filename = "results.txt"

def is_prime(number):
	for i in range(2,number):
		if(number%i) == 0:
			return False
	return True
	
def write_to_file(prime_str):
	file = open(filename, "w+")
	file.write(prime_str)
	file.close()
	
def main():
	result = ""
	
	for n in range(min, max+1):
		if is_prime(n):
			result += str(n) + ","
			
	result = result[:-1]
	print(result)
	write_to_file(result)
	
main()