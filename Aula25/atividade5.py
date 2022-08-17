from random import randint

matriz=[]
soma=0

linhas=int(input('Informe a quantidade de linhas da matriz: '))
colunas=int(input('Informe a quantidade de colunas da matriz: '))

for l in range(linhas):
    linha=[]
    for c in range(colunas):
        linha.append(randint(0,1))
        soma+=linha[-1]

    matriz.append(linha)

for l in range(linhas):
    for c in range(colunas):
        print(f'[{matriz[l][c]:^3}]', end='')
    print()

if soma==0:
    print('A matriz É nula!')
else:
    print('A matriz NÃO é nula.')

