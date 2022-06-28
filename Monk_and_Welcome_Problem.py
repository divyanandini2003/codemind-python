n=int(input())
l=list(map(int,input().split()))
m=list(map(int,input().split()))
for i in range(n):
    l[i]=l[i]+m[i]
print(*l)