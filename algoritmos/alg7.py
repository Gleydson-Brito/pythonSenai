meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for indice, mes in enumerate(meses):
    print(f'{indice + 1} - {mes}')

mes_escolhido = int(input('Informe o mês escolhido: '))
    
if mes_escolhido > 2 and mes_escolhido < 7:
    print('Estamos no outono')