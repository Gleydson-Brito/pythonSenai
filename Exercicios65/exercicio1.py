# 1. Crie um programa que pergunte ao usuário um número de 1 a 3 e exiba o nome correspondente ao número (1: "um", 2: "dois", 3: "três").


numero =  int(input('Digite um número entre 1 e 3: '))

if numero == 1:
    print('Um')
elif numero == 2:
    print('Dois')
elif numero == 3:
    print('Três')
else:
    print('Numero diferente de 1, 2 ou 3')
