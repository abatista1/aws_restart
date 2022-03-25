

x = y = "Hello"
print(x)
print(y)
print(x is y)
print (x == y)
print("-----------------------------------------------")
x, y, z = 6, "Hello", 2.5
print("{} {} {}".format(x,y,z))
print(x is y)
print(not(x is y))
print(x is not y)
print(x != y)
print("-----------------------------------------------")
x = y = 3
print(x==y)
print(x is y)
print(x < y)
print(x <= y)
print(x != y)
print(x is not y)
print(not(x==y))
print("-----------------------------------------------")
print((x != y) or (x > 2))
print((x is y) and (not(x > 1)))