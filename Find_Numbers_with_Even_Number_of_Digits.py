n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n):
    t=l[i]
    c=0
    while t!=0:
        r=t%10
        c+=1
        t//=10
    if c%2==0:
        s+=1
print(s)