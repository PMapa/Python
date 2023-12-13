T=float(input('Capital Total para empréstimo: '))
C=float(input('Capital emprestado: '))
while (T>=C):
    m=int(input('Quantidade de meses para quitação: '))
    if (C<=10000):
        t=0.10
    else:
        t=0.07
    J=C*t*m
    T=T-C
    print(F"Taxa de juros aplicada:{t*100:.00f}%")
    print(F"Juros devido: {J:.02f}.")
    print(F"Valor total: {J+C:.02f}.")
    C=float(input('Capital emprestado: '))
print(F"Empréstimo negado, capital total é de R$ {T:.02f}.")