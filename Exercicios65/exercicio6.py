# 6. Desenvolva um programa que pergunte ao usuário uma operação matemática (+, -, *, /) e dois números, e realize a operação escolhida.

operacao = str(input('Escolha uma das seguintes operações matemáticas + - * /: '))

numero1 = int(input('Escolha um número inteiro qualquer: '))
numero2 = int(input('Escolha um segundo número inteiro qualquer: '))

if(operacao == '+'):
    operacao =  numero1 + numero2
    print(f'O resultado é: {operacao}')
if(operacao == '-'):
    operacao =  numero1 - numero2
    print(f'O resultado é: {operacao}')
if(operacao == '*'):
    operacao =  numero1 * numero2
    print(f'O resultado é: {operacao}')
if(operacao == '/'):
    operacao =  numero1 / numero2
    print(f'O resultado é: {operacao}')
else:
    print('Você não escolheu uma operação matemática válida')