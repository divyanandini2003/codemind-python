n=str(input())
l=list(n)
a=set(l)
if len(a)==len(l):
    print('Unique Number')
else:
    print('Not Unique Number')