n1, n2, n3, n4=input().split()
n1=float(n1)
n2=float(n2)
n3=float(n3)
n4=float(n4)
media=(n1*0.2)+(n2*0.3)+(n3*0.4)+(n4*0.1)
print(f'Media: {media:.1f}')
if media>=7:
    print('Aluno Aprovado')
elif media<5:
    print('Aluno Reprovado')
