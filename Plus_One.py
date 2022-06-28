n=int(input())
a=list(map(int,input().split()))
v=0
for i in range(n):
    v=v*10+a[i]
v+=1
a=[]
while(v!=0):
    r=v%10
    a.append(r)
    v//=10
print(*a[::-1])