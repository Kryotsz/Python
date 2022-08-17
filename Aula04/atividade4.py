# Programa que calcula o salário somado à comissão de um corretor
nome=input('Qual o nome do corretor? ')
quantidade=int(input('Qual a quantidade de imóveis vendidos? '))
valor=float(input('Qual o valor total das vendas? '))
comissao=(200*quantidade)+(valor*0.05)
salario=1500+comissao
print('O salário final do corretor {} é: R${:.2f}'.format(nome, salario))