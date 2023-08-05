from math import sqrt
import math
def Prime(number,itr): #prime function to check given number prime or not
    if itr == 1: #base condition
        return True
    if number % itr == 0: #if given number divided by itr or not
        return False
    if Prime(number,itr-1) == False: #Recursive function Call
        return False
        
    return True

num =1
if num== 1:
    print ("False")
    exit()
itr =math.floor((sqrt(num)))
print(f"number {num}")
print(f"itr {itr}")
print(Prime(num,itr))