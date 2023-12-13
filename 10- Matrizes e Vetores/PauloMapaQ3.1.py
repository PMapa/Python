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

def calculaConsumos(vetor, matriz):
    quiPl=[]
    for i in range (len(matriz)):
        for j in range (len(matriz[0])):
            qPl=matriz[i][j]/vetor[j]
            quiPl.append(qPl)
    return quiPl

capacidade=input('Teste de consumo \nCapacidade dos tanques: \n>>> ')
if capacidade=='':
    print('É necessário pelo menos um automóvel')
else:
    capacV=preencherVetor(capacidade, 'float')

    quilometragens=input('Quilometragens dos condutores: \n>>> ')
    if quilometragens=='':
        print('Deve haver pelo menos um condutor')
    else:
        quiloM=preencherMatriz(quilometragens, 'float')

        if len(quiloM[0]) != len(capacV):
            print('Quantidade de automóveis incompatível')
        else:
            print('Consumos km/l:')
            kmpl=calculaConsumos(capacV,quiloM)
            print(kmpl)