from random import randint

composta=[]

jogos=int(input('Informe quantos jogos serão gerados: '))

for l in range(jogos):
    lista=[]
    for c in range(0,6):
        lista.append(randint(1,60))
        lista.sort()

    composta.append(lista)

print(composta)