t=int(input())
while(t):
    a=int(input())
    c=0
    k=list(map(int,input().split()))
    for i in k:
        if(i%2!=0):
            c=c+1
    print(int(c/2))
    t=t-1