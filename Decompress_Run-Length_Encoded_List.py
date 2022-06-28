n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
for j in range(n):
    if j%2!=0:
        a.append(l[j])
    if j%2==0:
        b.append(l[j])
for j in range(len(a)):
    for i in range(b[j]):
        print(a[j],end=' ')