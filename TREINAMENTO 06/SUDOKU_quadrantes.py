def quad1(linhas):
    quadrantes=[]
    l=0
    c=0
    while l<=6:
        while c<=6:
            quadrante=quad2(l,c,linhas)
            quadrantes.append(quadrante)
            c+=3
        c=0
        l+=3
    return quadrantes





def quad2(l,c,tabela):
    quad=[]         
    for x in range(l,l+3):
        for y in range(c,c+3):
            print(linhas[x][y])
            quad.append(linhas[x][y])  
    
    return quad
    
            
            
    

    





linhas=[[1, 3, 2, 5, 7, 9, 4, 6, 8], [4, 9, 8, 2, 6, 1, 3, 7, 5], [7, 5, 6, 3, 8, 4, 2, 1, 9], [6, 4, 3, 1, 5, 8, 7, 9, 2], [5, 2, 1, 7, 9, 3, 8, 4, 6], [9, 8, 7, 4, 2, 6, 5, 3, 1], [2, 1, 4, 9, 3, 5, 6, 8, 7], [3, 6, 5, 8, 1, 7, 9, 2, 4], [8, 7, 9, 6, 4, 2, 1, 5, 3]]


x=quad1(linhas)


    
        
    
