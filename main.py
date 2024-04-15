# borda decorativa de título (console):
def borda(s1):
    tam = len(s1)
    print('.', '-' * tam, '.')
    print('|', s1, '|')
    print('.', '-' * tam, '.')

# título do projeto:
borda('BIBLIOTECH')

lista_livro = []
id_global = 1

# cadastro de livros:
def cadastrar_livro(id):
    borda('CADASTRAR LIVRO')
    global id_global
    nome = input('Nome do livro: ')
    autor = input('Autor do livro: ')
    editora = input('Editora: ')
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro)
    id_global += 1

# consulta de livros:
def consultar_livro():
    borda('CONSULTAR LIVROS')
    while True:
        print('Escolha uma das opções para navegar: \n')
        print('[1] CONSULTAR TODOS \n',
              '[2] CONSULTAR POR ID \n',
              '[3] CONSULTAR POR AUTOR \n',
              '[4] RETORNAR AO MENU')
        opcao = input('Digite aqui a opção desejada: ')
        if (opcao == '1'):
            for livro in lista_livro:
                print(livro)
                return
            # se não houver uma lista:
            print('Você ainda não possui livros cadastrados.')
        elif (opcao == '2'):
            id_busca = int(input('Digite o ID do livro: '))
            for livro in lista_livro:
                if (livro['id'] == id_busca):
                    print(livro)
                    return
            # se digitar errado ou não existir:
            print('Desculpe, livro indisponível ou não encontrado. Por favor, tente novamente.')
        elif (opcao == '3'):
            autor_busca = input('Digite o nome do autor: ')
            for livro in lista_livro:
                if (livro['autor'] == autor_busca):
                    print(livro)
                    return
            # se digitar errado ou não existir:
            print('Desculpe, autor não encontrado. Por favor, tente novamente.')
        elif (opcao == '4'):
            return
        else:
            # se digitar uma opção errada:
            print('Opção inválida, Por favor, tente novamente.')

# remover livros:
def remover_livro():
    borda('REMOVER LIVROS')
    id_remover = int(input('Digite o ID do livro que deseja remover: '))
    for livro in lista_livro:
        if (livro['id'] == id_remover):
            lista_livro.remove(livro)
            print('Livro removido com sucesso.')
        else:
            # se digitar errado:
            print('Desculpe, livro não encontrado. Por favor, tente novamente.')
        return

# menu principal:
def menu():
    while True:
        print('Seja bem-vindo(a) a BIBLIOTECH! Escolha uma das opções para navegar: \n')
        print('[1] CONSULTAR LIVRO \n',
              '[2] CADASTRAR LIVRO \n',
              '[3] REMOVER LIVRO \n',
              '[4] SAIR')
        opcao = input('Digite aqui a opção de navegação desejada: ')
        if opcao == '1':
            consultar_livro()

        elif opcao == '2':
            cadastrar_livro(id_global)

        elif opcao == '3':
            remover_livro()

        elif opcao == '4':
            print('Encerrando...')
            break
        else:
            # se digitar uma opção errada:
            print('Opção inválida. Por favor, tente novamente.')
menu()