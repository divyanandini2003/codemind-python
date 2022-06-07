def is_prime(n):
    c=0
    flag=1
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return flag
    else:
        return 0
n=int(input())
if(is_prime(n)):
    r=0
    v=0
    while(n>0):
        d=n%10
        if(is_prime(d)):
            r+=1
        v+=1
        n=n//10
        
    if v==r:
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
        print("Not Mega Prime")