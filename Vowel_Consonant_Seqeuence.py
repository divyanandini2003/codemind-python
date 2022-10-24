a=input()
s=""
for i in a:
    if i in "aeiou":
        s+="V"
    else:
        s+='C'
x=s[0]
y=s[0]
for i in range(1,len(s)):
    if x!=s[i]:
        x=s[i]
        y+=s[i]
print(y)