q=int(input('Digite a quantidadede lados:'))
if(q<3):
    print('Não é um polígono')
elif(q>5):
    print('Polígono não identificado')
else:
    L=float(input('Digita a medida do lado:'))
    if(q==3):
        A=(L**2)*(3**0.5)/4
        print(F"O polígono é um triângulo com área: {A:.02f}")
    elif(q==4):
        A=L**2
        print(F"O polígono é um quadrado com área: {A:.02f}")
    elif(q==5):
        A=((3*(L**2)*(3**0.5))/2)
        print(F"O polígono é um pentágono com área: {A:.02f}")

