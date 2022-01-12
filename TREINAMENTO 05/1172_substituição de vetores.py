x=[]
for _ in range(10):
    x.append (int(input()))
pos=0
for n in x:
    if n<=0: n=1
    print(f'X[{pos}] = {n}')
    pos+=1
      
             
