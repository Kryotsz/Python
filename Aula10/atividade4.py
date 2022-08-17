preço=float(input('Informe o preço normal do produto: '))
menu=int(input('***************************************************** \nOPÇÕES \n***************************************************** \n1) À vista com dinheiro/cheque: 10% de desconto \n2) À vista no cartão: 5% de desconto \n3) Em até 2x no cartão: preço normal \n***************************************************** \nInforme a condição de pagamento: '))
if menu==1:
    print('Você escolheu pagar à vista com dinheiro/cheque, portanto um desconto de 10% será aplicado. O valor a ser pago pelo produto será R${:.2f}.'.format(preço-(preço*0.10)))
elif menu==2:
    print('Você escolheu pagar à vista no cartão, portanto um desconto de 5% será aplicado. O valor a ser pago será R${:.2f}.'.format(preço-(preço*0.05)))
elif menu==3:
    print('Você escolheu pagar em até 2x no cartão. O valor a ser pago será R${:.2f}.'.format(preço))
else:
    print('OPÇÃO INVÁLIDA, DIGITE "1", "2" OU "3".')