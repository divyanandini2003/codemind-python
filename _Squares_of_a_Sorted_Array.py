n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
    l[i]=l[i]*l[i]
v=sorted((l))
print(*v)