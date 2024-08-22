#eu como um inutiu nao conseguir fazer esta porra e foi ia
def obter_estacao(mes):
    if 1 <= mes <= 12:
        if 3 <= mes <= 5:
            return "Outono"
        elif 6 <= mes <= 8:
            return "Inverno"
        elif 9 <= mes <= 11:
            return "Primavera"
        else:
            return "Verão"
    else:
        return "Mês inválido"

try:
    mes = int(input("Digite o número do mês (1 a 12): "))
    estacao = obter_estacao(mes)
    print(f"A estação correspondente ao mês {mes} é {estacao}.")
except ValueError:
    print("Entrada inválida. Digite um número válido.")
