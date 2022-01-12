def diferentes(x):     
    while x>0:  
        a=x%10
        z=x//10
        while z>0:        
            if a==z%10: return False
            else:z//=10
        x//=10
    return True
while True:
    try:
        n, m = input().split()
        n=int(n)
        m=int(m)   
        cont=0
        while m>=n:
            if diferentes(n):
                cont+=1
            n+=1       
        print(cont)
    except:break
