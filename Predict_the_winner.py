n=int(input())
l=list(map(int,input().split()))
s1,s2=0,0
for i in range(n):
    if i%2==0:
        s1+=l[i]
else:
        s2+=l[i]
if abs(s1-s2)%4==0:
        print("X")
else:
     print("Y")