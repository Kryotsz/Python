from random import randint

l1=[]
l2=[]
l3=[]
soma1=soma2=0

N=int(input('Quantos valores: '))

if N<=0:
    N=int(input('Quantos valores: '))

for c in range(N):
    valores1=randint(1,10)
    l1.append(valores1)
    soma1+=valores1

for c in range(N):
    valores2=randint(1,10)
    l2.append(valores2)
    soma2+=valores2

l3.append(soma1)
l3.append(soma2)

print(l1)
print(l2)
print(l3) #ESTÁ ERRADO, A SOMA DAS LISTAS DEVE SER DE OUTRO JEITO

#------------------------------------------JEITO DA PROFE
from random import randrange

n=int(input('Informe o valor para N: '))

if n>0:
    l1=[randrange(1,11) for i in range(n)]
    l2=[randrange(1,11) for i in range(n)]

    l3=[]

    for i in range(n):
        l3.append(l1[i]+l2[i])

    print(f'L1 = {l1}')
    print(f'L2 =  {l2}') 
    print(f'L3 = {l3}')
else:
    print('Erro: N deve ser maior que 0')
