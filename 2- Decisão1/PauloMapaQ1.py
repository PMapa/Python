C=float(input('Capital emprestado:'))
m=int(input('Quantidade de meses para quitação:'))
if(C<=10000):
    t=0.1
    T=t*100
else:
    if(C>10000):
        t=0.07
        T=t*100
J=C*t*m
VT=C+J
print(f"Taxa de juros aplicada:{T:.00f}%")
print(f"Juros devido:{J:.02f}")
print(f"Valor total:{VT:.02f}")