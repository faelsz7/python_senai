from os import system
import operacoes as op

nomes = ['abu', 'abi', 'ebo']

operacao = 'sim'

while operacao == 'sim':
    op.menu()
    opcao=int(input('informe a opçao desejada \n'))

    match opcao:
        case 1:
            nome = input('escrev o nome: \n')
            op.cadastrar_nome(nome)
        case 2:
            nome = input ('que nome deseja atualizar? \n')
            novo_nome = input('qual sera o novo nome? \n')

            op.atualiza_nome(nome, novo_nome)
        case 3:
            nome = input('Que nome deseja remover? \n')

            op.excluir_nome(nome)
        case 4:
            op.lista_nomes(nome)
        case _:
            print('invalido')
    
    operacao = input('Deseja fazer algo mais? \n').lower()
    os.system('clear')

    if operacao != 'sim':
        break