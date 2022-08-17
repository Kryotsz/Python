termo=int(input('Informe o primeiro termo da PA: '))
razao=int(input('Informe a razão da PA: '))

print('Os 10 primeiros termos da PA são:')
for c in range(0,10):
    termo+=razao
    print(termo)

#-----------------------------------------------------JEITO CERTO-------------------------------------------------------------------------------------------------------
primeiro=int(input('Informe o primeiro termo da PA: '))
razão=int(input('Informe a razão da PA: '))
décimo=primeiro+(10-1)*razão
print('Os 10 primeiros termos da PA são:')
for c in range(primeiro,décimo+razão,razão):
    print('{}'.format(c), end='-> ')
print('FIM')