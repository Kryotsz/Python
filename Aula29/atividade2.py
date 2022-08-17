def converte(horas,minutos):
        if horas==00:
            h=12
        elif horas<=12:
            h=horas
        else:
            h=horas-12
        horario=(f'{h}:{minutos}')
        return horario

def meridiano(horas):
        if horas<12:
            meridiano='A.M.'
        else:
            meridiano='P.M.'
        return meridiano

while True:
    print('Digite 999 para sair.')
    horas=int(input('Informe as horas: '))
    minutos=int(input('Informe os minutos: '))

    if horas==999 or minutos==999:
        break

    print('~'*40)
    print(f'O horário em 24 horas é: {horas}:{minutos} \nO horário em 12 horas é: {converte(horas,minutos)} {meridiano(horas)}')
    print('~'*40)

#------------------------------------------------------JEITO DA SORA-------------------------------------------------
def horario(hora, minuto):
    b=hora/12

    if b<=1:
        h=str(hora)
        print(f'Sua hora: {h}:', end='')
    elif b>1 and b<=2:
        h=str(hora-12)
        print(f'Sua hora: {h}:', end='')
    if b<=1 and minuto<=60:
        print(f'{minuto} A.M')
    elif b>1 and minuto<=60:
        print(f'{minuto} P.M')

while True:
    print('Digite 999 para sair.')
    h=int(input('Informe a hora: '))
    if h==999:
        break
    m=int(input('Informe os minutos: '))
    horario(h,m)