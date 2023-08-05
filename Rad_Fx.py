def Rad(name,place):
    with open("Rad.csv","a") as file:
        file.write(f"{name}, {place}\n")

def lex():    
    persons=[]
    with open("Rad.csv") as file:
    #lines=file.readlines()
    #print(lines)
        for line in file:
            name,place=line.rstrip().split(",")
            x={"name":name,"place":place}
            persons.append(x)
        #print(persons)
        def get_name(person):
            return person['name']
        for person in sorted(persons,key=get_name):
            print(f"hi {person['name']} from {person['place']}")  

def Ind():    
    persons=[]
    with open("Rad.csv") as file:
    #lines=file.readlines()
    #print(lines)
        for line in file:
            name,place=line.rstrip().split(",")
            x={"name":name,"place":place}
            persons.append(x)
        #print(persons)
        for person in sorted(persons,key=lambda person:person['place']):
            print(f"hi {person['name']} from {person['place']}")  

       

