

mylist= list(range(1,30))           #Create a sequence of elements using range from 1 to 29
print(mylist)

element = int(input("Find: "))

if(mylist.index(element)):          #index() finds an element by position in the list
    mylist[mylist.index(element)] = "Element Found"

    
print(mylist)
