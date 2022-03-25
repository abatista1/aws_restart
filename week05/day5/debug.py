import logging

output = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='app.log',level=logging.DEBUG,format=output)

def read(prompt):
    return input(prompt)

def add(a,b):
    return a+b 

def div(a,b):
    return a/b

#Unit Test to validate the input
def verifyInput(value):
    assert str(value).isnumeric(), str(value)+" Not a number"

#Unit Test to validate the division    
def validateDiv(a,b):
    assert b==0 , "Cannot divide by Zero"

def show():
    a = logging.debug(read("a = "))     #debugging read a
    b = logging.debug(read("b = "))     #debugging read b
    
    #The unit tests dynamically run with the script
    verifyInput(a)
    verifyInput(b)
    validateDiv(a,b)

    logging.getLogger().info(print(add(a,b)),stack_info=True)
    logging.getLogger().info(print(div(a,b)),stack_info=True)
show()

