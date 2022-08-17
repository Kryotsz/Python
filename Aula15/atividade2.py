maior=-1
menor=999999999

for c in range(1,6):
    peso=float(input('Informe seu peso: '))
    if peso>maior:
        maior=peso
    if peso<menor:
        menor=peso
print('O maior peso lido foi {} e o menor foi {}'.format(maior,menor))
    
