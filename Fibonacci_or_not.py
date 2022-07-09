n=int(input())
if((n==0) or (n==1)):
    print("%d",n)
else:
    a=0
    b=1
    c=a+b
    while(c<n):
        a=b
        b=c
        c=a+b
    if(c==n):
        print("True")
    else:
        print("False")
