
# Estudando um pouco de "if" e "elif"

# Fazendo um exemplo de uma votação a presidente utilizando o 'if' 'elif' e 'else'. 

# candidato = int(input('informe o número do candidato \n'))

# if candidato == 13:
#     print('Votou no lula')
# elif candidato == 22:
#     print ('Votou no Bolsonaro')
# else:
#     print('Candidado inválido')

# Utilizando a estrutura 'match' onde se ele não tiver nenhum número correspondente ao candidato, que está representado no comando 'case 13:' onde caso não seja
# nenhum dos números que estão relacionado em 'case + número', então tenho que colocar uma variável para caso a escolha de candidato não exista, que no caso seria
# o comando 'case _:'

# candidato = int(input('informe o número do candidato \n'))
# match candidato:
#     case 13:
#         print('Votou no companheiro Lula')
#     case 22:
#         print('Votou no capitão Bolsonaro')
#     case _:
#         print('Sai de cima do muro')


# Utilizando um número qualquer e construindo um contador, como se fosse eu pegar um número qualquer e atribuir uma soma, subtração, multiplicação ou divisão baseado no
# primeiro númenro mais a outra parte. Retribuição de valor

# numero = 10

# numero = numero + 10
# print(numero)

# numero = numero - 10
# print(numero)

# numero = numero * 10
# print(numero)

# numero = numero / 10
# print(numero)

# Também pode ser feito da seguinte maneira, onde coloca-se a variável, o sinal que quer atribuir e depois da igualdade, colocar o valor que quer atribuir
# Exemplo

# numero = 10

# numero += 10
# print(numero)

# numero -= 10
# print(numero)

# numero *= 10
# print(numero)

# numero /= 10
# print(numero)

# O mod é utilizado para saber se o resto da divisão é um número par ou ímpar. O mod é representado pela porcentagem %
# Verificando se o número é par ou ímpar utilizando o mod (%)

# numero = int(input('Informe o número: '))
# if numero % 2 == 0:
#     print('O número é par')
# else:
#     print('O número é ímpar')

# Laços de repetição
# Estamos agora usando uma estrutura de repetição, onde eu posso repetir uma resposta quantas vezes eu quiser. Utilizamos o comando (for), a letra (i) de índice
# o (in) que é 'em' e o tamanho (range) das repetições. Exemplo

# for i in range(5):
#     print('gleydson')

# Variável lista
# É utilizando para criar várias informações na mesma variável. Utilizando colchetes '[]' Exemplo

# nomes = ['Luciano', 'Lucas', 'Arthur', 'Aline', 'Beatriz']
# print(nomes)

# for nome in nomes:
#     print(nome)

# frutas = ['banana', 'maçã', 'morango', 'laranja']
# for fruta in frutas:
#     print(fruta)

# Para melhor entender essa parte, esse algoritmo 'for fruta in frutas' significa: Para cada Fruta(índice) na lista de Frutas, imprima esse índice.

# Para selecionar e enumerar a lista, utilizamos o 'for' 'in' e logo depois o comando 'enumerate"

# frutas = ['banana', 'maçã', 'morango', 'laranja']
# for indice, fruta in enumerate(frutas):
#     print(f'Suas frutas são: {indice}: {fruta} ')

# Para ter uma lista vazia e acrescentar os dados que forem pedidas, utilizaremos um comando chamado 'append'

# nomes = []

# for i in range(5):
#     nome = input('Informe o seu nome: ')
#     nomes.append(nome)

# for nome in nomes:
#     print(nome)

# O outro tipo de laço usado é o 'while' que significa 'enquanto'. Utilizando o while, significa que enquanto a condição específica não for atendida, ela irá 
# repetir infinitamente a´te a condição ser aceita.

# numero = None
# while numero != 0:
#     numero = int(input('Digite o número \n'))

# contador = 1
# numero = int(input("Informe o número: "))

# while contador <= 10:
#     print(numero * 2)
#     contador +=1

# numero = 10
# while True:
#     numero *= 10
#     print(numero)
#     if numero > 1000000000000:
#         break

