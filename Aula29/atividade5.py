def reverso(num):
    reverso=int(str(num)[::-1])
    return reverso

n=int(input('Digite um número: '))
print(f'O reverso do número \033[32m{n}\033[m é \033[32m{reverso(n)}\033[m')