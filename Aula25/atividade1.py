tupla=('Arroz', 1.00,
       'Feijão', 2.00, 
       'Tomate', 3.00, 
       'Morango', 4.00,
       'Carne', 5.00,
       'Pão', 6.00,
       'Queijo', 7.00,
       'Bolacha', 8.00,
       'Salgadinho', 9.00,
       'Brigadeiro', 10.00)

print('-'*40)
print('TABELA DE PREÇOS')
print('-'*40)
for c in range(0, len(tupla)):
    if c%2==0:
        print(f'{tupla[c]:.<30}', end=' ')
    else:
        print(f'R${tupla[c]:>5.2f}')
print('-'*40)
