n1,n2=map(int,input().split())
for i in range(1,(n1*n2)+1,1):
    if((i%n1==0) and (i%n2==0)):
        break
print("%d"%i)