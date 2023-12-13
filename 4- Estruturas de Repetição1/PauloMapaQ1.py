comprimento=float(input('Comprimento de corte dos tubos:'))
erro=float(input('Margem de erro aceitável:'))
quantidade=int(input('Quantidade de tubos demandada:'))
tRejeitados=0
tAceitos=0
i=1
while (i<=quantidade):
    compTcort=float(input('Comprimento do tubd cortado:'))
    if (compTcort>comprimento+erro) or (compTcort<comprimento-erro):
        print('Acima da margem de erro, tudo rejeitado')
        tRejeitados+=1
    else:
        tAceitos+=1
        i+=1
print('Fim da produção, demanda atendida.')
print(F"Total de tubos cortados:{tAceitos+tRejeitados}")
print(F"Total de tubos rejeitados:{tRejeitados}")