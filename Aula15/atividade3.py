soma=0
cont=0
maior=-1
velho=''

for c in range(1,5):
    nome=input('Informe seu nome: ').strip().title()
    idade=int(input('Informe sua idade: '))
    sexo=input('Informe seu sexo [M/F]: ').upper().strip()
    if sexo=='F' and idade<20:
        cont+=1
    if sexo=='M'and idade>maior:
        maior=idade
        velho=nome
    soma+=idade
    media=soma/4

print('A média de idade do grupo é {}'.format(media))
print('O nome do homem mais velho é: {} e possui {} anos'.format(velho,maior))
print('{} mulher(es) têm menos de 20 anos'.format(cont))