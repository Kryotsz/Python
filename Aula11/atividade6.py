from random import randint
computador=randint(0,2)
lista=['Pedra','Papel','Tesoura']
escolha=int(input('0)Pedra \n1)Papel \n2)Tesoura \nSua escolha: '))
if escolha==computador:
    print('EMPATE! Ambos escolheram {}!'.format(lista[escolha]))
elif (escolha==0 and computador==2) or (escolha==1 and computador==0) or (escolha==2 and computador==1):
    print('Você venceu! Você escolheu {} e o computador escolheu {}!'.format(lista[escolha],lista[computador]))
elif (escolha==0 and computador==1) or (escolha==1 and computador==2) or (escolha==2 and computador==0):
    print('Você perdeu! Você escolheu {} e o computador escolheu {}!'.format(lista[escolha],lista[computador]))
else:
    print('------------------ \nOPÇÃO INVÁLIDA \n------------------')
