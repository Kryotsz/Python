# Exemplo de IF e ELSE
# if = se
# else = se não
nota1=int(input('Informe a nota 1: '))
nota2=int(input('Informe a nota 2: '))
media=(nota1+nota2)/2

'''>=6 maior que 6, incluindo o 6. (maior ou igual)
   >6 maior que 6, sem incluir o 6, sendo do 7 pra cima.'''

if media>=6:
    print('Aprovado')
else:
    print('Reprovado')

'''== igual
!=diferente
>maior que
<menor que
>=maior ou igual a
<=menor ou igual a
resulta em true ou false'''