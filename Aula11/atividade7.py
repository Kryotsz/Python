cargo=int(input('------------------------------ \n            CARGOS \n------------------------------ \n1) Programador de Sistemas \n2) Analista de Sistemas \n3) Analista de Banco de Dados \n------------------------------ \nInforme seu cargo: '))
salario=float(input('Informe seu salário: '))
if cargo==1:
    print('Seu cargo é: Programador de Sistemas. Seu novo salário será: R${:.2f}'.format(salario+(salario*0.30)))
elif cargo==2:
    print('Seu cargo é: Analista de Sistemas. Seu novo salário será: R${:.2f}'.format(salario+(salario*0.20)))
elif cargo==3:
    print('Seu cargo é: Analista de Banco de Dados. Seu novo salário será: R${:.2f}'.format(salario+(salario*0.15)))
else:
    print('Cargo inválido')
    
# da pra usar print('-'*30) ao invés de ficar fazendo ----------------------------------