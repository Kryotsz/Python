L=[]
menor=maior=media=0

n=int(input('Digite um número para adicionar na lista: '))

maior=n
menor=n

while True:
    n=int(input('Digite um número para adicionar na lista: '))
    if n<=0:
        break
    if n>maior:
        maior=n
    if n<menor:
        menor=n

media=(menor*maior)**(1/4)

print(f'A média geométrica entre o menor valor: {menor}, e o maior valor: {maior}, é: {media:.2f}')