print(f"Cálculo da Média dos Pares")
qtd=0
soma=0
nro=int(input('Digite um número natural: '))
while (nro>=0):
    if ((nro%2)==0):
        soma+=nro
        qtd+=1
    nro=int(input('Digite um número natural: '))
mediaPar=soma/qtd
print(f"\nMedia dos Pares: {mediaPar:8.3f}")
print(f"Quantidade de Pares: {qtd}")
print('Fim do Programa!')