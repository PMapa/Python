dsj=str(input('Deseja imprimir um retângulo? (s/n) ')).upper()

while (dsj=='S'):
    a=int(input('Altura do retângulo: '))
    l=int(input('Largura do retângulo: '))
    while (a<=0) or (l<=0) or (l<a):
        print('Valor inválido.')
        print()
        a=int(input('Altura do retângulo: '))
        l=int(input('Largura do retângulo: '))
        print()
    
    for y in range (0,a):
        print(f"{l*'*'}")
    print() 
    dsj=str(input('Deseja imprimir outro retângulo? (s/n) ')).upper()