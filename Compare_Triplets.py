a=list(map(int,input().split()))
b=list(map(int,input().split()))
c1=c2=0
for i in range(3):
    if a[i]>b[i]:
        c1+=1
    elif a[i]<b[i]:
        c2+=1
print(c1,c2)