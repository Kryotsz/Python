reta1=float(input('Digite o comprimento da primeira reta: '))
reta2=float(input('Digite o comprimento da segunda reta: '))
reta3=float(input('Digite o comprimento da terceira reta: '))
if (reta1+reta2<reta3) or (reta1+reta3<reta2) or (reta2+reta3<reta1):
    print('As retas não podem formar um triângulo.')
else:
    print('As retas podem formar um triângulo.')

# --------------------------------------------------JEITO DA SORA---------------------------------------------------------------
if reta1<reta2+reta3 and reta2<reta1+reta3 and reta3<reta1+reta2:
    print('As retas podem formar um triângulo.')
else:
    print('As retas não podem formar um triângulo.')