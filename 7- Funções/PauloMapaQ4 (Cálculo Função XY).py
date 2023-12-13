def f (x,y):
    fX=(x**2)+(2*x*y)+y
    return fX
def g (x,y):
    gX=(y**2)+(2*x*y)+x
    return gX

a=int(input('a: '))
while a<0:
    a=int(input('a: '))
b=int(input('b: '))
while b<=a or b<0:
    b=int(input('b: '))
p=int(input('p: '))
while p<0 or p>a:
    p=int(input('p: '))
print(f"Intervalo definido: [ {a}, {b} ], com passo {p}.")
print()
print('x, y, f(x,y), g(x,y)')
for i in range (a,b+1,p):
    for j in range (a,b+1,p):
        f1=f(i,j)
        f2=g(i,j)
        print(f"{i}, {j}, {f1}, {f2} ")
