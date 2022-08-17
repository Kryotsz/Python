vel=float(input('Qual a velocidade média do carro? '))
acima=vel-80
multa=7*acima
if vel>80:
    print('Você foi multado por excesso de velocidade, no valor de: {:.2f} reais.'.format(multa))
else:
    print('Você está dentro do limite de velocidade!')
