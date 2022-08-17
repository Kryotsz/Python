unit=float(input('Informe o preço unitário da peça: '))
venda=int(input('Qual a quantidade de peças vendidas? '))
lucro=(venda*unit)
lucro2=(lucro*0.05)
print('O seu lucro pessoal foi de: {:.2f} reais'.format(lucro2))

# da pra fazer o cálculo do lucro apenas em uma linha, sendo dessa forma: comissão=(unit*venda)*0,05

