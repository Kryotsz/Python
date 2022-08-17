salario=float(input('Informe seu salário: R$'))
if salario>1250:
    print('Seu salário é superior a R$1250.00, portanto receberá um aumento de 10%, seu novo salário é: R${:.2f}.'.format(salario+salario*0.10))
else:
    print('Seu salário é inferior ou igual a R$1250.00, portanto receberá um aumento de 15%, seu novo salário é: R${:.2f}.'.format(salario+salario*0.15))