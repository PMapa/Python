#Definindo funções
def SomaPar (a):
    somap=0
    if a%2==0:
        somap+=a
    return somap
def SomaImpar (a):
    somai=0
    if a%2==1:
        somai+=a
    return somai
#Início do programa
n1=int(input('N1: '))
n2=int(input('N2: '))
while (n2<n1):
    n2=int(input('N2: '))
#Somatório
somaPar=0
somaImpar=0
for x in range (n1,n2+1): 
    retornoP=SomaPar(x)
    retornoI=SomaImpar(x)
    somaPar+=retornoP
    somaImpar+=retornoI
#Impressões
print(f"Somatório de números pares em [{n1}, {n2}]: {somaPar}")
print(f"Somatório de números ímpares em [{n1}, {n2}]: {somaImpar}")
