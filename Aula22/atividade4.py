from statistics import median

cont=0
lista=[]
centro=0

N=int(input('Quantos números serão informados? (Tem que ser ímpar): '))

while N%2==0:
    N=int(input('Informe um número ímpar: '))

while cont<N:
    num=int(input('Informe um número inteiro positivo: '))
    lista.append(num)
    cont+=1

centro=int(len(lista)/2)

c=centro
f=1
print('Calculando {}! = '.format(c), end='')

while c>0:
    print('{}'.format(c), end='')
    print(' x ' if c> 1 else ' = ', end='')
    f*=c
    c-=1
print('{}'.format(f))

#-----------------------------------------------JEITO DA SORA------------------------------------------------------
n=int(input('Digite um número ímpar, maior que 1: '))

if n<=1 or n%2==0:
    print('Número informado não atende os critérios definidos.')
    n=int(input('Digite um número ímpar, maior que 1: '))
else:
    l=[]
    for x in range(n):
        num=int(input('Digite um número maior ou igual a zero: '))
        l.append(num)

centro=int(len(l)/2) #arredonda pra baixo, por isso funciona
elementocentro=l[centro]
fatorial=1

for n in range(2, elementocentro+1):
    fatorial*=n
print(f'Lista: {l}')
print(f'O elemento central da lista é {elementocentro} e seu fatorial é igual a {fatorial}')

