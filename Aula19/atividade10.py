soma=cont=0

estatura=float(input('Informe a estatura do aluno: '))

menor=estatura
maior=estatura
soma+=estatura
cont+=1

while True:
    estatura=float(input('Informe a estatura do aluno: '))
    if estatura<=0:
        break
    else:
        soma+=estatura
        if estatura>maior:
            maior=estatura
        if estatura<menor:
            menor=estatura
        cont+=1
media=soma/cont
print(f'A menor estatura é {menor} \nA maior estatura é {maior} \nA média das estaturas informadas é {media}')