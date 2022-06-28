n=int(input())
l=list(map(int,input().split()))
m=int(input())
l1=list(map(int,input().split()))
p=[]
for i in range(n):
    p.insert(l1[i],l[i])
print(*p)