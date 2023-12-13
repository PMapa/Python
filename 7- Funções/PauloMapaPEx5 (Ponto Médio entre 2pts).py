def pontoMédio (a1,b1,a2,b2):
    am=(a1+a2)/2
    bm=(b1+b2)/2
    return (am, bm)

print('Digite as coordenadas (x1, y1) e (x2, y2)')
x1=int(input('x1= '))
y1=int(input('y1= '))
x2=int(input('x2= '))
y2=int(input('y2= '))

xm, ym = pontoMédio(x1,y1,x2,y2)

print('Coordenadas:')
print(f"({x1:4.1f}, {y1:4.1f})")
print(f"({x2:4.1f}, {y2:4.1f})")
print('Ponto Médio:')
print(f"({xm:4.1f}, {ym:4.1f})")
