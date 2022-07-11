n=int(input())
o=0
s=0
l=list(map(int,input().split()))
for i in  range(0,len(l)//2):
    s+=l[i]
for i in range(len(l)//2,len(l)):
    o+=l[i]
if(o>s):
    print(o-s)
else:
    print(s-o)