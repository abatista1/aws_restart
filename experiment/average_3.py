#Read integers from STDIN until -1
#Show the average value

finish = False
total = 0
count = 0

while not finish:
    value = input ("Value: ")

    if ('.' in value):
        try:
            total += float(value)
            count += 1
            print("Float!")
        except ValueError:
            pass
    else: 
        if (value == "-1"):
            finish = True
        elif (value.isdigit()):
            total += float(value)
            count += 1
        else:
            print("Invalid input, please try again!")
        
try:
    print("Average value = {:.3f}".format(total/count))
except ZeroDivisionError:
    print("division by zero")
    