lista=[12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52]
maiorvalor=lista[0]
menorvalor=lista[0]
listapares=[]
ocorrencia=0
media=0
soma=0

for index in range(0,len(lista)):
    #Maior valor
    if maiorvalor<lista[index]:
        maiorvalor=lista[index]
    #Menor valor
    if menorvalor>lista[index]:
        menorvalor=lista[index]
    #Lista de números pares
    if lista[index]%2==0:
        listapares.append(lista[index])
    #Número de ocorrências do primeiro elemento
    if lista[index]==lista[0]:
        ocorrencia+=1
    #Somatório para fazer a média
    media+=lista[index]
    #Soma dos números negativos
    if lista[index]<0:
        soma+=lista[index]
#Somatório dividido pelo tamanho da lista, para fazer a média
media/=len(lista)

print(f'Maior valor: {maiorvalor}')
print(f'Menor valor: {menorvalor}')
print(f'Lista de números pares: {listapares}')
print(f'Número de ocorrências do primeiro elemento: {ocorrencia}')
print(f'Média dos elementos: {media:.2f}')
print(f'A soma dos números negativos é: {soma}')