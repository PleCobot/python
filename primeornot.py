def check(n):
    if n==1:
        return False
    elif n>1:
        for i in range(2,n//2+1):
            if n%i==0:
                return False
        else:
            return True 
        
def armstrong(n):
    t=0
    m=n
    while m>0:
        t+=1
        m//=10
    m=n
    s=0
    while m>0:
        s+=(m%10)**t
        m=m//10
    #print(f"s= {s}, t={t}, n={n}")
    return n==s