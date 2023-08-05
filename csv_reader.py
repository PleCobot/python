import csv
def Ind_csv():    
    persons=[]
    with open("Rad.csv") as file:
        reader=csv.reader(file)
        for name,place in reader:
            x={"name":name,"place":place}
            persons.append(x)
        for person in sorted(persons,key=lambda person:person['place']):
            print(f"hi {person['name']} from {person['place']}")  