n=input()
l=list(map(int,input().split()))
a=[]
d=0
for i in range(0,len(l)):
    c=0
    while(l[i]!=0):
        l[i]//=10
        c+=1
    a.append(c)
x=max(a)
for j in range(0,len(a)):
    if a[j]==x:
        d+=1
print(d)    