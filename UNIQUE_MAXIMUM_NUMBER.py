n=int(input())
l=list(map(int,input().split()))
c,m,s=0,0,0
for i in range(n):
    c=0
    for j in range(n):
        if i!=j and l[i]==l[j]:
           c+=1
    if c==0 and l[i]>m:
        s+=1
        m=l[i]
if s==0:
   print('-1')
else:
    print(m)
    