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

        

col=int(input())
Op=input()
tabela=preenche()


acumuladora=0
cont=0
for l in range(0,12):
    for n in range(col,col+1):
        print(f'[{l}][{n}]')

        acumuladora+=tabela[l][n]
        cont+=1
        

    
        
    
        
        
if Op=='S': print(f'{acumuladora:.1f}')
else: print(f'{acumuladora/cont:.1f}') 
        
    
    
    
    

                                                






    
        
    
