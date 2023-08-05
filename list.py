import os
name = ["Aiswarya", "Lekshmipriya", "Midhun", "Radhu",]
file=open("friends.txt","r")
txt=file.read()
print(txt)
friends = txt.split()
print(friends)
file.close()
os.remove("friends.txt")
# initial = []
# letter=[]
# initial2 = [x for x in name if "m" in x.lower()]
# for x in name:
#   if "d" in x[2]:
#     initial.append(x)

# for x in name:
#   if "h" in x:
#     letter.append(x)

# print(initial)
# print(letter)
# print(initial2)