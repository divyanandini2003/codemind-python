def is_prime(s):
    if s==1:
        return False
    for i in range(2,s//2):
        if s%i==0:
            return False
    return True
x=int(input())
s=0
a=x
while x!=0:
    v=x%10
    s=s*10+v
    x=x//10
if is_prime(s) and is_prime(a):
    print('circular prime')
elif(is_prime(a)):
    print('prime but not a circular prime')
else:
    print('not prime')