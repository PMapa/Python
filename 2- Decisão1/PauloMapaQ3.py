nota=float(input('Média no semestre:'))
freq=int(input('Frequência no semestre:'))
if(freq>=75) and(nota>=6):
        print(f"Conceito: aprovado")
elif(freq>=75) and(nota<6):
    media=6-nota
    print(f"Conceito: exame especial")
    print(f"Justificativa: média {media:.02f} abaixo da mínima")
elif(freq<75):
    falta=75-freq
    print(f"Conceito: reprovado por faltas")
    print(f"Justificativa: frequência {falta:.00f}% abaixo da mínima")
    