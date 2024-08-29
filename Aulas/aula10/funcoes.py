
# numero1 = int(input('Informe o número: '))
# numero2 = int(input('Informe o número: '))

# print('A soma é: ', numero1 + numero2)

# # A função "max" serve para buscar o maior número na lista abaixo, e o "min" busca o menor número.
# # A função "len" mostra a quantidade de números que tem numa lista
# # A função "sum" soma os números que estão na lista

# numeros = [1, 5, 8, 10, 3, 78, 100]

# print(max(numeros))
# print(min(numeros))
# print(len(numeros))
# print(sum(numeros))

# media = sum(numeros) / len(numeros)

# # Vamos criar uma função livremente para não ter que repetir uma linha de comando para fazer a mesma função.

# def media (numeros):
#     resultado = sum(numeros) / len(numeros)
#     return resultado
# print(media(numeros))

# Criando uma função para somar dois números


# def soma (numero1 , numero2):
#     soma = (numero1 + numero2)
#     return soma

# print(soma(15, 35))

# Criando uma função simples sem retorno

# def saudacao(nome):
#     print(f'Olá {nome}')

# # Uso da função
# saudacao('Luciano')

# Fazendo uma função com esccolha opcional, onde a pessoa escolhe ou não colocar algo na pergunta

# def ola(nome, mensagem='Olá'):
#     print(mensagem , nome)

# ola('Luciano')

# Função com multiplo retorno. Nesse caso abaixo, as duas barras significa que é uma divisão absoluta, e a porcentagem é o resto da divisão.

# def dividir (numero1 , numero2):
#     resposta = numero1 // numero2
#     resto = numero1 % numero2
#     return resposta, resto

# divisao, resto_divisao = dividir(9, 2)

# print(divisao, resto_divisao)

# função lambda. depois da função lambda, o "a, b" são os valores que serão utilizados, seguidos de dois pontos e depois o que essa função fará com os valores.
# Essa função é boa para minimizar uma função

# somar = lambda a, b: a + b
# print(somar(10, 5))

# Argumentos posicionais, eu tenho que colocar um asterisco na variável e ele me fala que iremos usar múltiplos argumentos


# def exibir_informacoes(*args):
#     print('Argumentos posicionais: ', args)

# exibir_informacoes(1, 4, 'luciano', 'teste')

# def exibir_informacoes2(**args):
#     print('Argumentos posicionais: ', args)

# exibir_informacoes2(nome ='Luciano' , idade = 30 , curso = 'python')

# Conceito de dicionário
# pessoa = variável | "nome; idade; estado_civil; escolaridade" são as chaves (keys) | "Luciano, 30, casado, especialista" é o valor da chave (value)

# Essa programação abaixo, está me falando que a variável 'pessoa' tem uma lista dentro dela e as informações estão entre chaves. Observe que no final de cada chave
# tem uma vírgula, e caso tenha que adicionar outra variável, que no caso 'pessoa2', na última chave que fecha o dicionário da variável 'pessoa', tem que ter uma
# vírgula para separar os dicionários.



# pessoa ={
#     'nome' : 'Luciano',
#     'idade' : 30,
#     'estado_civil' : 'casado',
#     'escolaridade' : 'especialista'
# },
# pessoa2 ={
#     'nome' : 'Daniel',
#     'idade' : 19,
#     'estado_civil' : 'casado',
#     'escolaridade' : 'especialista'
# }

# Continua....

