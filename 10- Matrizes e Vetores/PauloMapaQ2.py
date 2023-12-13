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

def notasAlunos(vetor, matriz):
    notas = []
    acerto = 0
    for i in range (len(matriz)):
        acerto = 0
        for j in range (len(matriz[0])):
            if(vetor[j] == matriz[i][j]):
                acerto = acerto + 1
        notas.append(acerto)
    for i in range (len(notas)):
        notas[i] = (notas[i] * 10)/(len(vetor))
    return notas

print('Notas de BCC701')
print('Digite o gabarito: ')
gabarito=input('>>> ').upper()
vetorGab=preencherVetor(gabarito, 'str')

print('Digite as respostas dos alunos:')
notas=input('>>> ').upper()
if notas=='':
    print('Nenhum aluno para avaliar')
else:
    matrizNot=preencherMatriz(notas, 'str')
    
    l, c= dimensaoMatriz(matrizNot)
    if c!=len(vetorGab):
        print('Quantidade de questões incompatível')
        
    else:
        notaAlunos=notasAlunos(vetorGab, matrizNot)
        print(f"{notaAlunos}")
        