inicio = int(input())
fim = int(input())

if inicio > fim:
    temp = inicio
    inicio = fim
    fim = temp

soma = 0
i = inicio + 1

while i < fim:
    if i % 2 != 0:
        soma += i
    i += 1

print(soma)
    
