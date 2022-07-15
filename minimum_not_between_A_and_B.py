n=int(input())
mi=100
d=0
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=set(l)
for i in s:
    if(i<a or i>b):
        if(i<mi):
            mi=i
            d+=1
if(d!=0):
    print(mi)
else:
    print("-1")
        