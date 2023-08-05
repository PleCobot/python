n=int(input("Enter a no: "))
sum=0
m=n

while(n>0):
    i=1
    fact=1
    rem=n%10

    while(i<=rem):
        fact=fact*i
        i+=1
    sum+=fact
    n=n//10

if m==sum:
    print('number is strong number')

else:  
    print('number is not a strong number')
     

