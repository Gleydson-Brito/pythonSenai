# 14. Desenvolva um algoritmo que peça ao usuário para digitar dois números e verifique se a soma deles é maior que 100.

numero1 = int(input('Digite o primeiro número \n'))
numero2 = int(input('digite o segundo número \n'))

if numero1 + numero2 > 100:
    print('A soma dos números é maior que 100')
elif numero1 + numero2 == 100:
    print('A soma dos números é igual a 100')
else:
    print('A soma dos números é menor que 100')