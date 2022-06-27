n=int(input())
l=[]
for i in range(0,n):
    l.append(int(input()))
v=int(input())
c=0
for i in l:
    if v>=i:
        c+=1
    else:
        c+=2
print(c)