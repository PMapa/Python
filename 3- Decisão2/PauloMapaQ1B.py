peso=float(input('Informe o peso:'))
altura=float(input('Informe a altura'))
IMC=peso/altura**2
if(IMC<20):
    print(F"Seu IMC é {IMC:.02f}")
    print('IMC abaixo do normal')
else:
    if(IMC<=25):   
        print(F"Seu IMC é {IMC:.02f}")
        print('IMC normal')
    else:
        if(IMC<30):
            print(F"Seu IMC é {IMC:.02f}")
            print('IMC indica sobrepeso')
        else:       
            if(IMC<40):
                print(F"Seu IMC é {IMC:.02f}")
                print('IMC indica obesidade leve a moderada')
            else:
                print(F"Seu IMC é {IMC:.02f}")
                print('IMC indica obesidade mórbida')