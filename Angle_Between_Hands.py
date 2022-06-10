h,m=map(int,input().split(':'))
if abs(30*h-(11/2)*m)>180:
    print((360-abs(30*h-(11/2)*m)))
else:
    print(abs(30*h-(11/2)*m))