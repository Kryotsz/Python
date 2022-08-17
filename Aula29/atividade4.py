def quantidade_de_numeros(num):
    digitos=len(str(num))
    return digitos

num=int(input('Digite um número: '))
print(f'O número {num} tem {quantidade_de_numeros(num)} dígitos.')
