p1x=float(input('Qual o x do ponto 1? '))
p1y=float(input('Qual o y do ponto 1? '))
p2x=float(input('Qual o x do ponto 2? '))
p2y=float(input('Qual o y do ponto 2? '))
distancia=((p2x-p1x)**2+(p2y-p1y)**2)**(1/2)
print('A distância entre os pontos P1 e P2 é {:.2f}'.format(distancia))

'''Para fazer raiz quadrada da pra importar uma função de uma biblioteca, nesse caso foi importado a raiz quadrada: from math import sqrt. 
Essa função é utilizada da seguinte forma: distancia=sqrt((p2x-p1x)**2+(p2y-p1y)**2)'''
