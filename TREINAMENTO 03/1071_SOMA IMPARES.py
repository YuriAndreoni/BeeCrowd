a=int(input())
b=int(input())
if a>b:
    x=a
    y=b
else:
    x=b
    y=a
ac=0
cont=y
while y<x:
    ac+=y
    y+=2
print(ac)
    
