print('Caixa aberto!')
pedidos=0
vendido=0
caixa='NÃO'

while caixa!='SIM':
    valor=0
    print()
    quantidade=int(input('Quantidade de itens do pedido: '))
    for x in range (1,quantidade+1,1):
        preço=float(input(f'. Preço do item {x}: '))
        valor+=preço
    deliv=str(input('. Cobrar delivery? ')).upper()
    if deliv=='SIM':
        valor+=15
    print(f". Valor do pedido: R$ {valor:.02f}.")
    pedidos+=1
    vendido+=valor
    caixa=str(input('Fechar caixa? ')).upper()
print()
print('Caixa fechado!')
print(f"Número de pedidos: {pedidos}")
print(f"Valor total vendido: R$ {vendido:.02f}")