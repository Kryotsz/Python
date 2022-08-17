from random import randint

lista=[]
tamanho=0

while True:
    nomes=str(input('Digite o nome do comprador: ')).strip().capitalize()
    if (nomes.lower())=='parar':
        break
    else:
        lista.append(nomes)

tamanho=len(lista)
sorteado=randint(0,tamanho)
print(f'O ganhador do prêmio é {lista[sorteado]}')
