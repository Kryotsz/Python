num=int(input('Digite quantos números a serem mediados: '))
soma=0
for c in range(num):
    n=float(input('Digite um número qualquer: '))
    soma+=n
media=soma/num
print('A média dos {} números digitados é: {:.2f}'.format(num,media))