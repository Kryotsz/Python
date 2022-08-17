aprovados=0
reprovados=0

for c in range(1,6):
    nota1=float(input('Informe a primeira nota: '))
    nota2=float(input('Informe a segunda nota: '))
    media=(nota1+nota2)/2
    if media>=7:
        aprovados+=1
    else:
        reprovados+=1
porcentagem=(reprovados*100)/5
print('O percentual de alunos em Prova Final é {:.0f}%'.format(porcentagem))
