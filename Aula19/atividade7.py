'''
valor=int(input('Informe o valor que quer sacar: '))

total=valor
nota=50
cont=0

while True:
    if total>=nota:
        total-=nota
        cont+=1
    else:
        if cont>0:
            print('Serão entregues {} cédulas de {} reais.'.format(cont,nota))
        if nota==50:
            nota=20
        elif nota==20:
            nota=10
        elif nota==10:
            nota=1
        cont=0
        if total==0:
           break
'''

#---------------------------------------------------------
print('{:^40}'.format('Banco Inf9'))
print('~'*40)
valor=int(input('Informe o valor que quer sacar: R$'))

total=valor
nota=105
cont=1

while True:
    if total>=nota:
        total-=nota
        cont+=1
    else:
        if cont>0:
            print('Serão entregues {} cédulas de {} reais.'.format(cont,nota))
        if nota==100:
            nota=50
        elif nota==50:
            nota=20
        elif nota==20:
            nota=10
        elif nota==10:
            nota=5
        elif nota==5:
            nota=1
        cont=0
        if total==0:
            break
print('~'*40)
print('{:^40}'.format('Volte sempre ao Banco!'))