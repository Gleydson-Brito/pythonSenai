# 9. Crie um algoritmo que verifique se um número inserido pelo usuário é par ou ímpar.

numero = int(input('Digite um número para verificarmos se é par ou ímpar \n'))

if numero % 2 == 0:
    print('O nímero é par')
else:
    print('O número é ímpar')