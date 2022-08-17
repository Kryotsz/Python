soma=0

a=int(input('Digite um número inteiro: '))
b=int(input('Digite outro número inteiro: '))

if a<b:
    for c in range(a+1,b):
        soma+=c

    print(f'A soma dos números no intervalo entre {a} e {b} é {soma}')
    
else:
    print('ERRO')

