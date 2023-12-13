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

def comparaVetores (a,b):
    compara=[]
    for i in range(0,len(atual)):
        if anterior[i] > atual[i]:
            parametro='R'
        elif anterior[i] < atual[i]:
            parametro='A'
        else:
            parametro='E'
        compara.append(parametro)
    return compara

def imprimeVetor(vetor):
    print('[', end='')
    if len(vetor) > 0:
        print(f' {vetor[0]}', end='')
        for i in range(1, len(vetor)):
            print(f', {vetor[i]}', end='')
    print(']', end='')
    
def classificaEstado(compara):
    classifica=[]
    contarA=0
    contarR=0
    contarE=0
    for i in range(len(compara)):
        if compara[i]=='A':
            contarA=contarA+1
        elif compara[i]=='R':
            contarR=contarR+1
        else:
            contarE=contarE+1
    if contarA>contarR:
            classifica='Onda Vermelha'
    if contarA<contarR:
            classifica='Onda Verde'
    if contarA==contarR:
            classifica='Onda Amarela'
    return classifica
    
semanaAn=input('Número de mortes na semana anterior: ')
semanaAt=input('Número de mortes na semana atual: ')
anterior=preencherVetor(semanaAn,'int')
atual=preencherVetor(semanaAt,'int')

if len(anterior) != len(atual):
    print(f"Número de elementos incompatível ({len(anterior)} != {len(atual)})")
else:
    print('Classificações das macro-regiões: ')
    comparação=comparaVetores(anterior,atual)
    imp=imprimeVetor(comparação)
    
    classificação=classificaEstado(comparação)
    print('')
    print('Classificação do estado: ', end='')
    print(f'{classificação}')
    