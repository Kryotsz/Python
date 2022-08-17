tupla=('abelha', 'besouro', 'camelo', 'dinossauro', 'elefante', 'flamingo', 'guepardo', 'hiena')

for palavra in tupla:
    print(f'A palavra {palavra.upper()} apresenta as vogais: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra.upper(), end=' ')
    print()
