n,k=map(int,input().split())
l=list(map(int,input().split()))
for i in range(abs((k-n)%n),n):
    print(l[i],end=' ')
for i in range(0,abs((k-n)%n)):
    print(l[i],end=' ')