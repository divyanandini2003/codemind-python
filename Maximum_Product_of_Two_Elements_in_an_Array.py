l=list(map(int,input().split()))
max=0
for i in range(len(l)):
    for j in range(i+1,len(l)):
        c=(l[i]-1)*(l[j]-1)
        if c>max:
            max=c
print(max)