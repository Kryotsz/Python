camisas=int(input('Informe a quantidade de camisas que irá levar: '))
preço=float(input('Informe o preço das camisas: '))
if camisas<=5:
    print('Um desconto de 3% será aplicado, o preço final será R${:.2f}'.format(preço-(preço*0.03)))
elif 5<camisas<=10:
    print('Um desconto de 5% será aplicado, o preço final será R${:.2f}'.format(preço-(preço*0.05)))
elif 10<camisas:
    print('Um desconto de 7% será aplicado, o preço final será R${:.2f}'.format(preço-(preço*0.07)))
else:
    print('OPÇÃO INVÁLIDA')