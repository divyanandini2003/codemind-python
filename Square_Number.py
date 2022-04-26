import math
num=int(input())
root=math.sqrt(num)
if int(root+0.5)**2==num:
    print("True")
else:
    print("False")