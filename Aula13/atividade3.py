cont=0
soma=0

for c in range(1,501):
    if c%3==0:
        if c%2!=0:
            cont+=1
            soma+=c
print('A soma de {} valores ímpares é: {}'.format(cont,soma))
