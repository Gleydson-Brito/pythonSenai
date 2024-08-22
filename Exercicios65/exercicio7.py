# 7. Escreva um programa que peça ao usuário uma nota de 0 a 10 e classifique a nota como "Baixa", "Média" ou "Alta" usando estrutura condicional if.

numero = float(input('Digite a nota do aluno:'))

if numero <= 5:
    print('A nota do aluno é baixa')
elif numero > 5 and numero < 7.5:
    print('A nota do aluno é média')
else:
    print('Parabéns! A nota do aluno é alta')
