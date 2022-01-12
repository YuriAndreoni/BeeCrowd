pulo,canos=input().split()
pulo=int(pulo)
canos=int(canos)
l= input().split()

for i in range(len(l)):
    l[i]=int(l[i])

dist=0
for h in range(len(l)-1):
    if abs(l[h]-l[h+1])>pulo:
        print('GAME OVER')
        break
    else: dist+=1
    if dist==canos-1:
        print('YOU WIN')
    

