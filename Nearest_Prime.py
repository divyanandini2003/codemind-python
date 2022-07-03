def prime(j):
    i=2
    v=0
    while i!=j:
        if j%i==0:
            v=1
        i+=1
    if v==0:
        return j
x=int(input())
for i in range(x):
    y=int(input())
    b=y
    for j in range(y,1,-1,):
        if prime(j):
            n=j
            break
    for k in range(2,y):
        if prime(b):
            m=b
            break
        b+=1
    if(y-n)<(m-y):
        print(n)
    elif(y-n)==(m-y):
        print(n)
    else:
        print(m)