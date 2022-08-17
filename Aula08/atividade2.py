largura=float(input('Qual a largura da parede em metros? '))
altura=float(input('Qual a altura da parede em metros? '))
area=largura*altura
tinta=area/2
print('A área da parede é {:.2f}m² e você terá que utilizar {:.2f} litros de tinta.'.format(area, tinta))