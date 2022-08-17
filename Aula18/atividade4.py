while True:
    num=int(input('Informe um número inteiro para ver sua tabuada: '))
    if num<0:
        print('Programa Finalizado...')
        break
    for c in range(1,11):
        print('{} X {} = {}'.format(num,c,num*c))

#----------------------------------------------JEITO DA PROFE---------------------------------------------------------
while True:
    n=int(input('Quer ver a tabuada de qual número: '))
    if n<0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
print('Programa tabuada encerrado')