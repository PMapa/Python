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

def criarVetor(qtdElementos, valorPadrao):
    vetor = [ ]
    for i in range(qtdElementos):
        vetor.append(valorPadrao)
    return vetor

def contabilizarDemandas(idades):
    vetor=criarVetor(4,0)
    mOitenta=0
    mSessenta=0
    mQuarenta=0
    mDezoito=0
    for i in range (len(idades)):
        if(idades[i] >= 85):
            mOitenta+=1
        elif(idades[i] >= 65):
            mSessenta+=1
        elif (idades[i] >= 45):
            mQuarenta+=1
        elif (idades[i] >= 18):
            mDezoito+=1
    vetor[0]=mOitenta
    vetor[1]=mSessenta
    vetor[2]=mQuarenta
    vetor[3]=mDezoito
    return vetor

def avaliaAtendimento (vacinas, demandas):
    true = 0
    false = 0
    for i in range (4):
        if(vacinas[i] >= demandas[i]):
            true = true + 1
        else:
            false = false + 1
    if(true == 4):
        return True
    else:
        return False

idadesH=input('Defina as idades dos habitantes: ')
idades=preencherVetor(idadesH,'int')

demandas=contabilizarDemandas(idades)
print('Demandas a serem atendidas por faixa etária: ')
print(f". >= 85.........: {demandas[0]}")
print(f".  < 85 e >= 65.: {demandas[1]}")
print(f".  < 65 e >= 45.: {demandas[2]}")
print(f". >= 18.........: {demandas[3]}")

vacinas = input("Defina as disponibilidades de vacinas: ")
vacinas = preencherVetor(vacinas,'int')
suficiente = avaliaAtendimento (vacinas, demandas)

if(suficiente == True):
    print("A quantidade de vacinas é suficiente. ")
else:
    print("Infelizmente, precisaremos de mais vacinas. ")