nome=str(input('Informe o nome do juiz: '))
np=int(input('Quantidade de partidas: '))
pt=1
somai=0
somaf=0
somac=0
somat=0

print()
for x in range (0,np):
    print(f"Partida {pt}:")
    i=int(input('. Impedimentos.......: '))
    f=int(input('. Faltas.............: '))
    c=int(input('. Cartões............: '))
    t=float(input('. Tempo de acréscimo.: '))
    print()
    somai+=i
    somaf+=f
    somac+=c
    somat+=t
    pt+=1
    
print(f"Estatísticas do juiz {nome}: ")
print(f". Impedimentos.......: {(somai/np):.02f}. ")
print(f". Faltas.............: {(somaf/np):.02f}. ")
print(f". Cartôes............: {(somac/np):.02f}. ")
print(f". Tempo de acréscimo.: {(somat/np):.02f}. ")