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

def localizaMenorValor(matriz):
    resp = (0, 0)
    for lin in range(len(matriz)):
        for col in range(len(matriz[lin])):
            if matriz[lin][col] < matriz[resp[0]][resp[1]]:
                menor = matriz[lin][col]
                resp = (lin, col)
    return menor

print('Conversão de vetor em matriz')
notas=input('Notas dos alunos: ')
tp=input('Tipo de nota: ')

if tp=='int':
    tip='int'
elif tp=='real':
    tip='float'
else:
    tip='str'

nts=preencherMatriz(notas,tip)

if tip=='float' or tip=='int':
    menor=float('inf')
    for i in range(len(nts)):
        for j in range(len(nts[i])):
            if nts[i][j]<menor:
                menor=nts[i][j]
    pior=menor
else:
    menor=str('A')
    for i in range(len(nts)):
        for j in range(len(nts[i])):
            if nts[i][j]>menor:
                menor=nts[i][j]
    pior=menor

print(f"Pior nota: {pior}")