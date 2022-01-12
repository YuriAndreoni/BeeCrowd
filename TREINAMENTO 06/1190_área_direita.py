def linhas():
    numeros=[]
    for i in range(12):
        n=float(input())
        numeros.append(n)
    return numeros


def preenche():
    matriz=[]
    for i in range(12):
        linha=linhas()
        matriz.append(linha)
    return matriz

        

Op=input()
tabela=preenche()


for i in tabela:
    print(f'{i}\n')
col=11
acumuladora=0
cont=0
for l in range(1,11):
    for n in range(col,12):
        acumuladora+=tabela[l][n]
        cont+=1
        print(f'[{l}][{n}] end=' '')
    if l<5:col-=1
    if l>5:col+=1
        
        
if Op=='S': print(f'{acumuladora:.2f}')
else: print(f'{acumuladora/cont:.2f}') 
        
    
    
    
    

                                                






    
        
    
