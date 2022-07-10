n=int(input())
while n:
    v=int(input())
    o=input()
    c,k=0,0
    for i in range(len(o)):
        c=0
        for j in range(len(o)):
            if i!=j and o[i]==o[j]:
                c+=1
        if c==0:
            k=1
            print(o[i])
            break
    if k==0:
        print(-1)
    n-=1