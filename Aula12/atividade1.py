cidade=str(input('Digite o nome de uma cidade qualquer: ')).title().strip()

cidade2=cidade.split()

if cidade2[0]=='Santa':
    print('A cidade começa com o nome "Santa".')
else:
    print('A cidade NÃO começa com o nome "Santa".')

#------------------------------------------------JEITO DA PROFE----------------------------------------------------------
cidade=input('Em que cidade você nasceu? ').strip()

print(cidade[:5].upper()== 'SANTA')