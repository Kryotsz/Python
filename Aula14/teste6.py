primeiro=int(input('Informe o primeiro termo da PA: '))
razão=int(input('Informe a razão da PA: '))
décimo=primeiro+(10-1)*razão

print('Os 10 primeiros valores da PA são: ')

for c in range(primeiro,décimo+1,razão):
    print(c)
