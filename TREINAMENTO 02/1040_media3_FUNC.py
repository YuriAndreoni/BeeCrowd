def media_inicial(n1, n2, n3, n4):
    return (n1*2 + n2*3 + n3*4 + n4) / 10

def media_final(mi, exame):
    return (mi + exame) / 2

n1, n2, n3, n4 = input().split()
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

mi = media_inicial(n1, n2, n3, n4)
print(f'Media: {mi:.1f}')
if mi >= 7.0:
    print('Aluno aprovado.')
elif mi < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    mf = media_final(mi, exame)
    if mf >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {mf:.1f}')
