mor=float(input('Quantidade de Morangos (em kg):'))
mac=float(input('Quantidade de Maçãs (em kg):'))
if(mor<0) or (mac<0):
    print('Entrada inválida')
else:
    if(mor<=5) and (mac<=5): 
        vlmor=2.5*mor
        vlmac=1.8*mac
    elif(mor>5) and (mac>5):
        vlmor=2.2*mor
        vlmac=1.5*mac
    elif(mor<=5) and (mac>5):
        vlmor=2.5*mor
        vlmac=1.5*mac
    else:
        vlmor=2.2*mor
        vlmac=1.8*mac
    total=vlmor+vlmac
    print(F"O valor total da sua compra é R${total:.02f}")