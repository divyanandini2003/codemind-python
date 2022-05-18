def fib(n):
    a,b=0,1
    print(a,b,end=' ')
    for i in range(2,n):
        c=a+b
        print(c,end=' ')
        a=b
        b=c
n=int(input())
fib(n)