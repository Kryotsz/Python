valor=float(input('Informe o valor da casa: '))
salario=float(input('Informe o salário do comprador: '))
anos=float(input('Informe em até quantos anos ele irá pagar: '))
prestaçao=valor/(anos*12)
if prestaçao>salario*0.30:
    print('Empréstimo negado!')
else:
    print('Empréstimo concedido!')