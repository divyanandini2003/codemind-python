x=int(input())
for i in range(1,x+1):
    c=0
    m,n=map(int,input().split())
    for i in range(m,n+1):
        d=i%10
        if(d==2 or d==3 or d==9):
            c+=1
    print(c)