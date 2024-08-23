# 13. Crie um algoritmo que solicite ao usuário um mês do ano (1 a 12) e exiba a estação do ano correspondente.

mes = int(input('Escolha um número de 1 a 12 correspondente ao mês do ano \n'))

if mes >= 1 and mes <= 3:
    print('Esse mês nós estaremos na primavera')
elif mes >= 4 and mes <= 6:
    print('Esse mês nós estaremos no verão')
elif mes >= 7 and mes <= 9:
    print('Esse mês nós estaremos no outono')
elif mes >= 10 and mes <=12:
    print('Esse mês nós estaremos no inverno')
else:
    print('Escolha inválida')