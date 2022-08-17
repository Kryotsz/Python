# Programa para adivinhar o número que foi gerado "aleatoriamente"
from random import randint
num=int(input('O computador pensou em um número inteiro entre 0 e 5, tente adivinhar qual é: '))
resposta=randint(0,5)
if num==resposta:
    print('Acertou!')
else:
    print('Errou!')