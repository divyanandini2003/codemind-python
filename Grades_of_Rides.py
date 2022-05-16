hf,sF,sp=map(int,input().split())
if(hf>50 and sF>60 and sp>100):
    print('10')
elif(hf>50 and sF>60):
    print('9')
elif(sF>60 and sp>100):
    print('8')
elif(hf>50 and sp>100):
    print('7')
elif(hf>50 or sF>60 or sp>100):
    print('6')
else:
    print('5')