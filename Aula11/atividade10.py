nome=input('Digite seu nome completo: ').strip()
nome2=nome.split()
print('Seu nome completo é: {}. Seu primeiro nome é: {}. Seu último nome é: {}.'.format(nome, nome2[0], nome2[len(nome2)-1]))