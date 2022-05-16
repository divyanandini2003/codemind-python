n=int(input())
d=0
r=0
c=0
o=0
while(n!=0):
    r=n%10
    n=n//10
    c+=1
    if(r%2==0):
        d+=1
    if r%2!=0:
        o+=1
if d==c:
    print('Even')
elif(o==c):
    print('Odd')
else:
    print('Mixed')