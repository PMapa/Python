def preencherVetor (valores, tipo):
    vetor = []
    valores = valores.split (',')
    for i in range(len(valores)):
        if tipo == 'int':
            valor = int (valores[i].strip())
        elif tipo == 'float':
            valor = float (valores[i].strip())
        else:
            valor = valores[i].strip()
        vetor.append(valor)
    return vetor

def criarMatriz(qtdLinhas, qtdColunas, valorPadrao):
    matriz = [ ]
    for lin in range(qtdLinhas):
        linha = [ ]
        for col in range(qtdColunas):
            linha.append(valorPadrao)
            matriz.append(linha)
    return matriz

def imprimeMatriz(matriz):
    if len(matriz) > 0:
        imprimeVetor(matriz[0])
        print('')
        for lin in range(1, len(matriz)):
            imprimeVetor(matriz[lin])
            print('')
            
def imprimeVetor(vetor):
    print('[', end='')
    z=len(vetor)
    if z > 0:
        print(f' {vetor[0]:.0f}', end='')
        for i in range(1, len(vetor)):
            print(f', {vetor[i]:.0f}', end='')
    print(' ]', end='')
    
def converterVetorMatriz(vetor):
    n=len(vetor)
    import math
    raizN=int(math.sqrt(n))
    
    matriz=[]
    vtap=[]
    z=0
    for i in range (raizN):
        for j in range (raizN):
            vtap.append(vetor[z])
            z+=1
        matriz.append(vtap)
        vtap=[]

    return matriz

vt=input('Entrada do vetor: ')
vtr=preencherVetor(vt, 'int')

mtz=converterVetorMatriz(vtr)
print('Matriz correspondente: ')
imprimeMatriz(mtz)