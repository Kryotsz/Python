def ficha(jogador='Nenhum', gols=0):
    tamanho=len(jogador)+25
    print('~'*tamanho)
    print(f'O jogador {jogador} marcou {gols} gol(s)')
    print('~'*tamanho)

j=input('Informe o nome do jogador: ').strip().title()
g=input('Informe a quantidade de gols marcados pelo jogador: ')

if g.isnumeric():
    g=int(g)
else:
    g=0

if j.strip()=='':
    ficha(gols=g)
else:
    ficha(j,g)
#-------------------------------------------------------JEITO DA SORA
def ficha(jogador='Igor', gol=0): #Se não for informado nenhum parâmetro, Igor e 0 serão o padrão
    print(f'O jogador {jogador} fez {gol} gol(s) no campeonato')

n=input('Nome do jogador: ')
g=input('Número de gols: ')

if g.isnumeric():
    g=int(g)
else:
    g=0

if n.strip()=='':
    ficha(gol=g)
else:
    ficha(n,g)