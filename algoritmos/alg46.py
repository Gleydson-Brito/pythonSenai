total = int()

for i in range(1, 11):
    numero = int(input(f'informe o número {i}: '))
    total += numero

media = total / 10
print('a média é: ', media)