frase=input('Digite uma frase qualquer: ').upper().strip()
frase2=frase.replace(' ','')
print('A letra "A" aparece na frase {} vezes. \nSua primeira aparição é na posição {}. \nSua última aparição é na posição {}.'.format(frase.count('A'),frase2.find('A')+1,frase2.rfind('A')+1))
