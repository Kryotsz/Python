# help(print)

def escreve(msg): #As aspas duplas """ criam a documentação da função, para poder usar no help
    """ 
    Print de mensagem informada pelo usuário
    msg: entrada do usuário para o programa
    """
    tamanho=(len(msg)+2)
    print('~'*tamanho)
    print(msg)
    print('~'*tamanho)

'''escreve(input('Digite uma frase: '))'''

#help(escreve)

def teste(b):
    b+=4 #Variável de escopo local
    c=2 #Variável de escopo local
    print(f'"A" dentro da função vale {a}')
    print(f'"B" dentro da função vale {b}')
    print(f'"C" dentro da função vale {c}')

a=5 #Variável de escopo global
teste(a)
print(f'"A" fora da função vale {a}')
#print(f'"B" fora da função vale {b}') #NameError: name 'b' is not defined
#print(f'"C" fora da função vale {c}') #NameError: name 'c' is not defined

