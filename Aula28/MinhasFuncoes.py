def calcula_area_circulo():
    from math import pi
    raio=float(input('Digite o valor do raio: '))
    area=pi*(raio**2)
    print(f'A área de um CÍRCULO de raio {raio} é {area}')

def calcula_area_triangulo():
    base=float(input('Digite o valor da base: '))
    altura=float(input('Digite o valor da altura: '))
    area=(base*altura)/2
    print(f'A área de um TRIÂNGULO de base {base} e altura {altura} é {area}')

def calcula_area_retangulo():
    base=float(input('Digite o valor da base: '))
    altura=float(input('Digite o valor da altura: '))
    area=base*altura
    print(f'A área de um RETÂNGULO de base {base} e altura {altura} é {area}')

#----------------------------------------JEITO DA SORA--------------------------------------------------------
'''
from math import pi

def calcula_area_circulo(raio):
    return pi*raio**2

def calcula_area_triangulo(base, altura):
    return (base*altura)/2

def calcula_area_retangulo(base, altura):
    return base*altura
'''
#--------------------------------------------------------------------------------------
def gera_matriz_aleatoria():
    from random import randint

    matriz=[]

    linhas=int(input('Informe a quantidade de linhas da matriz: '))
    colunas=int(input('Informe a quantidade de colunas da matriz: '))
    intervaloinicial=int(input('Digite o intervalo inicial: '))
    intervalofinal=int(input('Digite o intervalo final: '))

    for l in range(linhas):
        linha=[]
        for c in range(colunas):
            linha.append(randint(intervaloinicial, intervalofinal))
        matriz.append(linha)

    return matriz

def calcula_traco_matriz(matriz):
    soma=0
    linhas=len(matriz)
    colunas=len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            if i==j:
                soma+=matriz[i][j]
    return soma
#-----------------------------------------------------JEITO DA SORA-------------------------------------------------
'''
def gera_matriz_aleatoria(linhas, colunas, intervalo_inicial, intervalo_final):
    from random import randrange
    m=[[randrange(intervalo_inicial, intervalo_final) for i in range(colunas)]for j in range(linhas)]
    return m

def calcula_traco_matriz(matriz):
    traco=[]
    soma=0
    for i in range(len(matriz)):
        traco.append(matriz[i][soma])
        soma+=1
    return sum(traco)
'''
#------------------------------------------------------------------------------
def soma_matrizes(matrizA, matrizB):
    somaA=[]
    somaB=[]
    matrizC=[]
    linhas=len(matrizA)
    colunas=len(matrizA[0])

    for i in range(linhas):
        linha=[]
        for j in range(colunas):
            linha.append(matrizA[i][j])
        somaA.append(linha)

    for i in range(linhas):
        linha=[]
        for j in range(colunas):
            linha.append(matrizB[i][j])
        somaB.append(linha)
    
    for i in range(linhas):
        linha=[]
        for j in range(colunas):
            linha.append(somaA[i][j]+somaB[i][j])
        matrizC.append(linha)
    
    return matrizC
#-------------------------------------------------JEITO DA SORA-----------------------------------------------
'''
def soma_matrizes(a,b):
    c=[]
    for i in range(len(a)):
        c.append([])
        for j in range(len(a[i])):
            c[i].append(a[i][j]+b[i][j])
    return c
'''
#-----------------------------------------------------------------------------
def multipla_matriz_por_constante(matriz, k):
    matrizC=[]
    for i in range(len(matriz)):
        linha=[]
        for j in range(len(matriz[0])):
            linha.append((matriz[i][j])*k)
        matrizC.append(linha)
    return matrizC
#--------------------------------------------------JEITO DA SORA---------------------------------------------------------
'''
def multiplica_matriz_por_constante(matriz, constante):
    m=[]
    for i in range(len(matriz)):
        m.append([])
        for j in matriz[i]:
            m[i].append(j*constante)
    return m
'''
#------------------------------------------------------------------------------
#NÃO FIZ



#---------------------------------------------------JEITO DA SORA----------------------------------------------------
'''
def obtem_dados_funcionario():
    func=[['Ana','F'], ['Beatriz','F'], ['Carla','F'], ['Daniela','F'], ['Emílio','M'], ['Fernando','M'], ['Ítalo', 'M']]
    return func

def retorna_num_hom_mul(matriz):
    h=m=0
    linha=len(matriz)
    coluna=len(matriz[0])
    for nome, dados in matriz:
        print(nome, dados)
    
    for i in range(linha):
        if matriz[i][1]=='F':
            m+=1
        else:
            h+=1
    return f'Quantidade de mulheres cadastradas: {m} \nQuantidade de homens cadastrados: {h}'
'''