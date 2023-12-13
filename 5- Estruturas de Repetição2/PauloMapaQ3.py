nome1=str(input('Digite o nome do candidato 1: '))
n1=int(input('Digite o número do candidato 1: '))
nome2=str(input('Digite o nome do candidato 2: '))
n2=int(input('Digite o número do candidato 2: '))
eleitores=int(input('Digite a quantidade de eleitores: '))
while (eleitores<3):
    print('A quantidade de eleitores é inferior a 3')
    eleitores=int(input('Digite a quantidade de eleitores: '))
    
print()
print('## Votação Iniciada')
votos1=0
votos2=0
votosI=0
for x in range (0,eleitores):
    voto=int(input('Digite o número do candidato que você deseja votar: '))
    if (voto==n1):
        votos1+=1
    elif (voto==n2):
        votos2+=1
    else:
        votosI+=1
print('## Votação Encerrada')
print()

votosV=eleitores-votosI

print(f"Votos válidos: {(votosV*100)/eleitores:.02f}% ({votosV} votos)")
print(f"Votos inválidos: {(votosI*100)/eleitores:.02f}% ({votosI} votos)")
if votosV>0:
    print(f"Votos para {nome1}: {(votos1*100)/votosV:.02f}% ({votos1} votos)")
    print(f"Votos para {nome2}: {(votos2*100)/votosV:.02f}% ({votos2} votos)")
