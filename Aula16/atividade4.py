soma=0 #soma=menor=maior=cont=0
menor=0 #melhor=pior=''
maior=0
cont=0
melhor=''
pior=''

for c in range(1,8):
    nome=input('Digite o nome do atleta: ').strip().title()
    tempo=int(input('Digite o tempo em segundos: '))
    soma+=tempo
    media=soma/7
    if c==1:
        menor=tempo #menor=maior=tempo
        melhor=nome #melhor=pior=nome
        maior=tempo
        pior=nome
    elif tempo<menor:
        menor=tempo
        melhor=nome
    elif tempo>maior:
        maior=tempo
        pior=nome
    if tempo>=12 and tempo<=15:
        cont+=1

print('O nadador com o melhor tempo foi o {}!'.format(melhor))
print('O nadador com o pior desempenho foi o {}.'.format(pior))
print('O tempo médio dos nadadores foi: {:.2f} segundos'.format(media))
print('A quantidade de atletas com o tempo entre 12s e 15s é: {}'.format(cont))

#---------------------------------------------JEITO DA SORA-----------------------------------------------------------

nome=input('Nadador 1: ')
tempo=float(input('Tempo do nadador1: '))

melhornadador=nome
melhortempo=tempo
piornadador=nome
piortempo=tempo

somatempo=0
somatempo+=tempo
tempo12s15s=0

if 12<=tempo<=15:
    tempo12s15s+=1

for nadador in range(2,8):
    nome=input('Nadador {}'.format(nadador))
    tempo=float(input('Tempo do nadador {}'.format(nadador)))

    if tempo<melhortempo:
        melhornadador=nome
        melhortempo=tempo
    elif tempo>piortempo:
        piornadador=nome
        piortempo=tempo

    somatempo+=tempo

    if 12<=tempo<=15:
        tempo12s15s+=1

print(f'{melhornadador} é o melhor nadador com {melhortempo} seg. \n{piornadador} é o pior nadador com {piortempo}')

media=somatempo/7

print(f'Média dos tempos={media:.2f} seg. \n Atletas entre 12 seg e 15 seg: {tempo12s15s}')