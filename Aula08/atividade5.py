from random import shuffle
nome=str(input('Informe o nome do aluno: '))
nome2=str(input('Informe o nome do segundo aluno: '))
nome3=str(input('Informe o nome do terceiro aluno: '))
nome4=str(input('Informe o nome do quarto aluno: '))
lista=[nome,nome2,nome3,nome4]
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))

#-------------------------------------------OUTRO JEITO DE MOSTRAR O RESULTADO-------------------------------------------------------

print('A ordem de apresentação será: {}, {}, {} e {}.'.format(lista[0],lista[1],lista[2],lista[3]))