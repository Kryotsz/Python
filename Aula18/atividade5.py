
from random import randint

vitorias=0

print('Você jogará PAR ou ÍMPAR contra o computador.')

escolha=str(input('Você quer ser PAR ou ÍMPAR? ').strip().upper().replace('I','Í'))

while True:
    computador=randint(1,10)
    num=int(input('Digite um número de 1 a 10: '))
    if num%2==0 and computador%2==0 and escolha=='PAR':
        print('VOCÊ VENCEU, você digitou {} e o computador escolheu {}, o resultado deu PAR'.format(num,computador))
        vitorias+=1
    elif num%2==0 and computador%2!=0 and escolha=='PAR':
        print('VOCÊ PERDEU, você digitou {} e o computador escolheu {}, o resultado deu ÍMPAR. \nVocê teve {} vitórias consecutivas'.format(num,computador,vitorias))
        break
    elif num%2!=0 and computador%2==0 and escolha=='PAR':
        print('VOCÊ PERDEU, você digitou {} e o computador escolheu {}, o resultado deu ÍMPAR. \nVocê teve {} vitórias consecutivas'.format(num,computador,vitorias))
        break
    elif num%2!=0 and computador%2!=0 and escolha=='PAR':
        print('VOCÊ VENCEU, você digitou {} e o computador escolheu {}, o resultado deu PAR'.format(num,computador))
        vitorias+=1
    elif num%2==0 and computador%2==0 and escolha=='ÍMPAR':
        print('VOCÊ PERDEU, você digitou {} e o computador escolheu {}, o resultado deu PAR. \nVocê teve {} vitórias consecutivas'.format(num,computador,vitorias))
        break
    elif num%2==0 and computador%2!=0 and escolha=='ÍMPAR':
        print('VOCÊ VENCEU, você digitou {} e o computador escolheu {}, o resultado deu ÍMPAR'.format(num,computador))
        vitorias+=1
    elif num%2!=0 and computador%2==0 and escolha=='ÍMPAR':
        print('VOCÊ VENCEU, você digitou {} e o computador escolheu {}, o resultado deu ÍMPAR'.format(num,computador))
        vitorias+=1
    elif num%2!=0 and computador%2!=0 and escolha=='ÍMPAR':
        print('VOCÊ PERDEU, você digitou {} e o computador escolheu {}, o resultado deu PAR. \nVocê teve {} vitórias consecutivas'.format(num,computador,vitorias))
        break

#---------------------------------------------------------------------OUTRO JEITO------------------------------------------------------------
from random import randint

vitorias=0

escolha=str(input('Você quer ser PAR ou ÍMPAR? ')).strip().upper().replace('Í','I')
print('-'*110)

while True:
    computador=randint(0,10)
    if escolha not in 'PI':
        escolha=str(input('\033[1;31mOPÇÃO INVÁLIDA!\033[m Escolha novamente entre PAR ou ÍMPAR: ')).strip().upper().replace('Í','I')
        print('-'*110)
    if escolha[0]=='P':
        jogador=int(input('Digite um número de 0 a 10: '))
        if jogador%2==0:
            if computador%2==0:
                print('\033[1;32mVOCÊ VENCEU!\033[m Sua escolha foi \033[1;36m{}\033[m que é \033[1;32mPAR\033[m, o computador escolheu \033[1;36m{}\033[m que é \033[1;32mPAR\033[m, o resultado deu \033[1;36m{}\033[m que é \033[1;32mPAR!\033[m'.format(jogador,computador,jogador+computador))
                vitorias+=1
                print('-'*110)
            else:
                print(f'\033[1;31mVOCÊ PERDEU!\033[m Sua escolha foi \033[1;36m{jogador}\033[m que é \033[1;32mPAR\033[m, o computador escolheu \033[1;36m{computador}\033[m que é \033[1;31mÍMPAR\033[m, o resultado deu \033[1;36m{jogador+computador}\033[m que é \033[1;31mÍMPAR!\033[m \n\033[1;32mO número de vitórias consecutivas foi: {vitorias}\033[m')
                print('-'*110)
                break
        else:
            if computador%2==0:
                print(f'\033[1;31mVOCÊ PERDEU!\033[m Sua escolha foi \033[1;36m{jogador}\033[m que é \033[1;31mÍMPAR\033[m, o computador escolheu \033[1;36m{computador}\033[m que é \033[1;32mPAR\033[m, o resultado deu \033[1;36m{jogador+computador}\033[m que é \033[1;31mÍMPAR!\033[m \n\033[1;32mO número de vitórias consecutivas foi: {vitorias}\033[m')
                print('-'*110)
                break
            else:
                print(f'\033[1;32mVOCÊ VENCEU!\033[m Sua escolha foi \033[1;36m{jogador}\033[m que é \033[1;31mÍMPAR\033[m, o computador escolheu \033[1;36m{computador}\033[m que é \033[1;31mÍMPAR\033[m, o resultado deu \033[1;36m{jogador+computador}\033[m que é \033[1;32mPAR!\033[m')
                vitorias+=1
                print('-'*110)
    elif escolha[0]=='I':
        jogador=int(input('Digite um número de 0 a 10: '))
        if jogador%2==0:
            if computador%2==0:
                print(f'\033[1;31mVOCÊ PERDEU!\033[m Sua escolha foi \033[1;36m{jogador}\033[m que é \033[1;31mPAR\033[m, o computador escolheu \033[1;36m{computador}\033[m que é \033[1;31mPAR\033[m, o resultado deu \033[1;36m{jogador+computador}\033[m que é \033[1;31mPAR!\033[m \n\033[1;32mO número de vitórias consecutivas foi: {vitorias}\033[m')
                print('-'*110)
                break
            else:
                print(f'\033[1;32mVOCÊ VENCEU!\033[m Sua escolha foi \033[1;36m{jogador}\033[m que é \033[1;31mPAR\033[m, o computador escolheu \033[1;36m{computador}\033[m que é \033[1;32mÍMPAR\033[m, o resultado deu \033[1;36m{jogador+computador}\033[m que é \033[1;32mÍMPAR!\033[m')
                vitorias+=1
                print('-'*110)
        else:
            if computador%2==0:
                print(f'\033[1;32mVOCÊ VENCEU!\033[m Sua escolha foi \033[1;36m{jogador}\033[m que é \033[1;32mÍMPAR\033[m, o computador escolheu \033[1;36m{computador}\033[m que é \033[1;31mPAR\033[m, o resultado deu \033[1;36m{jogador+computador}\033[m que é \033[1;32mÍMPAR!\033[m')
                vitorias+=1
                print('-'*110)
            else:
                print(f'\033[1;31mVOCÊ PERDEU!\033[m Sua escolha foi \033[1;36m{jogador}\033[m que é \033[1;32mÍMPAR\033[m, o computador escolheu \033[1;36m{computador}\033[m que é \033[1;32mÍMPAR\033[m, o resultado deu \033[1;36m{jogador+computador}\033[m que é \033[1;31mPAR!\033[m \n\033[1;32mO número de vitórias consecutivas foi: {vitorias}\033[m')
                print('-'*110)
                break