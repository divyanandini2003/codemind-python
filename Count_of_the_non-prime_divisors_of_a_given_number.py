c=0
n=int(input())
for i in range(1,n+1):
    if(n%i==0):
        fc=0
        for j in range(1,i+1):
            if(i%j==0):
                fc+=1
        if(fc!=2):
            c+=1
print(c)