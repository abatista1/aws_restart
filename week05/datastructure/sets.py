#Set i sa collection of data of any type
#Set is unordered
#Set is un-indexed
#Set is changeable
#Set is unique, it does not allow duplicates

myset = {"AWS", "Restart", 2022, "Week 5"}              #Creating a set
print(myset)                                            #When printing the ordered of the elements is randomized

myset.add("Python")                                     #Adding an element to the set
print(myset)

myset.update(["March",22])                              #Add multiple elements using update
print(myset)

myset.remove("Python")                                  #Deleting by name
print(myset)

myset.discard("Restart")                                #Deleting by name
print(myset)

myset.pop()                                             #Remove last element from randomly organized set
print(myset)

set2 ={"Cohort",9}
newset = myset.union(set2)                              #Join 2 sets together
print(newset)

print("Adding duplicates")                              #Adding will not happen, no duplicates allowed
newset.add(9)
newset.add(9)
newset.add(9)
newset.add(9)
print(newset)
