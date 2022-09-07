n=int(input())
l=list(map(int,input().split()))
lenght=len(l)
flag=0
i=1
while i<lenght:
    if(l[i]>l[i-1]):
        flag=1
    i+=1
if(not flag):
    print("yes")
else:
    print("no")