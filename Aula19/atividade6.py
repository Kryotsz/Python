primeiro=int(input('Primeiro termo: '))
razao=int(input('Razão da PA: '))
termo=primeiro
cont=1
mais=10
total=0

while mais!=0:
    total+=mais
    while cont<=total:
        print(f'{termo}', end=' -> ')
        termo+=razao
        cont+=1
    print('PAUSA')
    mais=int(input('Deseja mostrar mais alguns termos? Informe a quantidade: '))
print('FIM')
        