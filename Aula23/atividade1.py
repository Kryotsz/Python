from random import randint

linhas=[0,0]
colunas=[[],[]]
matriz=[[],[]]

linhas=int(input('Informe o número de linhas das matrizes: '))
colunas=int(input('Informe o número de colunas das matrizes: '))

for l in range(linhas):
    matriz[linhas]=randint(1,10)
    for c in range(colunas):
        matriz[colunas]=randint(1,10)


for l in range(linhas):
    for c in range(colunas):
        print(f'[{matriz[linhas][colunas]:^3}]', end='')
    print()
   
A=[randint(1,10)] #INCOMPLETO PQ DEU ROLLBACK

#------------------------------------------------JEITO DA PROFE
from random import randrange

linhas=int(input('Números de linhas: '))
colunas= int(input('Número de colunas: '))

a=[[randrange(1,11) for i in range(colunas)] for j in range(linhas)]
b=[[randrange(1,11) for i in range(colunas)] for j in range(linhas)]
#a = [[2, 1, -5], [3, 7, 0], [6, 1, 8]]
#b =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]

abaixodp=0
acimadp=0

for i in range(linhas):
    for j in range(colunas):
        if i>j:
            abaixodp+=a[i][j]
        if i<j:
            acimadp+=b[i][j]

print('Matriza A:')
for i in range(linhas):
    for j in range(colunas):
        print(a[i][j], end=' ')
    print()

print('Matriz B')
for i in range(linhas):
    for j in range(colunas):
        print(b[i][j], end=' ')
    print()

print(f'Soma= {abaixodp+acimadp}')
