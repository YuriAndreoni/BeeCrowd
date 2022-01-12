def conv(n,atb):
    for _ in range(n):
        atb[_]=int(atb[_])
    return atb


def atributos(n):    
    atb=input().split()
    atb=conv(n,atb)
    return atb      



while True:
    try:
        n_atb=int(input())
        m,l=input().split()
        m=int(m)
        l=int(l)
        bm=[]
        bl=[]
        for carta in range(m):
            bm.append(atributos(n_atb))
            

        for carta in range(l):
            bl.append(atributos(n_atb))

        cm,cl=input().split()
        cm=int(cm)
        cl=int(cl)
        atb_sorteio=int(input())

        print(f'marcos={bm[cm-1][atb_sorteio-1]} Leo={bl[cl-1][atb_sorteio-1]}')
        if   bm[cm-1][atb_sorteio-1]>bl[cl-1][atb_sorteio-1]: print('Marcos')
        elif bm[cm-1][atb_sorteio-1]<bl[cl-1][atb_sorteio-1]: print('Leonardo')
        else: print('Empate')
    except:
        break
                                                






    
        
    
