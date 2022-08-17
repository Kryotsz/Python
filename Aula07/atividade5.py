num=float(input('Digite um número positivo qualquer: '))
num2=float(input('Digite outro número positivo diferente: '))
menu=int(input('=-=-=-=-=-=-=-=-=-=-=-=Menu=-=-=-=-=-=-=-=-=-=-=-= \n1= Média ponderada, com pesos 2 e 3 respectivamente. \n2= Quadrado da soma de ambos os números. \n3= Cubo do menor número. \nEscolha uma opção dentre as anteriores: '))
def menor(num,num2):
    min=num
    if num2<min:
        min=num2
    return min
if menu==1:
    print('A média ponderada dos números {} e {} com pesos 2 e 3 respectivamente é: {:.2f}.'.format(num,num2,(num*2+num2*3)/5))
elif menu==2:
    print('O quadrado da soma dos números {} e {} é: {:.2f}.'.format(num,num2,(num+num2)**2))
elif menu==3:
    print('O menor número é {} e seu cubo é: {:.2f}.'.format(menor(num,num2),menor(num,num2)**3))
else:
    print('## Opção inválida ##')

# -----------------------------------------------Outro jeito de fazer:------------------------------------------------------------
if num<num2:
    menor=num
else:
    menor=num2
if menu==1:
    print('A média ponderada dos números {} e {} com pesos 2 e 3 respectivamente é: {:.2f}.'.format(num,num2,(num*2+num2*3)/5))
else:
    if menu==2:
        print('O quadrado da soma dos números {} e {} é: {:.2f}.'.format(num,num2,(num+num2)**2))
    else:
        if menu==3:
            print('O menor número é {} e seu cubo é: {:.2f}.'.format(menor,menor**3))
        else:
            print('## Opção inválida ##')