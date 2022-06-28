n=int(input())
l=list(map(int,input().split()))
c,k=0,0
a=[]
for j in range(n):
    if l[j]==1:
        c+=1
    else:
        a.append(c)
        c=0
a.append(c)
print(max(a))