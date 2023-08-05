from primeornot import armstrong
l=int(input('Enter the lower range'))
u=int(input('Enter the upper range'))
print('Armstrong numbers are')
#print(armstrong(153))
for i in range(l,u+1):
    if armstrong(i):
        print(i)