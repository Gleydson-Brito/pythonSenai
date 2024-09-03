numeros_pares = list()

for i in range(10):
    numero = int(input('Informe o numero: '))
    if numero % 2 == 0:
        numeros_pares.append(numero)
print(f'Os números pares são: ', sorted(numeros_pares))

# O sorted serve pra organizar a lista do menor para o maior