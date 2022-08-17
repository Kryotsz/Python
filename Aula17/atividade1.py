cont=0

n=int(input('Digite um número qualquer: '))

for c in range(2,n):
    if n%c==0:
        cont+=1

if cont==0 and n>=2:
    print('O número {} é primo!'.format(n))
else:
    print('O número {} NÃO é primo'.format(n))

#------------------------------------------------------OUTRO JEITO---------------------------------------------------------

num=int(input('Digite um número: '))
tot=0

for c in range(1,num+1):
    if num%c==0:
        print('\033[33m', end=' ')
        tot+=1
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')

print(f'\n\033[mO número {num} foi divisível {tot} vezes.')

if tot==2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')