

divisores = list()

numero = int(input('Informe o número '))

for i in range(1, numero +1):
    if numero  % i == 0:
        divisores.append(i)

print(divisores)