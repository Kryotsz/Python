a=float(input('Digite o comprimento da primeira reta: '))
b=float(input('Digite o comprimento da segunda reta: '))
c=float(input('Digite o comprimento da terceira reta: '))

if (a + b < c) or (a + c < b) or (b + c < a):
    print('Não é possível formar um triângulo')
elif a==b and b==c:
    print('Triângulo equilátero')
elif a==b or b==c or c==a:
    print('Triângulo isósceles')
else:
    print('Triângulo escaleno')
