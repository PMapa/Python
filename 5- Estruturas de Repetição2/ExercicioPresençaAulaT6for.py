print(f"Cálculo da Média dos Pares")
contador=int(input('Quantos elementos seram digitados? '))
if (contador<1):
    print('Número de elementos abaixo do necessário para calcular a média.')  
else:
    qtd=0
    soma=0
    nro=int(input('Digite um número natural: '))
    for x in range (1,contador):
        if ((nro%2)==0):
            soma+=nro
            qtd+=1
        nro=int(input('Digite um número natural: '))  
    if (qtd==0):
        print('Não foi digitado nenhum número par... Não é possível calcular a média!')
    else:
        mediaPar=soma/qtd
        print(f"Media dos Pares: {mediaPar:8.3f}")
        print(f"Quantidade de Pares: {qtd}")
        print('Fim do Programa!')