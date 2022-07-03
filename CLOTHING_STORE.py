n=int(input())
l=list(map(int,input().split()))
k=0
for i in range(len(l)):
    c=1
    for j in range(i+1,len(l)):
        if i!=j and l[i]==l[j]:
            c+=1
            l[j]=-1
            break
    if c==2 and l[i]!=-1:
        k+=1
print(k)