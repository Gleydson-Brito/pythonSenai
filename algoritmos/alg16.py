
combustiveis = [
    {
        'nome' : 'diesel',
        'valor': 6.50
    },
    {
        'nome' : 'gasolina',
        'valor' : 6.17
    },
    {
        'nome' : 'etanol',
        'valor' : 4.45
    }
]

for indice, combustivel in enumerate(combustiveis):
    print(f'{indice} - {combustivel["nome"]}')

escolha = int(input('Informe o número do combustivel desejado: '))

print(f'O valor por litro é: {combustiveis[escolha]["valor"]}')