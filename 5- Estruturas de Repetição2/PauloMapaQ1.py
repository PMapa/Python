n=int(input('Número de termos: '))
r=int(input('Raio da esfera: '))
pi=0

for x in range (0,n,1):
    pi+=((-1)**x*4)/(2*x+1)

V=(4*pi*(r**3))/3
print(f"pi = {pi:.10f}.")
print(f"Volume da esfera = {V:.10f}.")