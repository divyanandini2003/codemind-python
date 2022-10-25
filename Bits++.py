n=int(input())
c=0
for i in range(n):
    a=input()
    if "++" in a:
        c+=1
    if "--"in a:
        c-=1
print(c)