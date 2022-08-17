
lista=[]
soma=0

termo=int(input('Informe o primeiro termo da PA: '))
quantidade=int(input('Informe a quantidade de termos da PA: '))
razao=int(input('Informe a razão da PA: '))

lista.append(termo)
soma+=termo

for c in range(quantidade-1):
    termo+=razao
    soma+=termo
    lista.append(termo)
print('-'*160)
print(f'Os {quantidade} termos da PA são:\n{lista}')
print(f'A soma dos elementos da PA é {soma}')

#-----------------------------------------------JEITO DA SORA------------------------------------------------------

termo=int(input('Informe o primeiro termo da P.A.: '))
num_termos=int(input('Informe o número de termos da P.A.: '))
razao=int(input('Informe a razão da P.A.: '))
pa = [termo]

termo_anterior=termo

for x in range(num_termos-1):
    termo_atual=termo_anterior+razao
    pa.append(termo_atual)
    termo_anterior=termo_atual
print(pa)

soma=sum(pa)

print(f'Soma dos elementos da PA = {soma}')
