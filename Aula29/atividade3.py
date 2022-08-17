def valorPagamento(prestacao, atraso):
    if atraso==0:
        pagamento=prestacao
    else:
        pagamento=prestacao+(prestacao*0.03)+(0.001*atraso)
    return pagamento

cont=0
soma=0

while True:
    valor=float(input('Informe o valor da prestação: '))
    if valor==0:
        print('~'*60)
        print('RELATÓRIO DO DIA:')
        print(f'Hoje foram pagas \033[32m{cont} prestações\033[m, totalizando um \033[32mvalor\033[m de \033[32mR${soma:.2f}\033[m')
        print('~'*60)
        break
    else:
        atraso=int(input('Informe o número de dias de atraso: '))
        pagamento=valorPagamento(valor, atraso)
        soma+=pagamento
        cont+=1
        print('~'*60)
        print(f'O \033[32mvalor\033[m a ser pago será \033[32mR${pagamento:.2f}\033[m')
        print('~'*60)

#--------------------------------------------------JEITO DA SORA-------------------------------------------------
