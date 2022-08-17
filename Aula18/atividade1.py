num=int(input('Quantos números você quer mostrar: '))
elemento1=0
elemento2=1
cont=3

print('{}'.format(elemento1), end=' -> ')
print('{}'.format(elemento2), end=' -> ')

while cont<=num:
    elemento3=elemento1+elemento2
    print('{}'.format(elemento3), end=' -> ')
    elemento1=elemento2
    elemento2=elemento3
    cont+=1
print('FIM!')

#-----------------------------------------------JEITO DA PROFE---------------------------------------------------------
n=int(input('Quantos termos você quer mostrar: '))

t1=0
t2=1

print(f'{t1} -> {t2}', end=' ')

cont=3

while cont<=n:
    t3=t1+t2
    print(f'-> {t3}', end=' ')
    t1=t2
    t2=t3
    cont+=1
print('-> FIM!')