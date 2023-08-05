persons=[]
with open("names.txt") as file:
   #lines=file.readlines()
   #print(lines)
   for line in file:
      name,place=line.rstrip().split(",")
      x={"name":name,"place":place}
      persons.append(x)
print(persons)
for person in persons:
    print(f"hi {person['name']} from {person['place']}")  




