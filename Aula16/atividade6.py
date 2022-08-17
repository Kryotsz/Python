parar=False
soma=0
cont=0

print('Código de cargo: \n1 - Enfermeiro \n2 - Nuricionista \n3 - Médico(a)')

while not parar:
    codigo=int(input('Informe o código do cargo: '))
    salario=float(input('Informe o salário desse cargo: '))
    if codigo==2:
        cont+=1
        soma+=salario
    if codigo==0:
        parar=True
    elif codigo>3:
        print('Código inválido!')
        break
media=soma/cont
print('A média salarial dos nutricionistas é: {:.2f}'.format(media))

#-------------------------------------------------JEITO DA SORA---------------------------------------------------------

print('Código de cargo: \n1 - Enfermeiro \n2 - Nuricionista \n3 - Médico(a)')

qtdenutri=0
total_sal_nutri=0

while True:
    cargo=int(input('Informe um código de cargo: '))
    if cargo>=1 and cargo<=3:
        salario=float(input('Salário R$: '))
        if cargo==2:
            qtdenutri+=1
            total_sal_nutri+=salario
        resp=input('Deseja continuar [S/N]: ')
        if resp.upper()=='N':
            break
    else:
        print('Código inválido!')

if qtdenutri>0:
    media=total_sal_nutri/qtdenutri
    print(f'Média salarial das nutricionistas R$: {media:.2f}')
else:
    print('Não foram inseridos dados sobre as nutricionistas.')
