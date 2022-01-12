n=int(input())
while n>0:
    maria = 3
    joao = 3
    pont_totalj=0
    pont_totalm=0

    while joao>0:      

        x,d = input().split()       
        pont_totalj+=int(x)*int(d)
        joao-=1
    
    while maria>0:        

        x,d = input().split()        
        pont_totalm+=int(x)*int(d)
        maria-=1

    if pont_totalj>pont_totalm:
        print('JOAO')
    else:
        print('MARIA')

    n-=1

    
    
        
