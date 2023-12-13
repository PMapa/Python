n=int(input('Informe o número que deseja calcular o Fatorial:'))
fat=1
i=1
while (n<=0):
    n=int(input('Número inválido, defina outro:'))
while (i<=n):
    fat=fat*i
    i+=1
print(F"O Fatorial de {n} é: {fat}")
