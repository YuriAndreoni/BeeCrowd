def add_quad1(linhas):
    quadrantes=[]
    l=0
    c=0
    while l<=6:
        while c<=6:
            quadrante=add_quad2(l,c,linhas)
            quadrantes.append(quadrante)
            c+=3
        c=0
        l+=3
    return quadrantes


def add_quad2(l,c,tabela):
    quad=[]         
    for x in range(l,l+3):
        for y in range(c,c+3):            
            quad.append(linhas[x][y])  
    
    return quad


def add_col1(linhas):
    colunas=[]
    for y in range(9): 
        x=add_col2(y,linhas)    
        colunas.append(x)
    return colunas


def add_col2(y,linhas):
    coluna=[]
    for x in range(9):
        coluna.append(linhas[x][y])
    return coluna


def verifica_l1(tipos):
    for lista in tipos:
        verificacao=verifica_l2(lista)
        if verificacao==False: return False
    return True

def verifica_l2(x):
    conttrue=0    
    for n in x:
        if x.count(n)!=1:            
            return False    
    else: return True              
   

k=int(input())
for testes in range(k): 
    linhas=[]
    for _ in range(9):
        linha=input().split()
        for n in range(len(linha)):
            linha[n]=int(linha[n])
        linhas.append(linha)


    l_colunas=add_col1(linhas)
    l_quadrantes=add_quad1(linhas)

    
    v_linhas=verifica_l1(linhas)      
    v_col=verifica_l1(l_colunas) 
    v_quad=verifica_l1(l_quadrantes)
        

    if v_quad==True and v_col==True and v_linhas==True:
        print(f'Instancia {testes+1}\nSIM\n')
    else:print(f'Instancia {testes+1}\nNAO\n')








    
        
    
