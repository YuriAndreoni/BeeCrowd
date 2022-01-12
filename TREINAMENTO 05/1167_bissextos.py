inicio=int(input())
fim=int(input())

cont=0
for n in range(inicio,fim+1):
    if n%100!=0 and n%4==0 or n%400==0:          
            print(n)
            cont+=1
print(f'bissextos:{cont}')
