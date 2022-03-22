
#List is a collection of data of different types
#List is ordered
#List is indexed
#List is changeable
#List allows duplicates

mylist = ["Tom",30,255.80]          #Creating a list
list2 = list(["Bank", "Account"])   #Creating a list

print(mylist)                       #Print a list
print(mylist[0])                    #Accessing first element
l = len(mylist)                     #Calculate the length of the list
print("Length is "+str(l))

print(mylist[l-1])                  #Accessing the last element
print(mylist[1:l])                  #Accessing all elements from 1 until length -1

mylist.insert(2,"has")              #Insert element at an index
print(mylist)
mylist.append("$")                  #Add an element to the end of the list
print(mylist)

mylist.remove("$")                  #Remove element by name
print(mylist)

mylist.pop(1)                       #Remove element by index
print(mylist)

mylist[l-1] = "dollars"             #Change a element at a position
print(mylist)
mylist[0] = "Lucy" 
print(mylist)

mylist.pop()                        #Remove the last element
print(mylist)

newlist = mylist + list2            #Joining 2 lists 
print(newlist)

del mylist                          #Delete the list

try:
    print(mylist)
except NameError:
    print("The list no longer exists!!!!")
    
print("Thank you")  





