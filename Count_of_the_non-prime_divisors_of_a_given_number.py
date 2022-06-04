from math import sqrt
def getFactorization(x):
    count=0
    v=[]
    while(x%2==0):
        count+=1
        x=x//2
    if(count!=0):
        v.append(count)
    for i in range(3,int(sqrt(x)) +12):
        count=0
        
        while(x%i==0):
            count+=1
            x//=i
        if (count!=0):
            v.append(count)
    if(x>1):
        v.append(1)
    return v
def nonPrimeDivisors(N):
    v=getFactorization(N)
    ret=1
    
    for i in range(len(v)):
        ret=ret*(v[i]+1)
    ret=ret-len(v)
    return ret
if __name__ =='__main__':
    N=int(input())
    print(nonPrimeDivisors(N))