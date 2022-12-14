# Converter Tupla em Lista

dias=('Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado')

semana=list(dias)

print(f'A variável semana é do tipo {type(semana)} e contém {semana}')

#---------------------------------------------------------------------------------
#Lista NÃO comprimida
num=[]
for n in range(0,10):
    num.append(n**2)

print(num)

#A MESMA lista só que COMPRIMIDA
lista1=[x**2 for x in range(10)]
print(lista1)

#Outro exemplo de lista comprimida
lista2=[x for x in range(1,20) if x%2==0]
print(lista2)

lista3=[i for i in "HACKATHON" if i in ['A', 'E', 'I', 'O', 'U']]
print(lista3)

lista4=[1,2,3]
lista4=[i**3 for i in lista4] #atribuir novos valores aos elementos da lista através de uma operação
print(lista4)