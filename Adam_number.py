def reverse(n):
    rev=0
    while(n):
        r=n%10
        rev=rev*10+r
        n//=10
    return rev
n=int(input())
a=n*n
b=reverse(n)
c=b*b
d=reverse(c)
if d==a:
    print("True")
else:
    print("False")