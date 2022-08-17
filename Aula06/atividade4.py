distancia=float(input('Qual a distância da viagem em km? '))
preço1=0.50*distancia
preço2=0.45*distancia
if distancia<=200:
    print('Como sua viagem é abaixo de 200km, o preço da sua passagem vai ser {:.2f} reais.'.format(preço1))
else:
    print('Como sua viagem é mais longa, o preço da sua passagem vai ser {:.2f} reais.'.format(preço2))