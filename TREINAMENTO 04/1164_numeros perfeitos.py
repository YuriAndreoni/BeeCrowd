def nperfeito(n):    
    s_div=0    
    for divisor in range(1,n):
        if n%divisor==0:
            s_div+=divisor            
    if s_div==n: return True
    else: return False

x=int(input())

for _ in range(x):

    n=int(input())

    if nperfeito(n):
        print(f'{n} eh perfeito')
    else:
        print(f'{n} nao eh perfeito')
    
