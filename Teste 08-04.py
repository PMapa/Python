def vetorPrimo (vetor):
    r=[]
    for i in range (len(vetor)):
        if vetor[i]%2==1:
            r.append(1)
        else:
            r.append(0)
    return r
'''def imprimeVetor(vetor):
    print('[', end='')
    if len(vetor) > 0:
        print(f' {vetor[0]}', end='')
        for i in range(1, len(vetor)):
            print(f', {vetor[i]}', end='')
    print(' ]', end='')
    '''
print('Vetor de inteiros: ')
nV=int(input('Elementos de V? '))

v=[]
for i in range (0,nV):
    elementoI=int(input(f"Elemento[{i}]= "))
    v.append(elementoI)
print('V:')
print(f"{v}")

print('R:')
r=vetorPrimo(v)
print(f"{r}")
'''imprimeVetor(r)'''