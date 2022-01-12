def diferentes(x):
    if x<10: return True
    else:
        while x>0:  
            a=x%10
            z=x//10
            while z>0:        
                if a==z%10: return False
                else:z//=10
                x//=10
        return True
u=diferentes(4564)
print(u)


    
