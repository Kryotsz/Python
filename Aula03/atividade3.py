# Programa para calcular velocidade média
final=float(input('Quantos metros o objeto percorreu durante seu trajeto? '))
inicio=float(input('Qual o ponto de partida do objeto (em metros)? '))
deslocamento=final-inicio
tempofinal=float(input('Quantos segundos o objeto levou para percorrer todo o trajeto? '))
tempoinicial=float(input('Quando o objeto começou seu deslocamento, qual era o tempo em segundos? '))
tempo=tempofinal-tempoinicial
velmedia=deslocamento/tempo
print('O objeto se deslocou numa velocidade média de {:.2f} m/s'.format(velmedia))
