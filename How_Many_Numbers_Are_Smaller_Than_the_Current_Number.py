n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    c=0
    for j in range(n):
        if i!=j and l[i]>l[j]:
            c+=1
    print(c,end=' ')