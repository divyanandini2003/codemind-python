n=int(input())
l=list(map(int,input().split()))
s=0
for i in range(n-1):
    if l[i]<l[i+1]:
        s+=abs(l[i+1]-l[i])
print(s)