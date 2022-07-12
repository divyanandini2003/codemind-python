n=int(input())
l=list(map(int,input().split()))
f=0
for i in range(0,len(l)):
    if(l[i]%2==0):
        f+=1

if (f==n):
    print("True")
else:
    print("False")