numeros=[]
listapares=[]

print('-'*60)

def sorteia():
    from random import randint
    for c in range(0,5):
        numeros.append(randint(0,10))
    print(f'Os números sorteados foram: {numeros}')
    print('-'*60)

def somapar():
    sorteia()
    soma=0
    for valor in numeros:
        if valor%2==0:
            listapares.append(valor)
            soma+=valor
    print(f'Os números pares presentes na lista são: {listapares}')
    print('-'*60)
    return soma

print(f'A soma dos pares é: {somapar()}')
print('-'*60)

#---------------------------------------------JEITO DA PROFE
from random import randint

def sorteia(lista):
    for cont in range(0,5):
        n=randint(1,10)
        lista.append(n)

def somaPar(lista):
    soma=0
    for valor in lista:
        if valor%2==0:
            soma+=valor
    print(f'Somando os valores pares de {lista}, temos {soma}')

numeros=list()
sorteia(numeros)
somaPar(numeros)