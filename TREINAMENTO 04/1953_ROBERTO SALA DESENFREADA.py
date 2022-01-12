NA=int(input())
epr=0
ehd=0
intrusos=0
while NA>0:
    ra,curso=input().split()   
    if curso== 'EPR':
        epr+=1
    elif curso=='EHD':
        ehd+=1
    else:
        intrusos+=1
    NA-=1
print(f'EPR: {epr}')
print(f'EHD: {ehd}')
print(f'INTRUSOS: {intrusos}')
        
    




