n=int(input())
s=0
p=1
t=n
while(t>0):
    r=t%10
    s+=r
    p*=r
    t=t//10
if(s==p):
    print("Spy Number")
else:
    print("Not Spy Number")