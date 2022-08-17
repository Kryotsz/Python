n=int(input('Digite um número qualquer para ver seu fatorial: '))

resultado=1

for c in range(1, n+1):
    resultado*=c
print('Você digitou {} e seu fatorial é {}'.format(n,resultado))

#---------------------------------------------OUTRO JEITO-----------------------------------------------------------------
count=1
resultado=1

while count<=n:
    resultado*=count
    count+=1

print('Você digitou {} e seu fatorial é {}'.format(n,resultado))

#-----------------------------------------------JEITO DA SORA--------------------------------------------------------------
c=n
f=1
print('Calculando {}! = '.format(n), end='')

while c>0:
    print('{}'.format(c), end='')
    print(' x ' if c> 1 else ' = ', end='')
    f*=c
    c-=1
print('{}'.format(f))