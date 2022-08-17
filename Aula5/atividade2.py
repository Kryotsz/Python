oposto=float(input('Digite o comprimento do cateto oposto: '))
adjacente=float(input(' Digite o comprimento do cateto adjacente: '))
hipotenusa=(oposto**2+adjacente**2)**(1/2)
print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa))

# Outra maneira de fazer usando a biblioteca math:
from math import hypot
hipotenusa1=hypot(oposto, adjacente)
print('O comprimento da hipotenusa é: {:.2f}'.format(hipotenusa1))