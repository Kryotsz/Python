# Exemplo de IF e ELSE
print('## Programa de Empréstimos ## \n Responda: 0- Não e 1- Sim')
nomeNegativado=int(input('Possui nome negativado? '))

if nomeNegativado == 1:
    print('Não pode realizar o empréstimo.')
else:
    carteiraAssinada=int(input('Possui carteira assinada? '))
    if carteiraAssinada == 0:
        print('Não pode realizar o empréstimo.')
    else:
        possuiCasaPropria=int(input('Possui casa própria? '))
        if possuiCasaPropria == 0:
            print('Não pode realizar o empréstimo.')
        else:
            print('Concede o empréstimo.')