print('-'*50)
sexo=input('Informe seu sexo: \nM. Masculino \nF. Feminino \nDigite M ou F: ').upper().strip()
if sexo!='M' and sexo!='F':
    print('Por favor, digite novamente utilizando "M" ou "F"')
else:
    if sexo=='M':
        print('Seu sexo é Masculino')
    elif sexo=='F':
        print('Seu sexo é Feminino')
print('-'*50)
#---------------------------------------------------JEITO DA PROFE-------------------------------------------------------
sexo=input('Informe seu sexo [M/F]: ').strip().upper()
while sexo not in 'MF':
    sexo=input('Dados inválidos. Por favor, digite "M" ou "F": ').strip().upper()
print('Sexo {} registrado com sucesso.'.format(sexo))