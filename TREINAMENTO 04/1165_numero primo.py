def primo(x):
    cont=1
    div=0

    while x>=cont:
        if x%cont==0:
            div+=1            
        cont+=1            
    if div==2 : return True
    else: return False


nlinhas=int(input())
while nlinhas>0:
    nlinhas-=1
    num=int(input())
    if primo(num): print(f'{num} eh primo')
    else:print(f'{num} nao eh primo')

