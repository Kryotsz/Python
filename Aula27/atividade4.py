'''def ajuda(comando):
    help(comando)

while True:
    comando=''
    comando=str(input('Digite o nome do comando: '))
    if comando.strip().upper()=='FIM':
        print('\033[31m~\033[m'*30, end='')
        print('\033[32m~\033[m'*30, end='')
        print('\033[33m~\033[m'*30, end='')
        print('\n\033[31m{:^77}\033[m'.format('PROGRAMA ENCERRADO'))
        print('\033[31m~\033[m'*30, end='')
        print('\033[32m~\033[m'*30, end='')
        print('\033[33m~\033[m'*30, end='')
        break
    else:
        ajuda(comando)'''
#INCOMPLETO
#--------------------------------------------------JEITO DA SORA
c=('\033[m', '\033[0;30;41m', '\033[0;30;42m', '\033[0;30;43m', '\033[0;30;44m', '\033[0;30;45m', '\033[7;30;46m')

def ajuda(com):
    titulo(f'Acessando o manual de comandos {com}',4)
    print(c[6], end='')
    help(com)
    print(c[0], end='')

def titulo(msg,cor=0):
    tam=len(msg)+4
    print(c[cor], end='')
    print('~'*tam)
    print(f'{msg}')
    print('~'*tam)
    print(c[0], end='')

comando=''
while True:
    titulo('Ajuda Python',2)
    comando=input('Função ou Biblioteca: ')
    if comando.upper()=='FIM':
        break
    else:
        ajuda(comando)