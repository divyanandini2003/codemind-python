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
def rev(x):
    s=0
    while(x>0):
        r=x%10
        s=s*10+r
        x=x//10
    return s
n=int(input())
a=n+(rev(n))
while pal(a)==0:
    a=a+rev(a)
print(a)