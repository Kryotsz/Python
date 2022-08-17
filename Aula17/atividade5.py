parar=False
soma=0
cont1=0
cont2=0
barato=''

while not parar:
    nome=input('Digite o nome do produto: ')
    preço=float(input('Informe o preço do produto: '))
    continuar=input('Deseja continuar? [S/N]: ').strip().upper()
    soma+=preço
    cont2+=1
    if cont2==1:
        menor=preço
        barato=nome
    elif preço<menor:
        menor=preço
        barato=nome
    if preço>1000:
        cont1+=1
    if continuar=='S':
        parar=False
    else:
        parar=True
print('O total gasto na compra foi: R${:.2f}'.format(soma))
print('A quantidade de produtos que custa mais de R$1000,00 é: {}'.format(cont1))
print('O produto mais barato é: {}'.format(barato))

#--------------------------------------------JEITO DA SORA------------------------------------------------------------
total=totmil=menor=cont=0
barato=''
while True:
    produto=input('Nome do produto: ')
    preco=float(input('Preço R$: '))
    cont+=1
    total+=preco
    if preco>1000:
        totmil+=1
    if cont==1 or preco<menor:
        menor=preco
        barato=produto
    resp=' '
    while resp not in 'SN':
        resp=input('Quer continuar [S/N]? ').strip().upper()
    if resp=='N':
        break
print(f'O total das compras foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$1000,00.')
print(f'O produto mais barato foi {produto} que custa R${menor:.2f}')