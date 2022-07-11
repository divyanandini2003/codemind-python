n=int(input())
s=0
l=list(map(int,input().split()))
k=int(input())
for i in range(0,len(l)):
    if(l[i]<=k):
        s+=l[i]
print(s)