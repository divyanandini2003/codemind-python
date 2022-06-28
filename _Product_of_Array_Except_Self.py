n=int(input())
l=list(map(int,input().split()))
mul=1
for i in range(n):
    mul*=l[i]
for j in range(n):
    print(mul//l[j],end=" ")