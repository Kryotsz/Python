cont=soma=0

while True:
    num=int(input('Digite um número inteiro: '))
    if num==999:
        break
    cont+=1
    soma+=num
print('A quantidade de números digitados foram {} e a soma entre eles foi {}'.format(cont,soma))

#------------------------------------------------JEITO DA PROFE---------------------------------------------------------
num=cont=soma=0

num=int(input('Digite um número ou 999 para parar: '))

while num!=999:
    soma+=num
    cont+=1
    num=int(input('Digite um número ou 999 para parar: '))
print(f'Você digitou {cont} números e a soma entre eles é {soma}')

