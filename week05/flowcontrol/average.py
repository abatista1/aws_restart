#Read integers from STDIN until -1
#Show the average value

value = input("Value = ")
number = 0
if (value.isdigit()):
    number = int(value)
else:
    value = input("Value = ")

total = 0
count = 0

while number != -1:
    total += number
    count += 1
    value = input("Value = ")
    if(not(value.isdigit()) and (value != -1)):
        print("Please try again ...")  
        value = input("Value = ")
    number = int(value)


print("Average value = {:.3f}".format(total/count))
    
