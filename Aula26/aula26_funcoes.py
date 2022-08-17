def exibirMensagem(): #Define a função
    print('Python é fácil') #O que a função irá fazer

exibirMensagem() #Chama a função
#-----------------------------------------------
def exibirMensagemBoasVindas(pessoa, mensagem): #Função com 2 parâmetros que terão de ser informados depois
    print(f'{mensagem}, {pessoa}')

exibirMensagemBoasVindas('Igor', 'Bem-Vindo') #Chamando a função e informando os parâmetros
#--------------------------------------------------------------------
def exibirMensagemBoasVindas(pessoa='Fulano', mensagem='Bem-Vindo'): #Declarando a função e informando os valores dos parâmetros
    print(f'{mensagem}, {pessoa}')

exibirMensagemBoasVindas() #Dái só precisa chamar, sem informar mais nada
#---------------------------------------------------------------------