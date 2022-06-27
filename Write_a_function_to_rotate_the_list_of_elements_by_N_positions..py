n=int(input())
l=list(map(int,input().split()))
k=int(input())
for i in range((n-k)%n,n):
    print(l[i],end=' ')
for i in range(0,(n-k)%n):
    print(l[i],end=' ')