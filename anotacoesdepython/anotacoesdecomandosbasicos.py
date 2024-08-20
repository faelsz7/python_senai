1. Impressão de Texto
print("Olá, mundo!")  # Imprime uma string
print(42)            # Imprime um número inteiro
print(3.14)          # Imprime um número de ponto flutuante
2. Variáveis
nome = "João"
idade = 30
altura = 1.75
3. Tipos de Dados
print(nome)
print(idade)
print(altura)
4. Operadores Aritméticos
a = 10
b = 5
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
modulo = a % b
exponenciacao = a ** b
print(soma, subtracao, multiplicacao, divisao, divisao_inteira, modulo, exponenciacao)
5. Estruturas Condicionais
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")

6. Laços de Repetição
Para repetir ações, use for e while loops:

Laço for:
python
Copiar código
for i in range(5):  # Vai de 0 até 4
    print(i)
Laço while:
python
Copiar código
contador = 0
while contador < 5:
    print(contador)
    contador += 1
7. Funções
Funções permitem que você defina blocos de código reutilizáveis:

python
Copiar código
def saudacao(nome):
    return f"Olá, {nome}!"

nome_usuario = "Maria"
print(saudacao(nome_usuario))
8. Listas
Listas são coleções de itens que podem ser de diferentes tipos:

python
Copiar código
frutas = ["maçã", "banana", "laranja"]
print(frutas[0])  # Acessa o primeiro item da lista

frutas.append("manga")  # Adiciona um item à lista
print(frutas)

for fruta in frutas:
    print(fruta)
9. Dicionários
Dicionários armazenam pares chave-valor:

python
Copiar código
dados_pessoais = {
    "nome": "Ana",
    "idade": 25,
    "cidade": "São Paulo"}


print(dados_pessoais["nome"])  # Acessa o valor associado à chave "nome"

dados_pessoais["email"] = "ana@example.com"  # Adiciona um novo par chave-valor
print(dados_pessoais)
10. Comentários
Comentários são usados para explicar o código e são ignorados pelo Python:

python
Copiar código
# Este é um comentário de uma linha

"""
Este é um comentário de múltiplas linhas.
Pode ser usado para fornecer explicações mais detalhadas.
"""

11. Importação de Módulos
Você pode usar módulos (bibliotecas) para adicionar funcionalidades ao seu código:

python
Copiar código
import math

print(math.sqrt(16))  # Imprime a raiz quadrada de 16
12. Manipulação de Strings
Strings em Python têm muitos métodos úteis:

python
Copiar código
texto = "hello world"
print(texto.upper())     # Converte para maiúsculas
print(texto.lower())     # Converte para minúsculas
print(texto.title())     # Capitaliza a primeira letra de cada palavra
print(texto.replace("world", "Python"))  # Substitui 'world' por 'Python'