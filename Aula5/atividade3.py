from math import radians, sin, cos, tan
angulo=float(input('Digite um ângulo qualquer: '))
angulo1=radians(angulo)
seno=sin(angulo1)
cosseno=cos(angulo1)
tangente=tan(angulo1)
print('O ângulo {:.2f} tem como seno {:.2f}, cosseno {:.2f} e tangente {:.2f}.'.format(angulo, seno, cosseno, tangente))
