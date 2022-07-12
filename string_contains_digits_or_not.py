s=int(input())
while(s):
    a=input()
    c=0
    for i in range(0,len(a)):
        if a[i]<='9' and a[i]>='0':
            c=1
            break
    if c==1:
        print("Yes")
    else:
        print("No")
    s-=1