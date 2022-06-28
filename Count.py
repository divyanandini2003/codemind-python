n=int(input())
l=list(map(int,input().split()))
e,o=0,0
for i in range(0,n):
    if l[i]%2==0:
        e+=1
    else:
        o+=1
print(e,o)
    