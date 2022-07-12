n=input()
a=['a','e','i','o','u']
b=[]
c=0
for i in n:
    if i in a:
        c+=1
    else:
        b.append(c)
        c=0
b.append(c)
print(max(b))