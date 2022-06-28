n=int(input())
l=list(map(int,input().split()))
c=0
for i in range(n):
    c=0
    for j in range(n):
        if l[i]==l[j]:
            c+=1
    if(c==2):
        print(l[i])
        break