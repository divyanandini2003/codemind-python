n=int(input())
l=list(map(int,input().split()))
k=int(input())
t=-1
for i in range(len(l)):
    if k==l[i]:
        t=i
        break
print(t)