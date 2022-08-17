from random import randint
from math import prod

lista=[]
mult=1

n=int(input('Digite quantos números você quer na lista: '))

if n<=1:
    n=int(input('Digite um valor maior que 1: '))
else:
    for c in range(n):
        lista.append(randint(1,10))

print(lista)
mediageo=(prod(lista))**(1/n)
print(f'A média geométrica dos {n} elementos é: {mediageo:.2f}')

