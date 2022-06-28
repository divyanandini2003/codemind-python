def is_sq(m):
    l=int(m**0.5)
    if l*l==m:
        return 1
    else:
        return 0
n=int(input())
a=list(map(int,input().split()))
s=0
for i in range(n):
    if is_sq(a[i]):
        s+=a[i]
print(s)