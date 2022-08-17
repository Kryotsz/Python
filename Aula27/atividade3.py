'''def leiaInt(valor):
    if type(valor)!=int:
        print('Erro, a função aceita só números inteiros: ')
    else:
        print(f'Você digitou o número inteiro {valor}')

valor=input('Digite um número inteiro: ')
print(type(valor))
leiaInt(valor)'''
#INCOMPLETO
#--------------------------------------JEITO DA SORA
def leiaInt(msg):
    ok=False
    valor=0
    while True:
        n=input(msg)
        if(n.isnumeric()):
            valor=int(n)
            ok=True
        else:
            print('Digite um número válido.')
        if ok:
            break
    return valor

n=leiaInt('Digite um número: ')
print(f'Você digitou o número {n}')





