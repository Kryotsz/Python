menu=int(input('********************************** \nCÁLCULO DE GRANDEZAS ELÉTRICAS \n********************************** \n1. Tensão (em Volt) \n2. Resistência (em Ohm) \n3. Corrente (em Ampére) \n********************************** \nQual grandeza deseja calcular? '))
if menu==1:
    resistencia=float(input('Informe o valor da Resistência: '))
    corrente=float(input('Informe o valor da Corrente: '))
    print('O valor da tensão é {} Volts'.format(resistencia*corrente))
elif menu==2:
    tensao=float(input('Informe o valor da Tensão: '))
    corrente=float(input('Informe o valor da Corrente: '))
    print('O valor da Resistência é {} Ohm.'.format(tensao/corrente))
elif menu==3:
    tensao=float(input('Informe o valor da Tensão: '))
    resistencia=float(input('Informe o valor da Resistência: '))
    print('O valor da Corrente é {} Ampére.'.format(tensao/resistencia))
else:
    print('##################### OPÇÃO INVÁLIDA #####################')