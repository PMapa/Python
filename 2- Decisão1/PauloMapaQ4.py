Peso=float(input('Digite seu peso (em kg):'))
Altura=float(input('Digite sua altura (em metros):'))
Sexo=str(input('Seu sexo é masculino (M) ou feminino (F):'))
IMC=Peso/Altura**2
if(Sexo=="M"):
    if(IMC>25):
        peso=25*Altura**2
        perder=Peso-peso
        print(f"Você deve perder {perder:.02f}kg para ter IMC = 25")
    else:
        print(f"Você não precisa perder peso para ter IMC <= 25") 
else:
    if(Sexo=="F"):
        if(IMC>24):
            peso=24*Altura**2
            perder=Peso-peso
            print(f"Você deve perder {perder:.02f}kg para ter IMC = 24")
        else:
            print(f"Você não precisa perder peso para ter IMC <= 24")    
    else:
        print(f"A entrada contém dados não reconhecidos")