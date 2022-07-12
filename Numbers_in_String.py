s=input()
sum=0
for i in range(0,len(s)):
    if s[i]>='0' and s[i]<='9':
        sum+=int(s[i])
print(sum)
