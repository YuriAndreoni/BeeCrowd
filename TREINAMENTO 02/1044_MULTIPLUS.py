a, b = input().split()
a=int(a)
b=int(b)
if a>=b:
    multi=a%b
else:
    multi=b%a
if multi==0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')
    
