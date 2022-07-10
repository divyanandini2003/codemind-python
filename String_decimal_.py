s=int(input())
while(s):
    a=input()
    c=0
    for i in range(0,len(a)):
        if a[i]<='9' and a[i]>='0':
            c+=1
    if c==len(a):
        print(True)
    else:
        print(False)
    s-=1