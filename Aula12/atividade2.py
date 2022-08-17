nome=input('Digite seu nome completo: ').upper().strip()

if nome.find('DIAS'):
    print('Seu nome possui "DIAS".')
else:
    print('Seu nome NÃO possui "DIAS".')

#--------------------------------------------JEITO DA PROFE---------------------------------------------------------------
nome=input('Qual seu nome completo: ').strip()
print('Seu nome tem {} '.format('DIAS' in nome.upper()))