from aula28_00 import *

while True:
    print('~'*40)
    escolha=int(input('Escolha uma das opções: \n1)Soma \n2)Subtração \n3)Divisão \n4)Multiplicação \n5)Todas as operações \nDigite sua escolha: '))
    print('~'*40)
    
    if escolha<=0 or escolha>5:
        print('Opção inválida.')
        print('~'*40)
    else:
        num1=int(input('Digite o primeiro número: '))
        num2=int(input('Digite o segundo número: '))

        if escolha==1:
            s=soma(num1,num2)
            print('~'*40)
            print(f'A soma dos números {num1} e {num2} é {s}')
            print('~'*40)
            break
        elif escolha==2:
            sb=subtracao(num1,num2)
            print('~'*40)
            print(f'A subtração dos números {num1} e {num2} é {sb}')
            print('~'*40)
            break
        elif escolha==3:
            d=divisao(num1,num2)
            print('~'*40)
            print(f'A divisão dos números {num1} e {num2} é {d}')
            print('~'*40)
            break
        elif escolha==4:
            m=multiplicacao(num1,num2)
            print('~'*40)
            print(f'A multiplicação dos números {num1} e {num2} é {m}')
            print('~'*40)
            break
        elif escolha==5:
            c=calculadora(num1,num2)
            print('~'*40)
            print(f'Números= {num1} e {num2} \nSoma= {c[0]} \nSubtração= {c[1]} \nDivisão= {c[2]} \nMultiplicação= {c[3]}')
            print('~'*40)
            break