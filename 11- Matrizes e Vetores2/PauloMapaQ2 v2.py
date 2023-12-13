def preencherVetor(valores, tipo):
    vetor = []
    valores = valores.split(',')
    for i in range(len(valores)):
        if tipo == 'int':
            valor = int(valores[i].strip())
        elif tipo == 'float':
            valor = float(valores[i].strip())
        else:
            valor = valores[i].strip()
        vetor.append(valor)
    return vetor
def preencherMatriz(valores, tipo):
    matriz = []
    linhas = valores.split(';')
    for lin in range(len(linhas)):
        linha = preencherVetor(linhas[lin], tipo)
        matriz.append(linha)
    return matriz
notas=input('Notas dos alunos: ')
tp=input('Tipo de nota: ')
tipo=''
if tp=='int':
    tipo='int'
if tp=='real':
    tipo='float'
if tp=='letra':
    tipo='str'
nt=preencherMatriz(notas,tipo)
if tipo=='float' or tipo=='int':
    menor=float('inf')
    for i in range(len(nt)):
        for j in range(len(nt[i])):
            if nt[i][j]<menor:
                menor=nt[i][j]
    pior=menor
else:
    menor=str('A')
    for i in range(len(nt)):
        for j in range(len(nt[i])):
            if nt[i][j]>menor:
                menor=nt[i][j]
    pior=menor
print(f'Pior nota: {pior}')