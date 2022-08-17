cont=0

primeiro=int(input('Informe o primeiro termo da PA: '))
razão=int(input('Informe a razão da PA: '))
termos=primeiro

print('Os 10 primeiros termos da PA são: ')
print(primeiro)

while True:
    cont+=1
    termos+=razão
    print(termos)
    if cont==9:
        break

#------------------------------------------------JEITO DA PROFE----------------------------------------------------------

primeiro=int(input('Primeiro termo: '))
razao=int(input('Razão da PA: '))
termo=primeiro
cont=1
while cont<=10:
    print(f'{termo}', end=' ')
    termo+=razao
    cont+=1
print('Fim')