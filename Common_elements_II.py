n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
c=0
for i in l:
    if i not in l1:
        print(i,end=' ')
for j in l1:
    if j not in l:
        print(j,end=' ')
