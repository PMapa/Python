def preencherMatriz(valores, tipo):
    matriz = [ ]
    linhas = valores.split(';')
    for lin in range(len(linhas)):
        colunas = linhas[lin].split(',')
        vetor = [ ]
        for col in range(len(colunas)):
            if tipo == 'int':
                valor = int(colunas[col].strip())
            elif tipo == 'float':
                valor = float(colunas[col].strip())
            else:
                valor = colunas[col].strip()
            vetor.append(valor)
        matriz.append(vetor)
    return matriz

def linhaMenorValor(matriz):
    import math
    menor = math.inf
    for i in range (len(matriz)):
        for j in range (len(matriz[0])):
            if(matriz[i][j] < menor):
                indL = i
                menor = matriz[i][j]
    return indL

def colunaMaiorValor(matriz, indL):
    import math
    maior = -math.inf
    for i in range (len(matriz[indL])):
        if(matriz[indL][i] > maior):
            indC = i
            maior = matriz[indL][i]
    return indC

print('MinMax de uma Matriz')
print('Valores da matriz:')
valorMatriz=input('>>> ')
matriz=preencherMatriz(valorMatriz, 'int')

índiceLin=linhaMenorValor(matriz)
índiceCol=colunaMaiorValor(matriz, índiceLin)

elemento=matriz[índiceLin][índiceCol]

print(f"MinMax: [{índiceLin}, {índiceCol}] = {elemento}")