# Programa para resolver equações de segundo grau
a=float(input('Digite um valor para "a": '))
b=float(input('Digite um valor para "b": '))
c=float(input('Digite um valor para "c": '))
delta=(b**2)-(4*a*c)
x1=((-b+(delta**(1/2)))/2*a)
x2=((-b-(delta**(1/2)))/2*a)
print('O valor do delta é: {:.2f}'.format(delta))
print('O resultado da equação deu x1= {:.2f} e x2= {:.2f}'.format(x1, x2))
