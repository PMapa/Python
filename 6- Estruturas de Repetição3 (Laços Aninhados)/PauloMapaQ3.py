horas=int(input('Informe a quantidade de horas: '))
salto=int(input('Informe o tamanho do salto: '))

while salto<1 or salto>60 or (60%salto)!=0:
    print('Salto inválido')
    salto=int(input('Informe o tamanho do salto: '))

a=60-salto
for x in range (horas-1,-1,-1):
    print(f"{x+1}:0")
    for y in range (a,0,-salto):
        print(f"{x}:{y}")
    
print('É hora da inauguração.')