n=int(input())
c=0
l=list(map(int,input().split()))
s=set(l)
for i in s:
    if(i%2==0):
        c+=i
print(c)