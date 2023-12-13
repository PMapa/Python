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
    vt=[]
    for i in range (0, len(matriz)):
        for j in range (len(matriz[0])):
            qPl=float(matriz[i][j])/float(vetor[j])
            vt.append(qPl)
        quiPl.append(vt)
        vt=[]
    return quiPl

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
           
def calculaMedias(matriz):
    vetor=[]
    l=len(matriz)
    c=len(matriz[0])
    for i in range (0,c):
        total=0
        contador=0
        for j in range (0,l):
            total+=(matriz[j][i])
            contador+=1
        media=total/contador
        vetor.append(media)
    return vetor

def criarMatriz(qtdLinhas, qtdColunas, valorPadrao):
    matriz = [ ]
    for lin in range(qtdLinhas):
        linha = [ ]
        for col in range(qtdColunas):
            linha.append(valorPadrao)
            matriz.append(linha)
    return matriz

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

        aut=len(quiloM[0])
        if aut != len(capacV):
            print('Quantidade de automóveis incompatível')
        else:
            print('Consumos km/l:')
            kmpl=calculaConsumos(capacV,quiloM)
            imprimeMatriz(kmpl)
          
            print('Médias dos consumos por automóvel:')
            mediaConsumo=calculaMedias(kmpl)
            imprimeVetor(mediaConsumo)
            