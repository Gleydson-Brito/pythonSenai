
nomes = []
operacao = 'sim'

while operacao == 'sim':
    print('1 - Cadastre o nome')
    print('2 - Atualize o nome')
    print('3 - Exclua o nome')
    print('4 - Listar os nomes')
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
            for indice, nome in enumerate(nomes):
             
                print(f' {indice} - {nome}')
        case _:
            print('opção inválida')
    operacao = input('Deseja realizar outra operação? \n').lower()

    if operacao != 'sim':
        break