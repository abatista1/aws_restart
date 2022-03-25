
#declare 3 integers 2, 3, 4
#update the first to itself + 1
#update the second to itself + 2
#update the third to itself + 1
#show all integers on the same line
#compute the following operations:
#first integer to the power of 2
#print the total of: ((first+second)*(second-third)/(first + 1))
x = 2
y = 3
z = 4

x += 1
y += 2
z += 1

print("x = {} ; y = {} ; z = {}".format(x,y,z))
print(x**2)  # print(pow(x,2))
result = ((x+y)*(y-z)/(x + 1))
print("Result = %f"%(result))



