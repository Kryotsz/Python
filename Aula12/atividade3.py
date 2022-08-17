altura1=float(input('Informe a estatura da primeira pessoa: '))
altura2=float(input('Informe a estatura da segunda pessoa: '))
altura3=float(input('Informe a estatura da terceira pessoa: '))

if altura1>altura2>altura3:
    print('A estatura da pessoa mais alta é: {:.2f}m.'.format(altura1))
    print('A estatura da pessoa do meio é: {:.2f}m.'.format(altura2))
    print('A estatura da pessoa mais baixa é: {:.2f}m.'.format(altura3))
else:
    if altura2>altura1>altura3:
        print('A estatura da pessoa mais alta é: {:.2f}m.'.format(altura2))
        print('A estatura da pessoa do meio é: {:.2f}m.'.format(altura1))
        print('A estatura da pessoa mais baixa é: {:.2f}m.'.format(altura3))
    else:
        if altura3>altura2>altura1:
            print('A estatura da pessoa mais alta é: {:.2f}m.'.format(altura3))
            print('A estatura da pessoa do meio é: {:.2f}m.'.format(altura2))
            print('A estatura da pessoa mais baixa é: {:.2f}m.'.format(altura1))
        else:
            if altura1>altura3>altura2:
                print('A estatura da pessoa mais alta é: {:.2f}m.'.format(altura1))
                print('A estatura da pessoa do meio é: {:.2f}m.'.format(altura3))
                print('A estatura da pessoa mais baixa é: {:.2f}m.'.format(altura2))
            
# ------------------------------------------------JEITO DA PROFE ------------------------------------------------------
alt1=float(input('Digite a estatura da primeira pessoa: '))
alt2=float(input('Digite a estatura da segunda pessoa: '))
alt3=float(input('Digite a estatura da terceira pessoa: '))

mais_alto=alt1
est_mediana=alt1
mais_baixo=alt1

if alt1>alt2 and alt1>alt3:
    mais_alto=alt1
    if alt2>alt3:
        est_mediana=alt2
        mais_baixo=alt3
    else:
        est_mediana=alt3
        mais_baixo=alt2
elif alt2>alt1 and alt2>alt3:
    mais_alto=alt2
    if alt1>alt3:
        est_mediana=alt1
        mais_baixo=alt3
    else:
        est_mediana=alt3
        mais_baixo=alt1
else:
    mais_alto=alt3
    if alt1>alt2:
        est_mediana=alt1
        mais_baixo=alt2
    else:
        est_mediana=alt2
        mais_baixo=alt1

print('Mais alto: {:.2f}m. Mediano: {:.2f}m. Mais baixo: {:.2f}m.'.format(mais_alto, est_mediana, mais_baixo))