import math:
def funçãoF (x):
    return (x- math.sin(x))
def funçãoG (x):
    return (x**3- math.cos(2*x))

print('Cálculo do Somatório')
n=int(input('Quantidade de parcelas do somatório: '))
somatório=0
for i in range (1,n+1):
    somatório+=funçãoF(i)/funçãoG(i)
    
print(f"Valor do Somatório: {somatório:6.4f}")
            