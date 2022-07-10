def prime(n):
    if n<=1:
        return False
    else:
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        else:
            return True
            
def pali(n):
    temp=n
    rev=0
    while temp:
        rev=rev*10+(temp%10)
        temp//=10
    if rev==n:
        return True
    else:
        return False
        
n=int(input())
i=n+1
while prime(i)==False or pali(i)==False:
    i=i+1
print(i)