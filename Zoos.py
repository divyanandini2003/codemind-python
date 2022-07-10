s=input()
s1,s2=0,0
for i in s:
    if i=='z':
        s1+=1
    else:
        s2+=1
if s1*2==s2:
    print("Yes")
else:
    print("No")