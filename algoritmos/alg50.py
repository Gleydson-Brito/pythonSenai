
# numero = int(input('Digite um número qualquer: '))

# # while numero >=1:
# #     print(numero, end=' ')
# #     numero -= 1

# for i in range(numero, 0, -1):
#     print(i, end=' ')

# Essa parte abaixo é para entender como funcionam as hierarquias no python. 
# Para entender como funciona, tem que tirar o comando global texto2.

texto1 = 'Luciano lopes'

def saudacao():
    print(f'Olá {texto1} - esse texto veio da função')
    # global texto2
    texto2 = 'tia Fran'
    print(f'Olá {texto2} - esse texto veio da função')

saudacao()
print(f'Olá {texto1} - esse texto veio de fora da função')
print(f'Olá {texto2} - esse texto veio de fora da função')