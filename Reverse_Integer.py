def rev_signed(n):
    s=0
    sign=1
    if(n<0):
        sign=-1
        n=n*-1
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if not -2147483648<s<2147483647:
        return 0
    return sign*s
n=int(input())
print(rev_signed(n))