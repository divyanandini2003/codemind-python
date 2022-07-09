def prime(n):
    for i in range(2,(n//2)+1):
        if n%i==0:
            return False
    return True
n=int(input())
c=0
for i in range(2,n):
    if prime(i):
        for j in range(i,n):
            if prime(j):
                if i*j==n:
                    print(i,j)
                    c+=1
if c<1:
    print("-1")