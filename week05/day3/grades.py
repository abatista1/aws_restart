#Determine the grades based on marks from arguments



#Enter the student name from STDIN

import sys 

mark = int(sys.argv[1])

name = input("Student Name: ")

if mark >= 85:
    grade = "HD"
elif mark >= 75:
    grade = "D"
elif mark >= 65:
    grade = "C"
elif mark >= 50:
    grade = "P"
else:
    grade = "Z"

result = "Welcome {}, your mark is {} and your grade is {}".format(name,mark,grade)
print(result)