def Primo (x):
    for w in range(2,x):
        if x%w==0:
            return False
    return True

a=int(input('a: '))
while a<2:
    a=int(input('a: '))
b=int(input('b: '))
while b<a:
    b=int(input('b: '))

print(f"Número primos entre {a} e {b}: ")
for i in range (a,b+1):
    if Primo(i)==True:
        print(f'{i} ', end='')