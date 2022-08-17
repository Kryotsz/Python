parar=False
cont1=0
cont2=0

while not parar:
    sexo=input('Informe seu sexo [M/F]: ').upper().strip()
    idade=int(input('Informe sua idade: '))
    if sexo=='M' and idade>=18:
        cont1+=1
    if sexo=='F':
        cont2+=1
    if idade<0:
        parar=True
        
print('Nessa turma há {} homens com idade acima de 18 anos.'.format(cont1))
print('Nessa turma há {} mulheres.'.format(cont2))

#--------------------------------------------------OUTRO JEITO------------------------------------------------------------
mulheres=0
homens_acima18=0

while True:
    idade=int(input('Idade: '))
    if idade<0:
        break
    sexo=input('Sexo: ').strip().upper()
    if sexo=='F':
        mulheres+=1
    elif sexo=='M' and idade>18:
        homens_acima18+=1
print(f'Total de mulheres: {mulheres} \nTotal de homens acima de 18 anos: {homens_acima18}')