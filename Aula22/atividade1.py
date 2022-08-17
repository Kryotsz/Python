listapares=[]

valor1=int(input('Informe o primeiro valor: '))
valor2=int(input('Informe o segundo valor: '))
valor3=int(input('Informe o terceiro valor: '))
valor4=int(input('Informe o quarto valor: '))

tupla=(valor1, valor2, valor3, valor4)

print(f'O valor 9 apareceu {tupla.count(9)} vez(es)')
print(f'O valor 3 apareceu primeiramente na posição {tupla.index(3)+1}')

for c in range(0,4):
    if tupla[c]%2==0:
        listapares.append(tupla[c])

print(f'Os números pares digitados foram: {listapares}')

#-----------------------------------------JEITO DA SORA COM TUPLA---------------------------------------------------
num=(int(input('Digite um número: ')), int(input('Digite um outro número: ')), 
int(input('Digite mais um número: ')), int(input('Digite o último número: ')))

if 9 in num:
    print(f'O valor apareceu {num.count(9)}')
else:
    print('O número 9 não está presente')

if 3 in num:
    print(f'O número 3 foi digitado na posição {num.index(3)+1}')
else:
    print('O número 3 não foi informado')

for n in num:
    if n%2==0:
        print(n, end=' ')

#---------------------------------------OUTRO JEITO COM LISTA--------------------------------------------
num=[]

for n in range(0,4):
    num.append(int(input('Digite um número: ')))

if 9 in num:
    print(f'O valor apareceu {num.count(9)}')
else:
    print('O número 9 não está presente')

if 3 in num:
    print(f'O número 3 foi digitado na posição {num.index(3)+1}')
else:
    print('O número 3 não foi informado')

for n in num:
    if n%2==0:
        print(n, end=' ')

