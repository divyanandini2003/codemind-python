n=int(input())
while n:
    n-=1
    x=int(input())
    rev=0
    t=x
    while x!=0:
        r=x%10
        rev=rev*10+r
        x=x//10
    if t==rev:
        print(True)
    else:
        print(False)