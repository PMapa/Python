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

def dimensaoMatriz(matriz):
    linha = len(matriz)
    coluna = len(matriz[0])
    return linha, coluna

def calculaConsumos(cap, qui):
    vetor = []
    matriz = []
    for i in range(len(qui)):
        for j in range(len(cap)):
            g = float(qui[i][j])/float(cap[j])
            vetor.append(g)
        matriz.append(vetor)
        vetor = []
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
    if len(vetor) > 0:
        print(f' {vetor[0]:.2f}', end='')
        for i in range(1, len(vetor)):
            print(f', {vetor[i]:.2f}', end='')
    print(' ]', end='')

capacidade=input('Teste de consumo \nCapacidade dos tanques: \n>>> ')
if capacidade=='':
    print('É necessário pelo menos um automóvel')
else:
    capacV=preencherVetor(capacidade, 'float')

    quilometragens=input('Quilometragens dos condutores: \n>>> ')
    if quilometragens=='':
        print('Deve haver pelo menos um condutor')
    else:
        quiloM=preencherMatriz(quilometragens, 'str')

        cond, aut=dimensaoMatriz(quiloM)
        if aut != len(capacV):
            print('Quantidade de automóveis incompatível')
        else:
            print('Consumos km/l:')
            kmpl=calculaConsumos(capacV,quiloM)
            imprimeMatriz(kmpl)