M14=float(input('Média móvel dos últimos 14 dias:'))
A6=int(input('Somatório dos casos dos últimos 6 dias:'))
H=int(input('Quantidade de casos de hoje:'))
M7=(H+A6)/7
d=M7-M14
TXC=(d/M14)*100
if(TXC<0):
    txc=TXC*-1
    print(f"Casos diminuindo em {txc:.02f}%")
else:
    if(TXC<=15):
        print(f"Casos estáveis em {TXC:.02F}%")
    else:
        if(TXC>15):
            print(f"Casos aumentando em {TXC:.02f}%") 