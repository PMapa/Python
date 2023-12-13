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

def produtoMaisVendido(prod,qtd):
    matriz=[]
    vetor=[]
    soma=0
    for i in range(len(prod)):
        for j in range(len(qtd[i])):
            soma=sum(qtd[i])
        vetor.append(soma)
    matriz.append(vetor)
    vetor=[]
    return matriz

produtos=input('Nomes dos produtos: ')
prod=preencherVetor(produtos,'str')

quantidade=input('Quantidades de vendas: ')
qtd=preencherMatriz(quantidade, 'int')

produto=produtoMaisVendido(prod,qtd)
maior=float('-inf')
for i in range(len(prod)):
    for j in range(len(produto)):
        if produto[j][i]>maior:
            maior=produto[j][i]
            produt=prod[i]
            
print(f'Produto selecionado: {produt}')
print(f'Total de vendas do produto: {maior}')