def hcf(a,b):
    for i in range(a,0,-1):
        if a%i==0 and b%i==0:
            break
    return i
n,m=map(int,input().split())
c=hcf(n,m)
print(c)