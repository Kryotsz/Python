from datetime import date

cont1=0
cont2=0

for c in range(1,8):
    ano=int(input('Digite o ano de seu nascimento: '))
    idade=(date.today().year)-ano
    if idade<18:
        cont1+=1
    elif idade>=18:
        cont2+=1
print('Das 7 pessoas {} NÃO atingiram a maioridade e {} JÁ atingiram.'.format(cont1,cont2))