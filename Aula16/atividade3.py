tentativas=2
parar=False
nome=input('Digite seu nome: ').strip().title()

while not parar:
    senha=int(input('Digite sua senha: '))
    if senha==123456:
        print('Olá, {}. Seja bem-vindo ao nosso banco!'.format(nome))
        parar=True
    elif senha!=123456 and tentativas==2:
        print('Senha incorreta! Você ainda tem 2 tentativas.')
        tentativas-=1
    elif senha!=123456 and tentativas==1:
        print('Senha incorreta! Você ainda tem 1 tentativa.')
        tentativas-=1
    elif senha!=123456 and tentativas==0:
        print('Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.')
        parar=True
    
#--------------------------------------------------OUTRO JEITO-------------------------------------------------------------

nome=input('Digite seu nome: ').strip().title()

for c in range(1,4):
    senha=int(input('Digite sua senha: '))
    if senha==123456:
        print('Olá, {}. Seja bem-vindo ao nosso banco!'.format(nome))
        break
    elif senha!=123456 and c==1:
        print('Senha incorreta! Você ainda tem 2 tentativas.')
    elif senha!=123456 and c==2:
        print('Senha incorreta! Você ainda tem 1 tentativa.')
    elif senha!=123456 and c==3:
        print('Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.')
        break

#------------------------------------------------------JEITO DA PROFE----------------------------------------------------

nome=input('Informe seu nome: ')

for c in range(3,0,-1):
    senha=int(input('Senha: '))
    if senha==123456:
        print('Olá, {}. Seja bem vindo ao nosso banco!'.format(nome))
        break
    elif senha!=123456:
        print('Senha incorreta! Você ainda tem {} tentativa(s).'.format(c-1))
        if c==1:
            print('Sua senha foi bloqueada! Por favor, dirija-se a um de nossos caixas.')
            break