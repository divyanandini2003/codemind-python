def is_fib(i):
    a=0
    b=1
    c=a+b
    while c<i:
        c=a+b
        a=b
        b=c
    if c==i:
        return i
        
n=int(input())
k=n
for i in range(n,0,-1):
    if is_fib(i):
        a=i
        break
while k!=0:
    if is_fib(k):
        b=k
        break
    k+=1
if(n-a)<(b-n):
    print(a)
elif(n-a)==(b-n):
    print(a,b)
else:
    print(b)