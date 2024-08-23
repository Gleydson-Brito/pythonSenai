# 15. Escreva um programa que pergunte ao usuário uma idade e verifique se a pessoa é adolescente (entre 13 e 17 anos).

idade = int(input('Digite a sua idade \n'))

if idade >= 13 and idade <= 17:
    print('Você é adolecente')
elif idade > 0 and idade < 13:
    print('Você é uma criança')
else:
    print('Você é um adulto')