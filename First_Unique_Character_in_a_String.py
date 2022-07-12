s=input()
v=0
for i in range(0,len(s)):
    c=0
    for j in range(0,len(s)):
        if s[i]==s[j]:
            c+=1
    if c==1:
        print(i)
        break
    else:
        v+=1
if v==len(s):
    print('-1')