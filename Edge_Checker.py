a,b=map(int,input().split())
if a>0 and b>0:
    if(a+1==b or b+1==a or a==1 and b==10 or b==1 and a==10):
        print("Yes")
        
    else:
        print("No")