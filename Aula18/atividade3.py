soma=maior=menor=cont=0

while True:
    num=int(input('Digite um número inteiro: '))
    continuar=input('Deseja continuar? [S/N]: ').strip().upper()
    cont+=1
    soma+=num
    if cont==1:
        maior=menor=num
    elif num>maior:
        maior=num
    elif num<menor:
        menor=num
    if continuar=='N':
        break

media=soma/cont

print('A média dos {} números digitados foi {}. \nO maior valor lido foi {} e o menor foi {}'.format(cont,media,maior,menor))

#-----------------------------------------------JEITO DA PROFE---------------------------------------------------------
resp='S'
soma=quant=media=maior=menor=0

while resp in 'S':
    num=int(input('Digite um número: '))
    soma+=num
    quant+=1
    if quant==1:
        maior=menor=num
    else:
        if num>maior:
            maior=num
        if num<menor:
            menor=num
    resp=input('Quer continuar [S/N]? ').upper().strip()
media=soma/quant

print(f'Você digitou {quant} números e a média foi {media}')
print(f'O maior valor foi {maior} e o menor foi {menor}')