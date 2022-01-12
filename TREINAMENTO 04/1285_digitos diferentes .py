def diferentes(x):
    if x<10: return True
    else:
        a=x%10
        x=x//10
        b=x%10
        x=x//10
        if a==b: return False
        elif x==0: return True
        else:
            c=x%10
            x=x//10
            if c==a or c==b: return False
            elif x==0: return True
            elif x==a or x==b or x==c: return False
            else: return True

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
    except: break

       
