a,b=map(int,input().split())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
p=[]
for i in l:
    if i in m and i not in p:
        p.append(i)
print(*p)