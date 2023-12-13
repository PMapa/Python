exp=int(input('Anos de experiência:'))
ling=int(input('Linguagens de programação:'))
proj=int(input('Projetos:'))
if(exp>=10) and (ling>=5) and (proj>=10):
    print('Concorrendo à Vaga Sênior.')
else:
    if(exp>=3) and (ling>=3) and (proj>=5):
        print(F"Cncorrendo à Vaga Pleno. Para concorrer a Vaga Senior faltam:")
        if(exp<10):
            expF=10-exp
            print(F" -{expF} anos de experiência")
        if(ling<5):
            lingF=5-ling
            print(F" -{lingF} linguagens de programação")
        if(proj<10):
            projF=10-proj
            print(F" -{projF} projetos")
    else:
        print(F"Cncorrendo à Vaga Júnior. Para concorrer a Vaga Pleno faltam:")
        if(exp<3):
            expF=3-exp
            print(F" -{expF} anos de experiência")
        if(ling<3):
            lingF=3-ling
            print(F" -{lingF} linguagens de programação")
        if(proj<5):
            projF=5-proj
            print(F" -{projF} projetos")