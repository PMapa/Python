def preencherVetor(valores, tipo):
    vetor = [ ]
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

def calculaLucros(a,b,x,y):
    vetLucro=[]
    for i in range(len(coxinhas)):
        lucro=coxinhas[i]*undCox+quibes[i]*undQui
        vetLucro.append(lucro)
    return vetLucro

def imprimeVetor(vetor):
    print('[', end='')
    if len(vetor) > 0:
        print(f' {vetor[0]}', end='')
        for i in range(1, len(vetor)):
            print(f', {vetor[i]}', end='')
    print(']', end='')


vendasC=input('Vendas de coxinhas: ')
vendasQ=input('Vendas de quibes: ')
coxinhas=preencherVetor(vendasC,'int')
quibes=preencherVetor(vendasQ,'int')

if len(coxinhas) != len(quibes):
    print('Dados de vendas inválidos')
else:
    undCox=float(input('Lucro por unidade de coxinha: R$ '))
    undQui=float(input('Lucro por unidade de quibe: R$ '))
    
    lucro=calculaLucros(coxinhas,quibes,undCox,undQui)
    menor=min(lucro)
    maior=max(lucro)
    print('Lucros: ', end='')
    imp=imprimeVetor(lucro)
    print(f'Maior lucro: R$ {maior:.2f}')
    print(f'Menor lucro: R$ {menor:.2f}')