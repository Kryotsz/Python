from datetime import date
ano=int(input('Informe o ano de seu nascimento: '))
idade=(date.today().year)-ano
if idade==18:
    print('Você terá que se alistar esse ano!')
elif idade<18:
    print('Você terá que se alistar daqui a {} ano(s).'.format(18-idade))
else:
    print('Você já deveria ter se alistado! Você passou {} anos do prazo.'.format(idade-18))
