n=int(input())
while n:
    n-=1
    x=int(input())
    f=1
    while x!=0:
        f*=x
        x-=1
    print(f)