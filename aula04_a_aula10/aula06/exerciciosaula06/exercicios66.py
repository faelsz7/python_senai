nomes = ['abu', 'abi', 'ebo']

operacao = 'sim'

while operacao == 'sim':
    print('1 casdastre seu nome')
    print('2 atualize seu nome')
    print('3 exclua o nome')
    print('4 lista de nomes')
    opcao=int(input('informe a opçao desejada \n'))

    match opcao:
        case 1:
            nome = input('escrev o nome: \n')
            nomes.append(nome)
        case 2:
            nome = input ('que nome deseja atualizar? \n')
            novo_nome = input('qual sera o novo nome? \n')

            nomes[nomes.index(nome)] = novo_nome
        case 3:
            nome = input('Que nome deseja remover? \n')
            nomes.remove(nome)
        case 4:
            for indice, nome in enumerate(nomes):
                print(f'{indice} - {nome}')
        case _:
            print('invalido')
    
    operacao = input('Deseja fazer algo mais? \n').lower()

    if operacao != 'sim':
        break
