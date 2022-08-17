
listanomes=[]
listatempos=[]
melhor=pior=''
maior=menor=soma=media=0

for c in range(0,7):
    nome=input('Digite o nome do atleta: ').strip().title()
    tempo=int(input('Informe o tempo do atleta (em segundos): '))
    listanomes.append(nome)
    listatempos.append(tempo)
    soma+=tempo
    if c==0:
        maior=tempo
        menor=tempo
        melhor=nome
        pior=nome
    elif tempo>maior:
        maior=tempo
        pior=nome
    elif tempo<menor:
        menor=tempo
        melhor=nome
media=soma/7
print('-'*160)
print('RELATÓRIO')
print('-'*160)
print(f'O nadador com o melhor desempenho foi o {melhor} com o tempo de {menor} segundos')
print(f'O nadador com o pior desempenho foi o {pior} com o tempo de {maior} segundos')
print(f'O tempo médio dos nadadores é {media:.2f}')
print('-'*160)

#---------------------------------------------------JEITO DA SORA---------------------------------------------------

atletas=[]
tempo=[]

for x in range(7):
    nome=input('Informe o nome do nadador: ')
    tempos=float(input('Informe o tempo do nadador: '))
    atletas.append(nome)
    tempo.append(tempos)

indice_melhor=tempo.index(min(tempo)) # Imprime o índice(posição) do melhor tempo(menor)

indice_pior=tempo.index(max(tempo)) # Imprime o índice(posição) do pior tempo(maior)

media_tempos=sum(tempo)/len(tempo)

print(f'{atletas[indice_melhor]} tem o melhor tempo.')
print(f'{atletas[indice_pior]} tem o pior tempo.')
print(f'Média dos tempos: {media_tempos:.2f}.')