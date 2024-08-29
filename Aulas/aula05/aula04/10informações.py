# Receba 10 informações de cadastro pessoal e informe um relatorio com as informações em um unico print.

print('Vamos agora coletar algumas informações sobre você. Responda as perguntas abaixo.')

nome = str(input('Digite o seu nome: '))
endereco = str(input('Digite o seu endereço: '))
telefone = int(input('Digite o número do seu telefone: '))
email = str(input('Digite o seu e-mail: '))
altura = float(input('Digite a sua altura: '))
diaNascimento = int(input('Digite o dia do seu nascimento, por exemplo; 14: '))
mesNascimento = str(input('Digite o mês do seu nascimento, por exemplo; janeiro: '))
anoNascimento = int(input('Digite o ano do seu nascimento, por exemplo; 2005: '))
idade = str(input('Digite a sua idade : '))
cidadeNascimento = str(input('Diga a cidade em que nasceu: '))
estadoNascimento = str(input('Em qual Estado fica a cidade que nasceu?: '))

print(f'Seu nome é: {nome} seu endereço é: {endereco} o seu telefone é: {telefone} seu e-mail é: {email} sua altura é: {altura} você nasceu no dia {diaNascimento} no mês de {mesNascimento} no ano de {anoNascimento} e sua idade é: {idade} a cidade que você nasceu foi {cidadeNascimento} e o estado no qual nasceu foi {estadoNascimento} ')