def pal(x):
    a=x
    s=0
    while(x>0):
        r=x%10
        s=s*10+r
        x=x//10
    if a==s:
        return 1
    else:
        return 0
n=int(input())
if pal(n)==1:
    print(True)
else:
    print(False)
    