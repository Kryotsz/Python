sexo=''
while sexo!='M' and sexo!='F':
    sexo=input('Informe seu sexo [M/F]: ').upper().strip()
    if sexo!='M' and sexo!='F':
        print('Digite um valor correto')
    if sexo=='M':
        print('Seu sexo é Masculino')
    if sexo=='F':
        print('Seu sexo é feminino')
    
    
