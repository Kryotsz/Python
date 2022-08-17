from xml.dom.minidom import Notation


nota=float(input('Informe sua primeira nota: '))
nota2=float(input('Informe sua segunda nota: '))
media=(nota+nota2)/2
if media<5:
    print('REPROVADO!')
elif 5<=media<=6.9:
    print('RECUPERAÇÃO!')
else:
    print('APROVADO!')
