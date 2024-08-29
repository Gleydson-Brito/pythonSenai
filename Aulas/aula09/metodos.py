
# # texto = 'Gleydson Brito da Silva'
# # # Esse capitalize serve para deixar o primeiro caractere da string maiúsculo no começo das frases da string. Nesse caso, será melhor criar uma nova variável para não
# # # mudar a variável inicial, mas também podemos usar a mesma variável para utilizar o capitalize;
# # # Utilizando o print juntamente com a variável 'texto' ficaria assim
# # print(texto.capitalize())

# # # Se fosse da maneira correta, seria com a criação de outra variável para não alterar a variável inicial, ficando assim:

# # texto2 = texto.capitalize()
# # print(texto2)

# # # Utilizando o 'lower', ele vai priorizar a string em minúsculo. Ele vai transformar a string 'nome' em todas as letras minúsculas

# # nome = 'GlEyDson bRItO'
# # nome2 = 'gleydson brito'

# # print(nome.lower())

# # # Esse comando abaixo serve para fazer uma comparação com as duas strings, colocando ambas em letras minúsculas e comparando as duas se são iguais ou não

# # # if nome.lower() == nome2.lower():
# # #     print('são iguais')
# # # else:
# # #     print('não são iguais')

# # # Utilizando o 'replace', nós podemos substituir caracteres especiais, como ç, ã, õ, etc. 

# # silvano_sales = 'coração'

# # #Aqui eu crio outra variável e o replace, entre partênteses, eu coloco a letra que quero mudar, acrescento a vírgula e coloco em seguida a letra que eu quero substituir


# # silvano_sales2 = silvano_sales.replace('ç', 'c').replace('ã','a')
# # print(silvano_sales2)

# # # Utilizando o 'strip', ele faz com que eu consiga remorver os espaços na variável.

# # jack_stripador = '       removendo espaços de uma string          '
# # print(jack_stripador)
# # print(jack_stripador.strip())

# # Utilizando o 'split', serve para separar a string, fazendo que ela se torne uma lista com cada palavra da string.

# # espalhada = 'Gleydson Brito da Silva'
# # print(espalhada)
# # print(espalhada.split())

# #Utilizando o 'join', onde ele serve para transofmrar elementos de uma lista em uma string. Concatena strings

# # nome_lista = ['Gleydson', 'Brito', 'da', 'Silva']
# # print(''.join(nome_lista))

# # No 'join', observe que quando abrimos o comando 'print', colocamos as aspas sem nada dentro, porque ali tem que ter o caractere que será utilizado para 
# # separar e concatenar o que está na variável "nome_lista". No caso acima, como não colocamos nada ali, ele colocará a lista que foi transformada em string
# # sem nada para separar.

# # print('-'.join(nome_lista))

# # Aqui está separando com traço

# # Utilizamos o "slice" para manipular a string por índice. Não tem um comando para ele, mas para utilizar, colocamos entre colchetes[] e utilizamos dois pontos ":"
# # dentro do colchete. Antes dos pontos, colocamos a posição do inicial do índice e depois dos pontos a posição final. Se deixar em branco, ele busca do começo ao fim

# # cidade = 'Recanto das emas, cidade do povo'
# # print(cidade[:13])

# # # Aqui, ele está pegando do primeiro índice que começa a contar do zero e está indo até o índice 13.
# # # Se eu quiser inverter a string, eu utilizo dois pontos duas vezes seguido de -1. Exemplo

# # cidade = 'Recanto das emas, cidade do povo'
# # print(cidade[::-1])

# # Para ver se a palavra é uma palíndromo, ou seja, uma palavra ou frase que pode ser lida de trás para frente, podemsps utilizar o slice para fazer isso e ainda
# # fazer com que mesmo que seja digitado a primeira letra diferente, entre maiúscula e minúscula, ele padronize elas utilizando ou o "lower" ou "upper"

# # palindromo = 'Arara'
# # if palindromo.lower() == palindromo[::-1].lower():
# #     print('É palindromo')
# # else:
# #     print('Não é palindromo')

# cavaleiros = ['Seya', 'Shun', 'Shiryu', 'Yoga']
# print(cavaleiros)
# # Para adicionar um novo elemento no final dessa lista, eu utilizo o .append
# cavaleiros.append('Ikki')
# print(cavaleiros)

# # Para adicionar várias listas de uma só vez, usaremos o .extend em vez do .append

# cavaleiros.extend(['Shina', 'Maryn'])
# print(cavaleiros)

# # Para inserir na lista em uma posição específica, utilzamos o "insert"

# cavaleiros.insert(0, 'Athena')
# print(cavaleiros)

# # Depois do insert, o 0 é a posição no qual vai ficar a nova informação.

# # Ao utilizar o "remove", eu excluo a informação que eu escolher

# cavaleiros.remove('Shun')
# print(cavaleiros)

# # "pop" exclui e último item da lista

# cavaleiros.pop()
# print(cavaleiros)

# # Aqui eu vejo quem foi o último da lista
# elemento = cavaleiros.pop()
# print(cavaleiros)
# print(elemento)

# # Aqui eu falo qual a posição eu quero exluir
# cavaleiros.pop(0)
# print(cavaleiros)
# print(elemento)

# # index - retorna o indice da primeira ocorrencia de um valor procurado

# print(cavaleiros.index('Yoga'))
# cavaleiros.pop(cavaleiros.index('Yoga'))
# print(cavaleiros)

# # Para alterar um indice caso não saiba qual a posição ele está, podemos fazer da seguinte forma:

# cavaleiros[cavaleiros.index('Ikki')] = 'Ikki de fenix'
# print(cavaleiros)

# Para eu contabilizar a quantidade de elementos repeditos, eu utilizo o "count"

# print(cavaleiros.count('Aldebaran'))

# "sort" ordena a lista de forma crescente

frutas = ['morango', 'maça', 'abacaxi', 'kiwi', 'amora', 'umbu', 'laranja', 'bergamota']
numeros = [9, 5, 81, 100, 33, 21, 2]

frutas.sort()
numeros.sort()

print(frutas)
print(numeros)

# reverse - Ele vai pegar a lista e inverter ela, ou seja, se a lista estiver em ordem do menor para o maior, ele fará do maior para o menor

frutas.reverse()
numeros.reverse()

print(frutas)
print(numeros)

# para eu apagar umas lista, eu utilizo o "clear"

frutas.clear()
print(frutas)

# Para deletar da e nunca mais voltar a lista, pode usar o "del". Um vez feito é irreversível

del frutas
print(frutas)