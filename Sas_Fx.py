import csv
def Sas1(fileName):
    with open(fileName,"a", newline='') as file:
        name=input("Enter your name ?")
        place=input("Enter your place ?")
        writer=csv.writer(file)
        writer.writerow([name,place])
        # file.write(name,place)

def Sas2(fileName):
    datas=[]
    with open(fileName,"r") as file:
        reader=csv.reader(file)
        for name,place in reader:
            #print(row)
            datas.append({"name":name,"place":place})
    print("********************************")
    for data in datas:
        print(f"{data['name']} from {data['place']}")
    print("*******************************")

