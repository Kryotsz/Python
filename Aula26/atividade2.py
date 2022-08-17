def escreva(texto):
    tam=len(texto)+2
    print('~'*tam)
    print(texto)
    print('~'*tam)

texto=input('Informe o texto: ')

escreva(texto)

#--------------------------------------JEITO DA PROFE

def escreva(msg):
    tam=len(msg)+4
    print('~'*tam)
    print(f'{msg}')
    print('~'*tam)

escreva('Na aula de hoje estudamos funções em Python')
escreva('Turma Inf 9 - SENAC - SCS')