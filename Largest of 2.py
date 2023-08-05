# print('For quitting- PRESS c')
# while True:
#     a=float(input('Enter the 1st number:  '))
#     b=float(input('Enter the 2nd number:  '))
#     # print(r)
#     print(a) if a>b else print(a,'=',b) if a==b else print(b)
  
#     r=input('Do u want to continue?')
#     if r == 'c':
#         break


# if a>b:
#     print(a,'is large')

# else:
#     if a==b:
#         print(a,'=',b)
#     else:
#         print(b,'greater than',a)

a=int(input('Enter the 1st number:  '))
i=2
if a==1:
    print(f'{a} is not prime')
elif a>1:
    while i<= a//2:
        if a % i ==0:
             print(f'{a} is not prime')
             break       
        i+=1
    else:
        print(f'{a} is prime')

else:
    print(f'Enter a posivite number')
     

