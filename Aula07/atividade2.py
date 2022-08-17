from re import A


num=float(input('Digite um número qualquer: '))
num2=float(input('Digite um número qualquer diferente do primeiro: '))
num3=float(input('Digite um número qualquer diferente dos anteriores: '))
def maior(num,num2,num3):
    max=num
    if num2>max:
        max=num2
    if num3>max:
        max=num3   
    return max
def menor(num,num2,num3):
    min=num
    if num2<min:
        min=num2
    if num3<min:
        min=num3
    return min
print('O maior número entre {}, {} e {}, é: {}.'.format(num,num2,num3,maior(num,num2,num3)))
print('O menor número entre {}, {} e {}, é: {}.'.format(num,num2,num3,menor(num,num2,num3)))

# ------------------------------------------------Outro jeito de fazer:--------------------------------------------------------
if num2<num>num3:
    maior=num
else:
    if num<num2>num3:
        maior=num2
    else:
        maior=num3  
if num2>num<num3:
    menor=num
else:
    if num>num2<num3:
        menor=num2
    else:
        menor=num3
print('O maior número entre {}, {} e {} é: {}.'.format(num,num2,num3,maior))
print('O menor número entre {}, {} e {} é: {}.'.format(num,num2,num3,menor))

# -----------------------------------------------Jeito que a profe fez ---------------------------------------------------------
menor=num
if num2<num and num2<num3:
    menor=num2
if num3<num and num3<num2:
    menor=num3

maior=num
if num2>num and num2>num3:
    maior=num2
if num3>num and num3>num2:
    maior=num3
