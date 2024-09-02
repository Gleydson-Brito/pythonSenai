from os import system
import operacoes as op

# from operacoes import menu, listar_nomes
# import operacoes

operacao = 'sim'


while operacao == 'sim':
    op.menu()

    opcao = int(input('Informe a ação desejada: '))

    match opcao:
        case 1:
            nome = input('Qual nome deseja cadastrar? \n')
            op.cadastrar_nome(nome)
        case 2:
            nome = input('Qual nome deseja atualizar? \n')
            novo_nome = input('Qual será o novo nome? \n')
            op.atualiza_nome(nome, novo_nome)
        case 3:
            nome = input('Qual nome deseja excluir? \n')
            op.excluir_nome(nome)
        case 4:
            op.listar_nomes()

        case _:
            print('opção inválida')
    operacao = input('Deseja realizar outra operação? \n').lower()
    system('clear')

    if operacao != 'sim':
        break
