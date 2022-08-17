dias=('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado') #lista do tipo tupla
                                                                            #tupla() não pode mexer nos valores de dentro
print(dias[3])                                                              #lista[] pode mexer nos valores de dentro'''

texto='python'
print(tuple(texto))

lista=[1,2,3,4]
lista[2]=8
print(tuple(lista))

lista=[3,4]
tupla=(1,2,lista)
tupla=(1,2,lista[0],lista[1])

print(tupla)

print(tupla.count(2))

lista=['python', 1, 2, 'java']
print(lista)

meses=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
n=1
while n<4:
    mes=int(input('Escolha o mês [1-12]: '))
    if 1<=mes<13:
        print(f'O mês é {meses[mes-1]}')
    n+=1

meses=['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

meses.append('igor')

meses+=['igor', 'zé']

print(meses)

for mes in meses:
    print(mes, end=' ')