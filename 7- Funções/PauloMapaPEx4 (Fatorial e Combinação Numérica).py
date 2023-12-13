def fatorial (a):
    fat=1
    if (a==0) or (a==1):
        return fat
    else:
        for i in range (2,a+1):
            fat*=i
        return fat
    
n=int(input('Digite o valor de n: '))
k=int(input('Digite o valor de k: '))

nF=fatorial(n)
nMkF=fatorial(n-k)
kF=fatorial(k)

combinação=nF/(nMkF*kF)
print(f"n!/((n-k)!k!)={combinação}")