import math
print("The value of __name__ is:", repr(__name__))
a=int(input('Enter the number :  '))
# i=2
if a==1:
    print(f'{a} is not prime')
elif a>1:
    x=math.floor(math.sqrt(a))
    for i in range(2,x+1):
        if a%i==0:
            print("The",a,'is not prime' )
            break;
    else:
        print("The",a,'is prime' )
        
    

        

