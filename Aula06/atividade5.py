num=int(input('Digite um número inteiro positivo: '))
resto=num%2
if resto==0:
    print('O número digitado foi {}, é par e seu quadrado é {}.'.format(num, num**2))
else:
    print('O número digitado foi {}, é ímpar e seu cubo é {}.'.format(num**3))