n=int(input('Quantos valores serão mediados: '))
soma=0

for c in range(n):
    num=float(input('Informe um número para fazer a média: '))
    soma+=num
    media=soma/n
print('A média dos {} números é: {:.2f}'.format(n,media))