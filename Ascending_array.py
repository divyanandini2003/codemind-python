n=int(input())
l=list(map(int,input().split()))
flag=0
for i in range(len(l)-1):
    if(l[i]>=l[i+1]):
        flag=1
        break
if flag==0:
    print("yes")
else:
    print("no")