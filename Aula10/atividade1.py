from datetime import date
nascimento=int(input('Informe o ano de nascimento do atleta: '))
idade=(date.today().year)-nascimento
if idade<=9:
    print('MIRIM')
elif 9<idade<=14:
    print('INFANTIL')
elif 14<idade<=19:
    print('JÚNIOR')
elif 19<idade<=25:
    print('SÊNIOR')
elif 25<idade:
    print('MASTER')
else:
    print('OPÇÃO INVÁLIDA')