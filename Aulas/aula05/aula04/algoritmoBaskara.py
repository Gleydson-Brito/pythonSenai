# crie um algoritimo capaz de calcular o delta da formula de bascara
import math


print('Vamos calcular o Delta da fóruma de Báskara')

valorA = float(input('Digite o valor de A: '))
valorB = float(input('Digite o valor de B: '))
valorC = float(input('Digite o valor de C: '))

print('Lembrando que a fórmula do Delta de Báskara é B^2-4xAxC, vamos calcular.')

raiz = math.sqrt(valorB)
calculo1 = (raiz) - (4 * valorA * valorC)

print('O valor de Delta é: ', calculo1)