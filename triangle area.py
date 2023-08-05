a=float(input('Enter the 1st side of triangle: '))
b=float(input('Enter the 2nd side of triangle: '))
c=float(input('Enter the 3rd side of triangle: '))
s=(a+b+c)/2
A=(s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the triangles with first side ',a,',second side',b,'and third side',c,'is',A)