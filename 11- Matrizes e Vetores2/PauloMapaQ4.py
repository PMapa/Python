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
    matriz = []
    linhas = valores.split(';')
    for lin in range(len(linhas)):
        linha = preencherVetor(linhas[lin], tipo)
        matriz.append(linha)
    return matriz

def pontosJogos(matriz):
    vpontos=[]
    for lin in range(len(matriz)):
        total=0
        for col in range(len(matriz[lin])):
            if matriz[lin][col]=='1':
                pontos=3
            elif matriz[lin][col]=='0':
                pontos=1
            else:
                pontos=0
            total+=pontos
        vpontos.append(total)
    return vpontos

tim=input('Nomes dos times: ')
times=preencherVetor(tim,'str')

jg=input('Resultados dos jogos: ')
jogos=preencherMatriz(jg,'int')
    
resultado=pontosJogos(jogos)
maior=float('-inf')
for i in range(len(resultado)):
    if resultado[i]>maior:
        maior=resultado[i]
        campeao=times[i]

print(f"Time campeão: {campeao}")
print(f"Pontuação do campeão: {maior}")