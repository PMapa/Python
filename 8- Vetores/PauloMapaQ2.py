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

def estatNotas(notas):
    Maior = float('-inf')
    Menor = float('inf')
    n = 0
    soma = 0
    for i in range (len(notas)):
        n = notas[i]
        if n > Maior:
            Maior = n
        if n < Menor:
            Menor = n
        soma += n
    Media = soma / len(notas)
    return Maior, Menor, Media

def acimaMedia(notas, media):
    vetorIndice = []
    for i in range (len(notas)):
        if notas[i] > media:
            vetorIndice.append(i)
    return vetorIndice

def imprimeVetor(vetor):
    print('[', end="")
    if len(vetor) > 0:
        print(f" {vetor[0]}", end="")
        for i in range(1, len(vetor)):
            print(f', {vetor[i]}', end="")
    print(' ]', end="")
    
notas = input('Notas: ')
Notas = preencherVetor(notas,'float')
maior,menor,media = estatNotas(Notas)
print(f"Maior nota: {maior:.01f}")
print(f"Menor nota: {menor:.01f}")
print(f"Nota média: {media:.01f}")
print('Índices das notas acima da média:')

indicesAcimaMedia = acimaMedia(Notas, media)
imprimeVetor(indicesAcimaMedia)
print('')
print('Notas acima da média:')
print('[', end='')
if len(indicesAcimaMedia) > 0:
    print(f" {Notas[indicesAcimaMedia[0]]:.01f}", end="")
    for i in range(1, len(indicesAcimaMedia)):
        print(f", {Notas[indicesAcimaMedia[i]]:.01f}", end="")
print(' ]', end="")
