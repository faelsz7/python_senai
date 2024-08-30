def menu():
    opecoes = [ 'Cadastrar nome', 'Atualiza nome', 'Excluir nomes', 'Lista de nomes']

    for indice ,opcao in enumerate(opecoes):
        print(f'{indice +1} - {opcao}')

def listar_nomes():
    for indice ,nome in enumerate(nomes):
        print(f'{indice} - {nome}')

def cadastrar_nome(nome):
    nomes.append(nome )

def atualiza_nome(nome, novo_nome):
    nomes[nomes.index(nome)] = novo_nome

def excluir_nome(nome):
    nomes.remove(nome)