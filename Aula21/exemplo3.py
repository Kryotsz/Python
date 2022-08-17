from random import randint

n=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))

print('Os valores sorteados foram: ', end='')
for num in n:
    print(f'\033[32m{num}\033[m', end=' ')
print(f'\nO maior valor sorteado foi \033[32m{max(n)}\033[m')
print(f'O menor valor sorteado foi \033[32m{min(n)}\033[m')
