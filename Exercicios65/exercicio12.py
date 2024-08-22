# 12. Escreva um programa que peça ao usuário para escolher um modo de transporte (carro, bicicleta, a pé) e exiba uma mensagem com a velocidade média correspondente.

transporte = str(input('Olá usuário. Por favor, escolha um dos meios de transporte: carro, bicicleta ou a pe \n'))

if transporte == 'carro':
    print('Esse transporte tem uma velocidade de até 100km/h')
elif transporte == 'bicicleta':
    print('Esse transporte tem uma velociadade de até 25km/h')
elif transporte == 'a pe':
    print('Caminhar faz você ir até 3,6km/h')
else:
    print('Ficar parado não te leva a lugar algum')