def prime(n):
    c=0
    for i in range(2,(n//2)+1):
        if n%i==0:
            c+=1
    if c>0 or n==1:
        return 0
    else:
        return 1
a=int(input())
b=int(input())
for i in range(a,b+1):
    if prime(i)==1:
        print (i)