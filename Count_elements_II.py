n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
l=set(l)
l1=set(l1)
c=0
for i in l:
    if i not in l1:
        c+=1
for j in l1:
    if j not in l:
        c+=1
print(c)