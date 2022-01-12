cont=0
idade=0
a=int(input())
while a>0:    
    cont+=1
    idade+=a
    a=int(input())
media=idade/cont
print(f'{media:.2f}')
    
