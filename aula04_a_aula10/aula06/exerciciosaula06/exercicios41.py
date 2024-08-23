#41. Crie um programa que peça ao usuário um número inteiro positivo e exiba todos os números de 1 até o número informado.

# Solicita um número inteiro positivo ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
while numero <= 0:
    print("Número inválido. Digite um valor positivo.")
    numero = int(input("Digite um número inteiro positivo: "))

# Exibe os números de 1 até o número informado
contador = 1
while contador <= numero:
    print(contador)
    contador += 1
