def naoiguais(x):
    if x<11: return True
    else:
        while True:    
            if x==0: break
            else:
                a=x%10
                z=x//10
                while True:        
                    if z==0:break
                    elif a==z%10: return False
                    else:z//=10
                x//=10
        return True
n, m = input().split()
n=int(n)
m=int(m)   
cont=0
while m>=n:
    if naoiguais(n):
        cont+=1
    n+=1       
print(cont)
    
