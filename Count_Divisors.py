a,b,k=map(int,input().split())
c=0
for i in range(a,b+1):
    if(i%k==0):
        c+=1
print("%d"%c)