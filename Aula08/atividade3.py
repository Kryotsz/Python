distancia=float(input(' Informe quantos Kms o carro alugado percorreu: '))
dias=float(input('Informe por quantos dias o carro foi alugado: '))
preço=distancia*0.15+dias*60
print('O valor a ser pago pelo aluguel do carro é: R${:2f}.'.format(preço))