soma=0
cont=0
for c in range(1,7):
    num=int(input('Informe um número inteiro: '))
    if num%2==0:
        soma+=num
        cont+=1
print('A soma dos {} valores pares informados é: {}'.format(cont,soma))