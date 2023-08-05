from Sas_Fx import Sas1
from Sas_Fx import Sas2

print("Sas Register")
while True:
    print("Press 1 to input: ")
    print("Press 2 to read: ")
    print("Press anything(Except 1 & 2) to exit: ")
    a=int(input("Enter the input: "))
    if a==1:
        while True:
            Sas1("Sas.csv")
            c=int(input("If u want to continue..? [Press: 4] else click any"))
            if c!=4:
                break   
    elif a==2:
        #Sas2("Rad.csv")
        Sas2("Sas.csv")
    else:
        break





