#Definindo funções
def SomaPar (a,b):
    somap=0
    for i in range (a,b+1):
        if i%2==0:
            somap+=i
    return somap
def SomaImpar (a,b):
    somai=0
    for i in range (a,b+1):
        if i%2==1:
            somai+=i
    return somai
#Início do programa
n1=int(input('N1: '))
n2=int(input('N2: '))
while (n2<n1):
    n2=int(input('N2: '))
#Somatório
somaPar=SomaPar(n1,n2)
somaImpar=SomaImpar(n1,n2)

#Impressões
print(f"Somatório de números pares em [{n1}, {n2}]: {somaPar}")
print(f"Somatório de números ímpares em [{n1}, {n2}]: {somaImpar}")