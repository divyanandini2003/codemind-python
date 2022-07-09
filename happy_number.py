n=int(input())
s=0
while(s!=1 and s!=4):
    s=0
    while(n>0):
        i=n%10
        s+=(i*i)
        n=n//10
    n=s
if s==1:
    print("True")
else:
    print("False")