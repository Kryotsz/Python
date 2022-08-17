from random import randint, choice
nome=input('Informe o nome do aluno: ')
nome2=input('Informe o nome do segundo aluno: ')
nome3=input('Informe o nome do terceiro aluno: ')
nome4=input('Informe o nome do quarto aluno: ')
escolhido=randint(1,4)
if escolhido==1:
    print('{} foi escolhido(a) pra apagar o quadro!'.format(nome))
elif escolhido==2:
    print('{} foi escolhido(a) pra apagar o quadro!'.format(nome2))
elif escolhido==3:
    print('{} foi escolhido(a) pra apagar o quadro!'.format(nome3))
else:
    print('{} foi escolhido(a) pra apagar o quadro!'.format(nome4))

    #-------------------------------------------------OUTRO JEITO-------------------------------------------------------------------
lista=(nome,nome2,nome3,nome4)
escolhido1=choice(lista)
print('{} foi escolhido(a) para apagar o quadro!'.format(escolhido1))