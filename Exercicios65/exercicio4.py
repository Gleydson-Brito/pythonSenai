# 4. Crie um algoritmo que solicite ao usuário uma cor (vermelho, verde, azul) e exiba uma mensagem correspondente à cor escolhida.
from ssl import VERIFY_DEFAULT


cor1 = 1
cor2 = 2
cor3 = 3

cor = int(input('Escolha uma cor entre vermelho(1), verde(2) e azul(3) '))

if(cor == 1):
    print('Cor vermelha')
elif(cor == 2):
    print('Cor verde')
elif(cor == 3):
    print('Cor azul')
else:
    print('teste')
