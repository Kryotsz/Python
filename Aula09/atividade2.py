num=int(input('Digite um número inteiro qualquer: '))
escolha=int(input('Escolha a base de conversão: \n 1)binário \n 2)octal \n 3)hexadecimal \n Digite 1, 2 ou 3: '))
if escolha==1:
    binario=bin(num)
    print('O número {} convertido em binário é {}.'.format(num,binario))
elif escolha==2:
    octal=oct(num)
    print('O número {} convertido em octal é {}.'.format(num,octal))
elif escolha==3:
    hexadecimal=hex(num)
    print('O número {} convertido em hexadecimal é {}.'.format(num,hexadecimal))
else:
    print('Opção inválida! Você deve digitar "1", "2" ou "3".')