cont=0

for c in range(1,6): #range(5)
    num=int(input('Digite um número: '))
    if num%2==0:
        cont+=1
print('Dos {} números digitados, {} são pares'.format(c,cont))