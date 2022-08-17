from calendar import isleap
ano=int(input('Digite um ano qualquer: '))
if isleap(ano):
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} não é BISSEXTO.'.format(ano))

# ------------------------------------------------Outro jeito de fazer:----------------------------------------------------------
if ano%4 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} não é BISSEXTO.'.format(ano))