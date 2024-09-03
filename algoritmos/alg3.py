dias_semana = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado']

for indice, dia in enumerate(dias_semana):
    print(f'{indice + 1} - {dia}')

dia = int(input('Informe um número de 1 a 7 \n'))

print(f'O dia que você escolheu foi: {dias_semana[dia - 1]}')