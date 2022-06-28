n=int(input())
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
k=int(input())
c=0
for i in range(n):
    if l1[i]<=k and l2[i]>=k:
        c+=1
print(c)