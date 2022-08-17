from MinhasFuncoes import *
'''
print('~'*20)
menu=int(input('Cálculo \n1.Círculo \n2.Triângulo \n3.Retângulo \nQual figura deseja calcular a área: '))
print('~'*20)

if menu<1 or menu>3:
    print('Digite um valor de 1 a 3.')
elif menu==1:
    calcula_area_circulo()
elif menu==2:
    calcula_area_triangulo()
elif menu==3:
    calcula_area_retangulo()
'''
#--------------------------------------------JEITO DA SORA-----------------------------------------------------------
'''
print('Cálculo das áreas de figuras geométricas:')
escolha=int(input('1.Círculo \n2.Triângulo \n3.Retângulo \nEscolha uma opção: '))

if escolha==1:
    raio=float(input('Informe o raio: '))
    area=calcula_area_circulo(raio)
    print(f'Área do círculo: {area:.2f}')
elif escolha==2:
    base=float(input('Informe a base: '))
    altura=float(input('Informe a altura: '))
    area=calcula_area_triangulo(base, altura)
    print(f'Área do triângulo: {area:.2f}')
elif escolha==3:
    base=float(input('Informe a base: '))
    altura=float(input('Informe a altura: '))
    area=calcula_area_retangulo(base, altura)
    print(f'Área do retângulo: {area:.2f}')
else:
    print('Opção inválida.')
'''
#-----------------------------------------------------------------------------------------------------------
'''
matriz=gera_matriz_aleatoria()
linhas=len(matriz)
colunas=len(matriz[0])
print('~'*30)
print('MATRIZ')
for l in range(linhas):
        for c in range(colunas):
            print(f'[{matriz[l][c]:^3}]', end='')
        print()
print('~'*30)
print(f'O traço da matriz é: {calcula_traco_matriz(matriz)}')
print('~'*30)
'''
#----------------------------------------------------JEITO DA SORA---------------------------------------------
'''
linhas=int(input('Informe a quantidade de linhas da matriz: '))
colunas=int(input('Informe a quantidade de colunas da matriz: '))
intervalo_inicial=int(input('Informe o intervalo inicial: '))
intervalo_final=int(input('Informe o intervalo final: '))

m=gera_matriz_aleatoria(linhas, colunas, intervalo_inicial, intervalo_final)
print(f'Matriz gerada: \n{m}')

if len(m)==len(m[0]):
    print(f'Traço da matriz gerada: {calcula_traco_matriz(m)}')
else:
    print('Não é possível calcular o traço da matriz, pois não é quadrada.')
'''
#-------------------------------------------------------------------------------------------------------
'''
matrizA=gera_matriz_aleatoria()
matrizB=gera_matriz_aleatoria()
matrizC=soma_matrizes(matrizA, matrizB)
linhas=len(matrizC)
colunas=len(matrizC[0])
print('~'*30)
print('MATRIZ A:')
for l in range(linhas):
        for c in range(colunas):
            print(f'[{matrizA[l][c]:^3}]', end='')
        print()
print('~'*30)
print('MATRIZ B:')
for l in range(linhas):
        for c in range(colunas):
            print(f'[{matrizB[l][c]:^3}]', end='')
        print()
print('~'*30)
print('MATRIZ C:')
for l in range(linhas):
        for c in range(colunas):
            print(f'[{matrizC[l][c]:^3}]', end='')
        print()
print('~'*30)
'''
#-------------------------------------------------JEITO DA SORA----------------------------------------------
'''
linhas=int(input('Informe a quantidade de linhas da matriz: '))
colunas=int(input('Informe a quantidade de colunas da matriz: '))
intervalo_inicial=int(input('Informe o intervalo inicial: '))
intervalo_final=int(input('Informe o intervalo final: '))

a=gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final)
b=gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final)

if len(a)==len(b) and len(a[0])==len(b[0]):
    print(f'Matriz A: \n{a} \nMatriz B: \n{b} \nMatriz C: \n{soma_matrizes(a,b)}')
else:
    print('As matrizes não possuem a mesma ordem.')
'''
#---------------------------------------------------------------------------------------------------------------
'''
matrizA=gera_matriz_aleatoria()
K=int(input('Informe o valor para a constante K: '))
print(f'MATRIZ A: \n{matrizA} X K={K} = \nMATRIZ C: \n{multipla_matriz_por_constante(matrizA, K)}')
'''
#---------------------------------------------JEITO DA SORA--------------------------------------------------------
'''
linhas=int(input('Informe a quantidade de linhas da matriz: '))
colunas=int(input('Informe a quantidade de colunas da matriz: '))
intervalo_inicial=int(input('Informe o intervalo inicial: '))
intervalo_final=int(input('Informe o intervalo final: '))

m1=gera_matriz_aleatoria(linhas,colunas,intervalo_inicial,intervalo_final)
constante=int(input('Informe a constante que multiplica a matriz gerada: '))
print(f'Matriz gerada: \n{m1} \nMatriz C (M1*Constante): \n{multipla_matriz_por_constante(m1,constante)}')
'''
#--------------------------------------------------------------------------------------------------------------
#NÃO FIZ


#-------------------------------------------------JEITO DA SORA------------------------------------------------------
'''
cadastro=obtem_dados_funcionario()
print(retorna_num_hom_mul(cadastro))
'''