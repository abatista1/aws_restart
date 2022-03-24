#Read integers from STDIN until -1
#Show the average value

finish = False
total = 0
count = 0

while not finish:
    value = input ("Enter a value: ")
    
    if (value == "-1"):
        finish = True   
    else:
        try:
            total += float(value)
            count += 1
        except ValueError:
            print("Invalid input, please try again!")     
        
if (count > 0):
    print("Average value = {:.3f}".format(total/count))
else:
    print("You have not entered any valid values")
    