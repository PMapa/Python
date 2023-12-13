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

def exameEspecial(notas):
    ExameEspecial = []
    for i in range (len(notas)):
        if notas[i] >= 3 and notas[i] <6:
            ExameEspecial.append(i)
    return ExameEspecial

def imprimeVetor(vetor):
    print('[', end='')
    if len(vetor) > 0:
        print(f' {vetor[0]}', end='')
        for i in range(1, len(vetor)):
            print(f', {vetor[i]}', end='')
    print(' ]', end='')
    
notas = input('Notas: ')
nomes = input('Nomes: ')
Notas = preencherVetor(notas,'float')
Nomes = preencherVetor(nomes,'str')
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
    print(f"{Notas[indicesAcimaMedia[0]]:.1f} ({Nomes[indicesAcimaMedia[0]]})", end="")
    for i in range(1, len(indicesAcimaMedia)):
        print(f", {Notas[indicesAcimaMedia[i]]:.1f} ({Nomes[indicesAcimaMedia[i]]})", end="")
print(' ]', end="")

print('')
print('Índices das notas para Exames Especiais:')
notasExameEspecial = exameEspecial(Notas)
imprimeVetor(notasExameEspecial)

print('')
print('Notas para Exames Especiais:')
print('[', end="")
if len(notasExameEspecial) > 0:
    print(f"{Notas[notasExameEspecial[0]]:.01f} ({Nomes[notasExameEspecial[0]]})", end="")
    for i in range(1, len(notasExameEspecial)):
        print(f", {Notas[notasExameEspecial[i]]:.01f} ({Nomes[notasExameEspecial[i]]})", end="")
print(' ]', end="")