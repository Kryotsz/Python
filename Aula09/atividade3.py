from re import A


num=int(input('Digite um número inteiro: '))
num2=int(input('Digite outro número inteiro para comparar: '))
if num>num2:
    print('O primeiro valor é maior')
elif num2>num:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior')