import mymodule as m 

def main():
    n = int(m.read("N = "))
    names = m.dynamicdictionary(n)
    m.sort(names)
    
    key = int(m.read("Update by key: "))
    replacement = m.read("Name: ")
    m.update(names,key,replacement)
    m.sort(names)
    
    key = int(m.read("Delete by key: "))
    m.delete(names,key)
    m.sort(names)
    
main()
    


