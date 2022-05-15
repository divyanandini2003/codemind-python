n=int(input())
a=list(map(int,input().split()))
c=0
for i in range(0,n):
    if a[i]%2!=0:
        c+=1
if c<=2:
    print('YES')
else:
    print('NO')