n=int(input())
c=0
a=0
s=0
l=list(map(int,input().split()))
for i in range(0,len(l)):
    s+=l[i]
a=s//n
for i in range(0,len(l)):
    if(l[i]>=a):
        c+=1
print(c)