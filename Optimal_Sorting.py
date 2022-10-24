n=int(input())
c=0
for i in range(n):
    a=int(input())
    l=list(map(int,input().split()))
    for j in range(1,a):
        if(l[j]<l[j-1]):
            c+=1
    if(c==0):
        print(c)
    else:
        ma=max(l)
        mi=min(l)
        print(ma-mi)