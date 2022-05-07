import math
n=int(input())
root=math.sqrt(n)
if int(root+0.5)**2==n:
    print("True")
else:
    print("False")