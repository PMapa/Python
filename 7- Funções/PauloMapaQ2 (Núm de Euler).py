#Definindo funções
def SomaPar (a):
    resto=a%2
    if (resto==0):
        return True
def SomaImpar (a):
    resto=a%2
    if (resto!=0):
        return False

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
    if retornoP is True:
        somaPar+=x
    else:
        somaImpar+=x
#Impressões
print(f"Somatório de números pares em [{n1}, {n2}]: {somaPar}")
print(f"Somatório de números ímpares em [{n1}, {n2}]: {somaImpar}")
