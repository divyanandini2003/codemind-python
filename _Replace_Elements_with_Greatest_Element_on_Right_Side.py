n=int(input())
l=list(map(int,input().split()))
a=[]
for j in range(n-1):
    a.append(max(l[j+1:]))
a.append(-1)
print(*a)