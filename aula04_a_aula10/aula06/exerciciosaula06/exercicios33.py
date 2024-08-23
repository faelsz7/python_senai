#Crie um programa que solicite ao usuário o valor de um 
# produto e calcule o desconto de 10%.

# Solicita o valor do produto ao usuário
valor_produto = float(input("Digite o valor do produto: "))

# Calcula o desconto de 10%
desconto = valor_produto * 0.10

# Calcula o valor com desconto
valor_com_desconto = valor_produto - desconto

# Exibe o resultado
print(f"O valor com desconto é R$ {valor_com_desconto:.2f}")
