n=int(input())
m=int(input())
s=0
for i in range(1,n,1):
    if(n%i==0):
        s=s+i
if(s==m):
    print("Amicable")
else:
    print("Not Amicable")
