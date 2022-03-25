#Create a range of integers from 1 to 20
#Calculate the sum
#Display the average

startindex = 1
endindex = 32
step = 3
numbers = list(range(startindex,endindex,step))
print(numbers)

total = 0
for e in range(startindex,endindex,step):
    total += e
print("Average = {:.2f}".format(total/len(numbers)))

print("------------------------------------")

print("Average = {:.2f}".format(sum(numbers)/len(numbers)))
