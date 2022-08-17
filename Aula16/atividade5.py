parar=False
maior=0
menor=0
soma=0
cont=0

while not parar:
    idade=int(input('Digite sua idade: '))
    cont+=1
    if cont==1:
        maior=idade
        menor=idade
    elif idade<0:
        parar=True
    elif idade>maior:
        maior=idade
    elif idade<menor:
        menor=idade
soma+=(menor+maior)
media=soma/2
print('A média aritmética entre a maior e a menor idade é: {}'.format(media))

#----------------------------------------------JEITO DA SORA---------------------------------------------------------

idade=int(input('Idade: '))

maisnovo=idade
maisvelho=idade

while True:
    idade=int(input('Idade: '))
    if idade<0:
        break

    if idade<maisnovo:
        maisnovo=idade
    elif idade>maisvelho:
        maisvelho=idade

media=(maisnovo+maisvelho)/2

print(f'Menor idade: {maisnovo} \nMaior idade: {maisvelho} \nMédia das duas idades={media}')