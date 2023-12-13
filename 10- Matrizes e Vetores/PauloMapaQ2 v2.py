def criaMatriz (m,n,tipo):
    matriz= [] #definição da matriz vazia
    for i in range (m): # número de linhas, variação lenta
        linha = []
        for j in range (n): #número de colunas, variação rapida
            linha.append(tipo(0))
        matriz.append(linha)
    return matriz

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

def notasAlunos(vetor, matriz):
    notas = []
    acerto = 0
    for i in range (len(matriz)):
        acerto = 0
        for j in range (len(matriz[0])):
            if vetor[j] == matriz[i][j]:
                acerto = acerto + 1
        notas.append(acerto)
    for i in range (len(notas)):
        notas[i] = (notas[i] * 10)/(len(vetor))
    return notas

def imprimeVetor(vetor):
    print('[', end='')
    if len(vetor) > 0:
        print(f' {vetor[0]:.2f}', end='')
        for i in range(1, len(vetor)):
            print(f', {vetor[i]:.2f}', end='')
    print(' ]', end='')
    
print('Notas de BCC701')
print('Digite o gabarito: ')
gabarito=input('>>> ')
vetorGab=preencherVetor(gabarito, 'str')

print('Digite as respostas dos alunos:')
notas=input('>>> ')
matrizNot=preencherMatriz(notas, 'str')

if matrizNot=='':
    print('Nenhum aluno para avaliar')
    
col=len(matrizNot[0])
if col!=len(vetorGab):
    print('Quantidade de questões incompatível')
    
else:
    print('Nota dos alunos:')
    notaAlunos=notasAlunos(vetorGab, matrizNot)
    imprimeVetor(notaAlunos)
        