'''
def maior(inteiros):
    maior=0
    for valor in inteiros:
        if valor>maior:
            maior=valor
    return maior

inteiros=[0,1,2,3,4,5,6,7,8,9,10]

print(maior(inteiros))
'''
#--------------------------------------OUTRO JEITO DE FAZER
'''
def maior(inteiros):
    maior=max(inteiros)
    return maior

inteiros=[1,2,3,4,5,6,7,8,9,10]

print(maior(inteiros))
'''
#---------------------------------------JEITO DA PROFE

def maior(*num): #Esse vezes antes do num, possibilita a entrada de dados de vários números = maior(1,2,3,4,5,6,7,8,9,10)
    cont=maior=0
    for valor in num:
        print(f'{valor}', end=' ')
        if cont==0:
            maior=valor
        elif valor>maior:
            maior=valor
        cont+=1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(1,2,3,4,5,6,7,8,9,10)