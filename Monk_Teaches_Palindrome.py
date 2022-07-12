s=int(input())
while(s):
    a=input()
    if a==a[::-1]:
        if  len(a)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")
    s-=1