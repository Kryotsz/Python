def voto(nascimento):
    from datetime import date
    ano_atual=date.today().year
    idade=ano_atual-nascimento
    if idade<16:
        print('VOTO NEGADO')
    elif idade>=16 and idade<18:
        print('VOTO OPCIONAL')
    elif idade>=18 and idade<65:
        print('VOTO OBRIGATÓRIO')
    elif idade>=65:
        print('VOTO OPCIONAL')

nascimento=int(input('Digite o ano do seu nascimento: '))
voto(nascimento)

#-----------------------------------------------------JEITO DA SORA
def voto(ano):
    from datetime import date
    atual=date.today().year
    idade=atual-ano

    if idade<16:
        return f'Com {idade} anos: VOTO NEGADO'
    elif 16<=idade<18 or idade>65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

nasc=int(input('Digite o ano em que você nasceu: '))
print(voto(nasc))