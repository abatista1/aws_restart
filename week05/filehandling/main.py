from dataclasses import dataclass
import mapping as m 

def savetojson():
    csvfile = m.read("CSV File: ")
    reader  = m.handler(csvfile)
    data = m.csvtolist(reader)
    jsonfile = m.read("JSON File: ")
    m.savetojson(jsonfile,data)
    print("CSV saved to JSON")
    
def printjson():
    jsonfile = m.read("JSON File: ")
    jsonobj = m.readfromjson(jsonfile)
    m.showjson(jsonobj)
    
def switcher(choice):
    if choice == "S":
        savetojson()
    elif choice == "P":
        printjson()
    else:
        print("\n Invalid Command - Try Again! \n")
    
def run():
    choice = m.read("Command (S/P/X): ")
    while choice != "X":
        switcher(choice)
        choice = m.read("Command (S/P/X): ")
    print("\nThank You and hope you enjoyed Python!\n")
    
run()