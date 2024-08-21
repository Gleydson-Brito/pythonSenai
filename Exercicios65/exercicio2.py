# 2. Escreva um programa que peça ao usuário para inserir um número e verifique se o número é maior que 10.

numero = int(input('Digite um número qualquer: '))
if (numero < 10):
    print('Numero menor que dez')
elif (numero == 10):
    print('Numero igual a dez')
else:
    print('Numero maior que dez')