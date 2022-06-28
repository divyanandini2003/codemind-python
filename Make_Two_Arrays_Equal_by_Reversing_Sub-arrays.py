n=int(input())
l1=list(map(int,input().split()))
m=int(input())
l2=list(map(int,input().split()))
if(sorted(l1)==sorted(l2)):
    print(True)
else:
    print(False)