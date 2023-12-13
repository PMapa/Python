#Funções
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

def imprimeVetor(vetor):
    print("[", end=' ')
    if len(vetor) > 0:
        print(f" {vetor[0]}", end=" ")
        for i in range(1, len(vetor)):
            print(f", {vetor[i]}", end=" ")
    print(" ]", end=' ')
    
def estatNotas (vetor):
    maior = float('-inf')
    menor = float('inf')
    total = 0
    for i in range (len(vetor)):
        if(vetor[i] > maior):
            maior = vetor[i]
        if(vetor[i] < menor):
            menor = vetor[i]
        total = total + vetor[i]
    media = total / len(vetor)
    return maior, menor, media

def AcimaMedia (notas, corte):
    acima = []
    for i in range(0,len(notas)):
        if(notas[i] > corte):
            acima.append(i)
    return acima
#Entrada do Programa
notas=str(input("Nota: "))
notas=preencherVetor(notas,'float')
maior, menor, media = estatNotas(notas)
print(f"Maior nota: {maior:.01f}")
print(f"Menor nota: {menor:.01f}")
print(f"Nota média: {media:.01f}")