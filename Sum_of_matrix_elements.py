n=int(input())
m=int(input())
s=0
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(m):
        s+=a[j]
    a=[]
print(s)