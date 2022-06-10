n=int(input())
s=0
d=n
l=len(str(n))
while(n):
    r=n%10
    s+=r**l
    n=n//10
    l-=1
if s==d:
    print(True)
else:
    print(False)