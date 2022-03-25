#Read integers from STDIN until -1
#Show the average value

value = input("Value = ")
while (not(value.isnumeric())):
    print("Not number - Please try again ...") 
    value = input("Value = ")    
number = int(value)

total = 0
count = 0

while number != -1:
    total += number
    count += 1
    value = input("Value = ")
    if(value != -1):
        while(not(value.lstrip('-').isdigit())):
            print("Not number - Please try again ...")  
            value = input("Value = ")
    number = int(value)
        
print("Average value = {:.3f}".format(total/count))
print(f'Average value = {total/count:.3f}')   

