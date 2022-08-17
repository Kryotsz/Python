lista=['Maria', 'Janaina', 'José', 'Carlos']
listaa=['José', 'Pedro']

for n in range(0, len(lista)):
    print(lista[n], end=' ')

lista.append('Jorge') #inserir sempre no final

lista.insert(0, 'Jorge') #inserir na posição determinada

lista.sort() #ordenar lista em ordem crescente ou alfabética

lista.sort(reverse=True) #ordenar lista em ordem decrescente ou ordem alfabética reversa

del lista[3] #ou del lista[-1] para remover a última posição

lista.remove('Janaina') #remove o nome Janaina da lista, sem precisar saber a posição

lista.pop() #se não tiver parâmetros, ele remove o último item da lista

lista.clear() #limpa a lista(deixa vazia)

listaa=lista #vincula as duas listas, sendo assim, qualquer mudança em uma delas impacta na outra

listaa=lista[:] #copiar a lista sem vincular
lista.append('José') #o append irá adicionar José no fim da lista, mas não afetará listaa

lista.extend(listaa) #junta as listas, adicionando a listaa no fim da lista

print(lista.count('José'))

print(lista.index('Janaina')) #Mostra a posição do nome determinado

for indice, nome in enumerate(lista): #Mostra o nome e a posição em que o nome se encontra de todos os nomes e posições da lista
    print(f'{nome} está armazenado no índice {indice}')

a=[[2,1,-5],[3,7,0],[6,4,8]] #Matriz

print(a[0][0]+a[0][1]+a[0][2]) #Somar os números da primeira coluna

print(a[0][0], a[0][1], a[0][2]) #imprime os números da primeira coluna

soma_a=0
lin=len(a) #mostra o tamanho da lista, o número de sublistas, 2 sublistas nesse caso já q a primeira é a 0
col=len(a[0]) #mostra o tamanho das sublistas presentes na lista maior

for i in range(lin): #vai ler na linha quantas sublistas tem(3), que é 0, até 2
    for j in range(col): #vai começar na primeira sublista, vendo as colunas da sublista(3) na posição 0, até a posição 2
        soma_a+=a[i][j]

print(soma_a)
