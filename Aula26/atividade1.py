def area(largura, comprimento):
    area=largura*comprimento
    return area

largura=float(input('Digite a largura do terreno: '))
comprimento=float(input('Digite o comprimento do terreno: '))

print(area(largura, comprimento))

#------------------------------------JEITO DA PROFE

def area(larg, comp):
    a=larg*comp
    print(f'A área de um terreno {larg}X{comp} é de {a:.2f}m².')

print('Controle de terrenos')
l=float(input('Largura (m): '))
c=float(input('Comprimento (m): '))
area(l,c)