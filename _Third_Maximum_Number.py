n=int(input())
k=list(map(int,input().split()))
p=[]
p=sorted(list(set(k)))
if(n>=3):
    print(p[-3])
else:
    print(max(k))