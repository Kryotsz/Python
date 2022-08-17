frase=input('Digite uma frase: ').replace(' ',('')).upper().strip()
if frase==frase[::-1]:
    print('É palíndromo')
else:
    print('Não é palíndromo')

# ---------------------------------------------JEITO DA PROFE---------------------------------------------------------

frase=input('Digite uma frase: ').strip().upper()

palavras=frase.split()
junto=''.join(palavras)
inverso=''

for letra in range(len(junto)-1,-1,-1):
    inverso+=junto[letra]

if inverso==junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo!')

#--------------------------------------------OUTRO JEITO---------------------------------------------------------------

frase=input('Digite uma frase: ').strip().upper()

palavras=frase.split()
junto=''.join(palavras)
inverso=junto[::-1]
print(f'O inverso de {junto} é {inverso}')
if inverso==junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada NÃO é um palíndromo!')