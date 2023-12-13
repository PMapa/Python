n=int(input('Digite um número: '))
while (n>0):
    d=1
    soma=0
    while (d<n):
        if (n%d)==0:
            soma=soma+d
        d+=1
    if (soma==n):
        print(F"{n}=={n} é um número perfeito")
    else:
        print(F"{n}<>{soma} não é um número perfeito")
    n=int(input('Digite um número: '))