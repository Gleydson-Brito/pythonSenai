# 4. Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.
from ssl import VERIFY_DEFAULT




cor = str(input('Escolha uma cor entre vermelho, verde e azul '))

if(cor == 'vermelho'):
    print('Você escolheu a cor vermelha')
elif(cor == 'verde'):
    print('Você escolheu a cor verde')
elif(cor == 'azul'):
    print('Você escolheu a cor azul')
else:
    print('Você não escolheu nenhuma das cores')
