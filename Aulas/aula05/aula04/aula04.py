# numero1 = int(input('Digite o primeiro número \n'))
# numero2 = int(input('Digite o segundo número \n'))

# print(numero1 + numero2)
# print(type(numero1))
# print(type(numero2))

# nome = 'gleydson'
# print(type(nome))
# idade = 42
# print(type(idade))
# altura = 1.76
# print(type(altura))
# vivo = False
# print(type(vivo))

# int()
# float()
# str()
# bool()

numero1 = int(input('Digite o primeiro número \n'))
numero2 = int(input('Digite o segundo número \n'))

soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = numero1 / numero2

# existem algumas formas de contatenar os comandos, por exemplo colocar uma frase antes de cada resposta

print('A soma é: ', soma)
print('A subtração é: '+ str(subtracao))
print('A multiplicação é: {} e a divisão foi {} '.format(multiplicacao, divisao))
print(f'A multiplicação é: {multiplicacao} e a divisão foi: {divisao}')