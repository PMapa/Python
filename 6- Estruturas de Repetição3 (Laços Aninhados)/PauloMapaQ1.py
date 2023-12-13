qtdAlunos=int(input('Defina a quantidade de alunos: '))
reprovados=0
emExame=0
aprovados=0
notaR=0
notaE=0
notaA=0

for x in range (1,qtdAlunos+1,1):
    nota=float(input(f'Nota {x}: '))
    while nota<0 or nota>10:
        nota=float(input(f'Nota inválida. Nota {x}: '))
        
    if nota<3:
        reprovados+=1
        notaR+=nota
    elif 3<=nota and nota<6:
        emExame+=1
        notaE+=nota
    else:
        aprovados+=1
        notaA+=nota
        
if reprovados==0:
    reprovados=1
if emExame==0:
    emExame=1
if aprovados==0:
    aprovados=0

print()
print('Estatísticas dos alunos:')

print(f". {reprovados} alunos Reprovados com média {notaR/reprovados:.01f}.")
print(f". {emExame} alunos em Exame Especial com média {notaE/emExame:.01f}.")
print(f". {aprovados} alunos Aprovados com média {notaA/aprovados:.01f}.")