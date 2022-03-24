
#Read a radius from STDIN
#Calculate the perimeter, area of a circle
#Calculate the volume of a sphere
#Print all the results
#USe parametric functions to improve reusability

import math as m 

#General read function
def read(prompt):
    return input(prompt)

#Calculate perimeter
def calculate(r):
    perimeter = 2*m.pi*r;
    area = m.pi*pow(r,2)
    volume = (4/3)*m.pi*pow(r,3)
    return perimeter, area, volume

#Show results
def show():
    r = int(read("Radius = "))
    p, a, v = calculate(r)
    print("Perimeter = %.3f"%(p))
    print("Area = {:.3f}".format(a))
    print(f'Volume = {v:.4f}')
    
show()
    
    