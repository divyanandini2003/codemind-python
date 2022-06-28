n=int(input())
while(n):
    j=int(input())
    l=list(map(int,input().split()))
    print(j*(j+1)//2-sum(l))
    n-=1