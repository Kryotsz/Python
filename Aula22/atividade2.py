tupla=('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino', 'Fluminense', 'América-MG',
 'Atlético-GO', 'Santos', 'Ceará SC', 'Internacional', 'São Paulo', 'Athletico-PR', 'Cuiabá', 'Juventude', 'Grêmio', 
 'Bahia', 'Sport Recife', 'Chapecoense')

print('-'*160)
print(f'Os 5 primeiros colocados são: {tupla[:5]}')
print('-'*160)
print(f'Os últimos 4 colocados são: {tupla[-4:]}')
print('-'*160)
print(f'{sorted(tupla)}')
print('-'*160)
Chapecoense=tupla.index('Chapecoense')+1
print(f'O time Chapecoense se encontra na posição {Chapecoense}')
print('-'*160)


