n=int(input())
l=list(map(int,input().split()))
v=int(input())
o=max(l)
for i in range(n):
    if(l[i]+v)>=o:
        print(True,end=' ')
    else:
        print(False,end=' ')