soma=0
barato=0
medicamento=''

for c in range(1,6):
    nome=input('Informe o nome do medicamento: ').strip().capitalize()
    preço=float(input('Informe o preço do medicamento: '))
    soma+=preço
    media=soma/5
    if c==1:
        barato=preço
        medicamento=nome
    elif preço<barato:
        barato=preço
        medicamento=nome
print('O medicamento mais barato é o {}, que custa: {}'.format(medicamento,barato))
print('A média aritmética dos medicamentos informados é {}'.format(media))