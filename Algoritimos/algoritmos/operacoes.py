import email


nomes = []

def menu():
    opcoes = ['Cadastrar nome', 'Atualizar nome', 'Excluir nome', 'Listar nome']

    for indice, opcao in enumerate(opcoes):
        print(f'{indice + 1} - {opcao}')

def listar_nomes():
    for indice, nome in enumerate(nomes):
             
        print(f' {indice} - {nome}')

def cadastrar_nome(nome):
    aluno = {'nome': nome, 'email': email, 'data_nascimento': data_nascimento }
    nomes.append(nome, email, data_nascimento )

def atualiza_nome(nome, novo_nome):
    nomes[nomes.index(nome)] = novo_nome

def excluir_nome(nome):
    nomes.remove(nome)