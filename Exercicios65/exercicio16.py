# 16. Desenvolva um programa que peça ao usuário um tipo de combustível (gasolina, etanol, diesel) e exiba o preço correspondente por litro.

combustivel = str(input('Escolha um tipo de combustível, entre gasolina, etanol e diesel \n'))

if combustivel == 'gasolina':
    print('O preço da gasolina é 5,89')
elif combustivel == 'etanol':
    print('O preço do etanol é 4,08 ')
elif combustivel == 'diesel':
    print('O preço do diesel é 5,49 ')
else:
    print('Combustível inválido')