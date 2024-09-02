import os

nomes = []
operacao = 'sim'


def menu():
    opcoes = ['Cadastrar nome', 'Atualizar nome',
              'Excluir nome', 'Listar nome']

    for indice, opcao in enumerate(opcoes):
        print(f'{indice + 1} - {opcao}')


def listar_nomes():
    for indice, nome in enumerate(nomes):

        print(f' {indice} - {nome}')


while operacao == 'sim':
    menu()

    opcao = int(input('Informe a ação desejada: '))

    match opcao:
        case 1:
            nome = input('Qual nome deseja cadastrar? \n')
            nomes.append(nome)
        case 2:
            nome = input('Qual nome deseja atualizar? \n')
            novo_nome = input('Qual será o novo nome? \n')
            nomes[nomes.index(nome)] = novo_nome
        case 3:
            nome = input('Qual nome deseja excluir? \n')
            nomes.remove(nome)
        case 4:
            listar_nomes()

        case _:
            print('opção inválida')
    operacao = input('Deseja realizar outra operação? \n').lower()
    os.system('clear')

    if operacao != 'sim':
        break
