maior=0
parar=False

valor1=float(input('Digite um valor: '))
valor2=float(input('Digite um valor diferente: '))

while not parar:
    menu=int(input('1) Somar \n2) Multiplicar \n3) Maior \n4) Novos números \n5) Sair do programa \nQual sua opção: '))

    if menu==1:
        print(f'A soma dos valores {valor1} e {valor2} é: {valor1+valor2:.2f}')
    elif menu==2:
        print('A multiplicação dos valores {} e {} é: {}'.format(valor1,valor2,valor1*valor2))
    elif menu==3:
        if valor1>valor2:
            maior=valor1
        else:
            maior=valor2    
        print('O maior número entre os valores {} e {} é: {}'.format(valor1,valor2,maior))
    elif menu==4:
        print('Você escolheu digitar novos valores.')
        valor1=float(input('Digite um valor: '))
        valor2=float(input('Digite um valor diferente: '))
    elif menu==5:
        print('Programa Finalizado!')
        parar=True
    print('#'*30)

#------------------------------------------------JEITO DA PROFE-------------------------------------------------------


n1=int(input('Primeiro valor: '))
n2=int(input('Segundo valor: '))

opcao=0

while opcao!=5:
    print('''[1] Somar
    [2] Multiplicação
    [3] Maior
    [4] Novos números
    [5] Sair do programa''')
    opcao=int(input('Qual é a sua opção: '))

    if opcao==1:
        soma=n1+n2
        print(f'A soma entre {n1} e {n2} = {soma}')
    elif opcao==2:
        produto=n1*n2
        print(f'O produto entre {n1} e {n2} = {produto}')
    elif opcao==3:
        if n1>n2:
            maior=n1
        else:
            maior=n2
        print(f'Entre {n1} e {n2} o maior valor = {maior}')
    elif opcao==4:
        print('Informe novos números: ')
        n1=int(input('Primeiro número: '))
        n2=int(input('Segundo número: '))
    elif opcao==5:
        print('Finalizando...')
    else:
        print('Opção inválida.')
    print('#'*10)

print('Fim.')
