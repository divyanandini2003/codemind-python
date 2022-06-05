n=int(input())
f=0
s=1
print(f,s,end=" ")
for i in range(2,n):
    nex=f+s
    f=s
    s=nex
    print(nex,end=" ")