s=input()
c=0
for i in range(0,len(s)):
    if s[i]>='0' and s[i]<='9':
        c+=1
if c==0:
    print("Doesn't contain digit")
else:
    print("Contains {} digit".format(c))