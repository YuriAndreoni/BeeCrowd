cont=0
pos=1
atual=0
while cont<10:
    a=int(input())
    cont+=1
    if atual<a:
        atual=a
        pos=cont
  
print(atual)
print(pos)
