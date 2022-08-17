def somaImposto(taxaImposto, custo):
    imposto=taxaImposto/100
    custo=custo+custo*imposto
    return custo

taxaImposto=int(input('Informe quantos por cento é a quantia de imposto sobre vendas: '))
custo=float(input('Informe o custo do produto antes do imposto:'))

print(f'O preço final do produto com imposto será: {somaImposto(taxaImposto, custo)}')

#------------------------------------------------JEITO DA SORA-----------------------------------------------------------
def somaImposto(taxaImposto,custo):
    return (0.01*taxaImposto)*custo+custo

taxa=int(input('Informe a taxa de imposto do produto: '))
valor=int(input('Informe o custo do produto: '))

print(f'Qual o valor do produto com o imposto: {somaImposto(taxa,valor)}')