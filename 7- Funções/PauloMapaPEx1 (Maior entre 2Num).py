def maior2Num (a,b):
    if a>b:
        return a
    else:
        return b
    
print('Definindo o maior de 2 Valores')
x=float(input('Digite o primeiro número: '))
y=float(input('Digite o segundo número: '))

resultado=maior2Num(x,y)
print(f"Maior número entre {x} e {y} = {resultado}")