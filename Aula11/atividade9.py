usuario=input('Digite seu usuário: ')
senha=input('Digite sua senha: ')
login='Fábio123'
login2='Fabinho987'
if login==usuario+senha:
    print('Seja bem vindo {}!'.format(usuario))
elif login2==usuario+senha:
    print('Seja bem vindo {}!'.format(usuario))
else:
    print('Usuário e senha não conferem.')