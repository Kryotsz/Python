copo1= 'laranja'
copo2= 'acerola'

copo3=copo1
copo1=copo2
copo2=copo3

print('O primeiro copo possui: {}.'.format(copo1))
print('O segundo copo possui: {}.'.format(copo2))

#---------------------------------------------JEITO DA PROFE--------------------------------------------------------------
cop1='laranja'
cop2='acerola'

print('Antes da troca: \nCopo 1 tem {} \n Copo 2 tem {}'.format(cop1,cop2))

cop1,cop2=cop2,cop1

print('Depois da troca: \nCopo 1 tem {} \n Copo 2 tem {}'.format(cop1,cop2))